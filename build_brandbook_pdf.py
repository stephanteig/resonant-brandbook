from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageBreak, PageTemplate, Paragraph, Spacer,
    Table, TableStyle, KeepTogether, Preformatted, Flowable,
)

ROOT = Path(__file__).parent
VERSION = "v0.5"
OUT = ROOT / f"Resonant-Brandbook-{VERSION}.pdf"
DOCS = [ROOT / "README.md", *sorted((ROOT / "Resonant-Style").glob("*.md")), ROOT / "PROJECT_STATUS.md"]
LOGO_MASTER = ROOT / "Assets" / "Logo" / "Color-Variations" / "png" / "01-Primary-Full-Color.png"
APPLICATION_BOARD = ROOT / "Assets" / "Mockups" / "Resonant-logo-applications-v0.3.png"
LOGO_MINT = ROOT / "Assets" / "Logo" / "Color-Variations" / "png" / "05-Monochrome-Emerald.png"
LOGO_VARIANTS = [
    (LOGO_MASTER, "PRIMARY GRADIENT"),
    (LOGO_MINT, "EMERALD"),
    (ROOT / "Assets" / "Logo" / "Color-Variations" / "png" / "03-Monochrome-White.png", "WHITE"),
    (ROOT / "Assets" / "Logo" / "Color-Variations" / "png" / "02-Monochrome-Black.png", "BLACK"),
]
HERO_IMAGE = ROOT / "Assets" / "Editorial" / "resonant-hero-night-water-v0.4.png"
ALBUM_ART = ROOT / "Assets" / "Editorial" / "resonant-album-artwork-v0.4.png"

INK = colors.HexColor("#0B0F0D")
SURFACE = colors.HexColor("#171C1A")
MINT = colors.HexColor("#67F3C2")
EMERALD = colors.HexColor("#30DDA1")
PAPER = colors.HexColor("#F7F8F8")
MUTED = colors.HexColor("#AEBAB5")
LINE = colors.HexColor("#2C3934")
DEEP_GREEN = colors.HexColor("#10251E")
QUIET_GREEN = colors.HexColor("#18352A")
LIME = colors.HexColor("#7BEA73")


def draw_image_contain(canvas, image_path, x, y, max_w, max_h, align="center"):
    if not image_path.exists():
        return
    reader = ImageReader(str(image_path)); iw, ih = reader.getSize()
    scale = min(max_w / iw, max_h / ih); dw, dh = iw * scale, ih * scale
    if align == "left":
        dx = x
    elif align == "right":
        dx = x + max_w - dw
    else:
        dx = x + (max_w - dw) / 2
    dy = y + (max_h - dh) / 2
    canvas.drawImage(reader, dx, dy, width=dw, height=dh, preserveAspectRatio=True, mask="auto")


class AccentRule(Flowable):
    def __init__(self, width=35 * mm):
        super().__init__(); self.width = width; self.height = 5 * mm
    def draw(self):
        self.canv.setStrokeColor(EMERALD); self.canv.setLineWidth(2.2)
        self.canv.line(0, 2 * mm, self.width, 2 * mm)


class ImagePlate(Flowable):
    def __init__(self, image_path, title, subtitle, max_height=145 * mm):
        super().__init__(); self.image_path = image_path; self.title = title; self.subtitle = subtitle
        self.width = 174 * mm; self.height = max_height + 26 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(colors.HexColor("#141412")); c.setStrokeColor(LINE); c.roundRect(0, 0, w, h, 5, fill=1, stroke=1)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 10 * mm, self.title.upper())
        c.setFillColor(PAPER); c.setFont("Helvetica", 8); c.drawString(8 * mm, h - 16 * mm, self.subtitle)
        if self.image_path.exists():
            reader = ImageReader(str(self.image_path)); iw, ih = reader.getSize()
            max_w, max_h = w - 16 * mm, h - 25 * mm
            scale = min(max_w / iw, max_h / ih)
            dw, dh = iw * scale, ih * scale
            x, y = (w - dw) / 2, 5 * mm + (max_h - dh) / 2
            c.drawImage(reader, x, y, width=dw, height=dh, preserveAspectRatio=True, mask="auto")
        c.restoreState()


class LogoCover(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 58 * mm
    def draw(self):
        c = self.canv; c.saveState()
        c.setStrokeColor(LINE); c.setLineWidth(.6); c.line(0, 4 * mm, self.width, 4 * mm)
        draw_image_contain(c, LOGO_MASTER, 0, 11 * mm, self.width, 43 * mm)
        c.restoreState()


class ChapterOpener(Flowable):
    def __init__(self, number, label, title_lines, subtitle="", image_path=None, accent=EMERALD):
        super().__init__(); self.number = number; self.label = label; self.title_lines = title_lines; self.subtitle = subtitle
        self.image_path = image_path; self.accent = accent; self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(DEEP_GREEN if self.image_path is None else INK); c.rect(0, 0, w, h, fill=1, stroke=0)
        if self.image_path and self.image_path.exists():
            reader = ImageReader(str(self.image_path)); iw, ih = reader.getSize(); scale = max(w / iw, h / ih); dw, dh = iw * scale, ih * scale
            p = c.beginPath(); p.rect(0, 0, w, h); c.clipPath(p, stroke=0, fill=0)
            c.drawImage(reader, (w - dw) / 2, (h - dh) / 2, width=dw, height=dh, preserveAspectRatio=True, mask="auto")
            c.setFillColor(colors.Color(0.02, 0.05, 0.04, alpha=.67)); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(colors.Color(0.25, .55, .43, alpha=.28)); c.setFont("Helvetica-Bold", 118); c.drawRightString(w - 5 * mm, h - 57 * mm, f"{self.number:02d}")
        c.setFillColor(self.accent); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 14 * mm, self.label.upper())
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 39); y = h / 2 + 18
        for line in self.title_lines:
            c.drawString(8 * mm, y, line); y -= 43
        if self.subtitle:
            c.setFillColor(MUTED); c.setFont("Helvetica", 9); c.drawString(8 * mm, 29 * mm, self.subtitle)
        c.setStrokeColor(self.accent); c.setLineWidth(2); c.line(8 * mm, 19 * mm, 48 * mm, 19 * mm)
        c.restoreState()


class LogoHeroPage(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(INK); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 14 * mm, "BRAND / THE MARK")
        c.setFillColor(colors.Color(.2, .65, .48, alpha=.16)); c.circle(w / 2, h / 2 + 8 * mm, 65 * mm, fill=1, stroke=0)
        draw_image_contain(c, LOGO_MASTER, 31 * mm, 44 * mm, 112 * mm, 126 * mm)
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 22); c.drawString(8 * mm, 29 * mm, "A signal for listening.")
        c.setFillColor(MUTED); c.setFont("Helvetica", 8.5); c.drawString(8 * mm, 19 * mm, "The symbol is a single geometric unit. Preserve its rhythm, cut-out, and optical balance.")
        c.restoreState()


class LogoDetailPage(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(PAPER); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 14 * mm, "BRAND / DETAIL")
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 29); c.drawString(8 * mm, h - 43 * mm, "The cut-out is the signature.")
        c.setFillColor(colors.HexColor("#56625C")); c.setFont("Helvetica", 9); c.drawString(8 * mm, h - 55 * mm, "Every gap is intentional. It keeps the forms distinct while making them read as one mark.")
        c.setStrokeColor(colors.HexColor("#C7D4CD")); c.setLineWidth(.6); c.rect(8 * mm, 25 * mm, 99 * mm, 126 * mm, fill=0, stroke=1)
        draw_image_contain(c, LOGO_MASTER, 18 * mm, 35 * mm, 79 * mm, 106 * mm)
        c.setStrokeColor(EMERALD); c.setLineWidth(1.2); c.line(111 * mm, 105 * mm, 151 * mm, 132 * mm)
        c.setFillColor(EMERALD); c.circle(111 * mm, 105 * mm, 1.7 * mm, fill=1, stroke=0)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 10); c.drawString(116 * mm, 134 * mm, "CUT-OUT")
        c.setFillColor(colors.HexColor("#56625C")); c.setFont("Helvetica", 8); c.drawString(116 * mm, 126 * mm, "Do not close, widen, or")
        c.drawString(116 * mm, 120 * mm, "treat the negative space")
        c.drawString(116 * mm, 114 * mm, "as decoration.")
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 10); c.drawString(116 * mm, 91 * mm, "OPTICAL BALANCE")
        c.setFillColor(colors.HexColor("#56625C")); c.setFont("Helvetica", 8); c.drawString(116 * mm, 83 * mm, "Use the supplied artwork as")
        c.drawString(116 * mm, 77 * mm, "the visual authority at every")
        c.drawString(116 * mm, 71 * mm, "size and in every medium.")
        c.restoreState()


class LogoClearSpacePage(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(DEEP_GREEN); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 14 * mm, "BRAND / CLEAR SPACE")
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 29); c.drawString(8 * mm, h - 43 * mm, "Let the mark breathe.")
        bx, by, bw, bh = 35 * mm, 55 * mm, 104 * mm, 102 * mm
        c.setStrokeColor(colors.Color(.55, .93, .76, alpha=.6)); c.setDash(3, 3); c.rect(bx, by, bw, bh, fill=0, stroke=1); c.setDash()
        draw_image_contain(c, LOGO_MASTER, bx + 18 * mm, by + 16 * mm, bw - 36 * mm, bh - 32 * mm)
        c.setStrokeColor(MINT); c.setLineWidth(.8); c.line(bx - 14 * mm, by, bx - 14 * mm, by + 14 * mm); c.line(bx - 14 * mm, by, bx, by); c.line(bx - 14 * mm, by + 14 * mm, bx, by + 14 * mm)
        c.setFillColor(MINT); c.setFont("Helvetica-Bold", 9); c.drawString(bx - 29 * mm, by + 18 * mm, "1×")
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 10); c.drawString(8 * mm, 29 * mm, "Minimum clear space: 1× on every side")
        c.setFillColor(MUTED); c.setFont("Helvetica", 8); c.drawString(8 * mm, 19 * mm, "Use 2× for hero, editorial, and presentation applications.")
        c.restoreState()


class LogoSizePage(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(PAPER); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 14 * mm, "BRAND / DIGITAL SIZES")
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 29); c.drawString(8 * mm, h - 43 * mm, "Scale without losing the signal.")
        c.setFillColor(colors.HexColor("#56625C")); c.setFont("Helvetica", 9); c.drawString(8 * mm, h - 55 * mm, "Use the icon-only symbol at compact sizes. Test the cut-out before release.")
        specs = [(180, 45 * mm, "APP ICON"), (64, 30 * mm, "HEADER"), (32, 21 * mm, "FAVICON"), (16, 13 * mm, "MINIMUM TEST")]
        x = 12 * mm
        for px, box, label in specs:
            c.setFillColor(colors.HexColor("#E7EFEB")); c.roundRect(x, 67 * mm, box, box, 6, fill=1, stroke=0)
            draw_image_contain(c, LOGO_MASTER, x + 4 * mm, 71 * mm, box - 8 * mm, box - 8 * mm)
            c.setFillColor(INK); c.setFont("Helvetica-Bold", 8); c.drawString(x, 57 * mm, f"{px} px")
            c.setFillColor(colors.HexColor("#56625C")); c.setFont("Helvetica", 7); c.drawString(x, 51 * mm, label)
            x += box + 8 * mm
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 11); c.drawString(8 * mm, 30 * mm, "At 16 px, approve the silhouette—not the detail.")
        c.setFillColor(colors.HexColor("#56625C")); c.setFont("Helvetica", 8); c.drawString(8 * mm, 20 * mm, "Minimum sizes remain a production test, not a universal guarantee.")
        c.restoreState()


class LogoVariantPage(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(INK); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 14 * mm, "BRAND / APPROVED COLOUR SET")
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 27); c.drawString(8 * mm, h - 43 * mm, "One mark. Seven controlled treatments.")
        paths = [
            ("01-Primary-Full-Color.png", "PRIMARY"), ("02-Monochrome-Black.png", "BLACK"),
            ("03-Monochrome-White.png", "WHITE"), ("04-Monochrome-Forest.png", "FOREST"),
            ("05-Monochrome-Emerald.png", "EMERALD"), ("06-Monochrome-Lime.png", "LIME"),
            ("07-Grayscale.png", "GRAYSCALE"),
        ]
        root = ROOT / "Assets" / "Logo" / "Color-Variations" / "png"
        cell_w, cell_h = 51 * mm, 48 * mm
        for i, (filename, label) in enumerate(paths):
            row, col = divmod(i, 3); x = 8 * mm + col * 55 * mm; y = h - 107 * mm - row * 54 * mm
            is_light = label in {"BLACK", "LIME"}
            c.setFillColor(colors.HexColor("#F4F7F5") if is_light else colors.HexColor("#15231D")); c.roundRect(x, y, cell_w, cell_h, 4, fill=1, stroke=0)
            draw_image_contain(c, root / filename, x + 8 * mm, y + 9 * mm, cell_w - 16 * mm, cell_h - 18 * mm)
            c.setFillColor(INK if is_light else MUTED); c.setFont("Helvetica-Bold", 6.5); c.drawString(x + 5 * mm, y + 4 * mm, label)
        c.restoreState()


class ColorFieldPage(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(INK); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 14 * mm, "FOUNDATION / COLOUR")
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 31); c.drawString(8 * mm, h - 44 * mm, "Colour should arrive as a signal.")
        c.setFillColor(MUTED); c.setFont("Helvetica", 9); c.drawString(8 * mm, h - 56 * mm, "Space is the default. Accent is earned by the content it helps explain.")
        fields = [("CANVAS", "#11100F", colors.HexColor("#11100F"), PAPER), ("SURFACE", "#191816", colors.HexColor("#191816"), PAPER), ("ACCENT", "#D8B36A", colors.HexColor("#D8B36A"), INK), ("MINT SIGNAL", "#67F3C2", MINT, INK)]
        x, y, cell_w, cell_h = 8 * mm, 63 * mm, 77 * mm, 35 * mm
        for i, (name, hx, fill, textc) in enumerate(fields):
            xx = x + (i % 2) * 82 * mm; yy = y + (1 - i // 2) * 43 * mm
            c.setFillColor(fill); c.roundRect(xx, yy, cell_w, cell_h, 4, fill=1, stroke=0)
            c.setFillColor(textc); c.setFont("Helvetica-Bold", 7); c.drawString(xx + 5 * mm, yy + 9 * mm, name)
            c.setFont("Courier", 7); c.drawString(xx + 5 * mm, yy + 4 * mm, hx)
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 12); c.drawString(8 * mm, 30 * mm, "Quiet surfaces. Clear hierarchy. One useful signal.")
        c.setFillColor(MUTED); c.setFont("Helvetica", 8); c.drawString(8 * mm, 20 * mm, "Never use colour alone to communicate state, confidence, or connection.")
        c.restoreState()


class TypographySpecimenPage(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(PAPER); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 14 * mm, "FOUNDATION / TYPOGRAPHY")
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 31); c.drawString(8 * mm, h - 44 * mm, "Type gives context a shape.")
        c.setFillColor(colors.HexColor("#56625C")); c.setFont("Helvetica", 9); c.drawString(8 * mm, h - 56 * mm, "Display leads. Interface clarifies. Data aligns.")
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 33); c.drawString(8 * mm, 115 * mm, "Listen with")
        c.setFillColor(EMERALD); c.drawString(8 * mm, 79 * mm, "context.")
        c.setStrokeColor(colors.HexColor("#C7D4CD")); c.setLineWidth(.6); c.line(8 * mm, 66 * mm, w - 8 * mm, 66 * mm)
        rows = [("DISPLAY", "Inter Tight", "Statements and openings"), ("INTERFACE", "Inter", "Navigation and body"), ("DATA", "Geist Mono", "Measurements and IDs")]
        for i, (role, family, use) in enumerate(rows):
            yy = 52 * mm - i * 13 * mm; c.setFillColor(EMERALD if i == 0 else colors.HexColor("#56625C")); c.setFont("Helvetica-Bold", 7); c.drawString(8 * mm, yy, role)
            c.setFillColor(INK); c.setFont("Helvetica-Bold" if i < 2 else "Courier", 9); c.drawString(42 * mm, yy, family)
            c.setFillColor(colors.HexColor("#56625C")); c.setFont("Helvetica", 7.5); c.drawString(88 * mm, yy, use)
        c.restoreState()


class MotionTimelinePage(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(DEEP_GREEN); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 14 * mm, "BEHAVIOUR / MOTION")
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 31); c.drawString(8 * mm, h - 44 * mm, "Motion explains change.")
        c.setFillColor(MUTED); c.setFont("Helvetica", 9); c.drawString(8 * mm, h - 56 * mm, "The listener should feel the system respond, never watch it perform.")
        x = 24 * mm; top = 127 * mm; bottom = 57 * mm; c.setStrokeColor(MINT); c.setLineWidth(1.1); c.line(x, bottom, x, top)
        events = [("01", "Intent", "A clear action begins"), ("02", "Response", "The relevant surface moves"), ("03", "Settle", "The new state becomes readable"), ("04", "Reduce", "Motion yields to preference")]
        for i, (num, title, desc) in enumerate(events):
            yy = top - i * 24 * mm; c.setFillColor(EMERALD if i == 0 else MINT); c.circle(x, yy, 2.3 * mm, fill=1, stroke=0)
            c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 12); c.drawString(x + 10 * mm, yy + 1 * mm, title)
            c.setFillColor(MUTED); c.setFont("Helvetica", 8); c.drawString(x + 10 * mm, yy - 6 * mm, desc)
            c.setFillColor(EMERALD); c.setFont("Courier", 7); c.drawString(w - 28 * mm, yy + 1 * mm, num)
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 11); c.drawString(8 * mm, 29 * mm, "A quieter transition is still a transition.")
        c.restoreState()


class AccessibilityPage(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(PAPER); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 14 * mm, "SYSTEM / ACCESSIBILITY")
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 30); c.drawString(8 * mm, h - 44 * mm, "Access is part of the system.")
        c.setFillColor(colors.HexColor("#56625C")); c.setFont("Helvetica", 9); c.drawString(8 * mm, h - 56 * mm, "Every state needs a visible, operable, understandable path through it.")
        pillars = [("SEE", "Contrast, focus, hierarchy"), ("HEAR", "Visual alternatives"), ("OPERATE", "Keyboard and touch"), ("RECOVER", "Clear errors and next steps")]
        for i, (title, body) in enumerate(pillars):
            yy = 119 * mm - i * 20 * mm; c.setFillColor(DEEP_GREEN if i % 2 == 0 else QUIET_GREEN); c.roundRect(8 * mm, yy, 158 * mm, 14 * mm, 3, fill=1, stroke=0)
            c.setFillColor(MINT if i % 2 == 0 else LIME); c.setFont("Helvetica-Bold", 8); c.drawString(14 * mm, yy + 8 * mm, title)
            c.setFillColor(PAPER); c.setFont("Helvetica", 8.5); c.drawString(48 * mm, yy + 8 * mm, body)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 11); c.drawString(8 * mm, 29 * mm, "Accessibility is a release gate, not a polish pass.")
        c.restoreState()


class MockupGalleryPage(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(INK); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 14 * mm, "PRODUCT / VISUAL STORY")
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 29); c.drawString(8 * mm, h - 44 * mm, "Show the question, not just the screen.")
        c.setFillColor(MUTED); c.setFont("Helvetica", 9); c.drawString(8 * mm, h - 56 * mm, "Every mockup should make the product decision visible before it explains the component.")
        cards = [("HOME", "Orient me"), ("SEARCH", "Find it"), ("TASTE", "Understand me"), ("PLAYLIST REVIEW", "Help me decide"), ("DISCOVER", "Give me a reason"), ("ACCOUNT", "Keep trust clear")]
        for i, (title, prompt) in enumerate(cards):
            row, col = divmod(i, 2); x = 8 * mm + col * 82 * mm; y = 58 * mm + (2 - row) * 31 * mm
            c.setFillColor(colors.HexColor("#14221C") if row != 1 else colors.HexColor("#1B2E25")); c.roundRect(x, y, 76 * mm, 24 * mm, 4, fill=1, stroke=0)
            c.setFillColor(EMERALD if col == 0 else MINT); c.setFont("Helvetica-Bold", 6.5); c.drawString(x + 5 * mm, y + 15 * mm, title)
            c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 10); c.drawString(x + 5 * mm, y + 6 * mm, prompt)
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 11); c.drawString(8 * mm, 29 * mm, "Principle → product proof → annotated decision → rule.")
        c.restoreState()


class WebsiteStoryPage(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(DEEP_GREEN); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 14 * mm, "PUBLIC SURFACE / WEBSITE")
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 31); c.drawString(8 * mm, h - 44 * mm, "A doorway, not a catalogue.")
        c.setFillColor(MUTED); c.setFont("Helvetica", 9); c.drawString(8 * mm, h - 56 * mm, "The public story earns attention before the product asks for access.")
        stages = [("01", "Hero", "Listen with context."), ("02", "Why", "Context changes the way music stays with us."), ("03", "Product", "Home · Taste · Playlists · Discover"), ("04", "Connect", "Account first. Spotify separately.")]
        x1, x2 = 20 * mm, 154 * mm; c.setStrokeColor(MINT); c.setLineWidth(1); c.line(x1, 91 * mm, x2, 91 * mm)
        for i, (num, title, desc) in enumerate(stages):
            x = x1 + i * 44.5 * mm; c.setFillColor(EMERALD if i == 0 else MINT); c.circle(x, 91 * mm, 3 * mm, fill=1, stroke=0); c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 8); c.drawCentredString(x, 103 * mm, title); c.setFillColor(MUTED); c.setFont("Courier", 7); c.drawCentredString(x, 78 * mm, num)
            c.setFillColor(PAPER); c.setFont("Helvetica", 7.5); c.drawCentredString(x, 66 * mm, desc)
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 12); c.drawString(8 * mm, 29 * mm, "Editorial before explanation. Explanation before permission.")
        c.restoreState()


class LogoVariantsPlate(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 102 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(colors.HexColor("#141412")); c.setStrokeColor(LINE); c.roundRect(0, 0, w, h, 5, fill=1, stroke=1)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 10 * mm, "APPROVED LOGO VARIANTS")
        c.setFillColor(PAPER); c.setFont("Helvetica", 8); c.drawString(8 * mm, h - 16 * mm, "Use the exact supplied artwork on a contrast-safe surface")
        panel_w = (w - 20 * mm) / 4; panel_y = 14 * mm; panel_h = h - 38 * mm
        for i, (path, label) in enumerate(LOGO_VARIANTS):
            x = 8 * mm + i * panel_w
            c.setFillColor(colors.HexColor("#0B0F0D") if label != "BLACK" else colors.HexColor("#F7F8F8")); c.roundRect(x, panel_y, panel_w - 3 * mm, panel_h, 3, fill=1, stroke=0)
            if path.exists():
                reader = ImageReader(str(path)); iw, ih = reader.getSize(); scale = min((panel_w - 10 * mm) / iw, (panel_h - 13 * mm) / ih); dw, dh = iw * scale, ih * scale
                c.drawImage(reader, x + (panel_w - 3 * mm - dw) / 2, panel_y + (panel_h - dh) / 2 + 3 * mm, width=dw, height=dh, preserveAspectRatio=True, mask="auto")
            c.setFillColor(MUTED if label != "BLACK" else INK); c.setFont("Helvetica", 6.5); c.drawCentredString(x + (panel_w - 3 * mm) / 2, panel_y + 4 * mm, label)
        c.restoreState()


class LogoMisusePlate(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 88 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(colors.HexColor("#141412")); c.setStrokeColor(LINE); c.roundRect(0, 0, w, h, 5, fill=1, stroke=1)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 10 * mm, "INCORRECT USAGE")
        c.setFillColor(PAPER); c.setFont("Helvetica", 8); c.drawString(8 * mm, h - 16 * mm, "Every example below is rejected, even when the mark remains recognizable")
        labels = ["STRETCH", "ROTATE", "CROP", "OUTLINE", "SHADOW", "RECOLOUR"]
        cell_w, cell_h = (w - 22 * mm) / 3, 25 * mm
        for i, label in enumerate(labels):
            row, col = divmod(i, 3); x = 8 * mm + col * (cell_w + 3 * mm); y = h - 47 * mm - row * 30 * mm
            c.setFillColor(colors.HexColor("#0F1411")); c.setStrokeColor(LINE); c.roundRect(x, y, cell_w, cell_h, 3, fill=1, stroke=1)
            if LOGO_MINT.exists(): c.drawImage(ImageReader(str(LOGO_MINT)), x + 5 * mm, y + 6 * mm, width=12 * mm, height=13.5 * mm, preserveAspectRatio=True, mask="auto")
            c.setStrokeColor(colors.HexColor("#F06A5B")); c.setLineWidth(1.3); c.line(x + 4 * mm, y + 4 * mm, x + cell_w - 4 * mm, y + cell_h - 4 * mm)
            c.setFillColor(colors.HexColor("#F06A5B")); c.setFont("Helvetica-Bold", 6.5); c.drawString(x + 22 * mm, y + 10 * mm, label)
        c.restoreState()


class EditorialImagePage(Flowable):
    def __init__(self, image_path, kicker, title_lines, caption=""):
        super().__init__(); self.image_path = image_path; self.kicker = kicker; self.title_lines = title_lines; self.caption = caption
        self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(INK); c.rect(0, 0, w, h, fill=1, stroke=0)
        if self.image_path.exists():
            reader = ImageReader(str(self.image_path)); iw, ih = reader.getSize(); scale = max(w / iw, h / ih); dw, dh = iw * scale, ih * scale
            p = c.beginPath(); p.rect(0, 0, w, h); c.clipPath(p, stroke=0, fill=0)
            c.drawImage(reader, (w - dw) / 2, (h - dh) / 2, width=dw, height=dh, preserveAspectRatio=True, mask="auto")
            c.setFillColor(colors.Color(0.02, 0.04, 0.03, alpha=0.48)); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 12 * mm, self.kicker.upper())
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 31); y = h - 62 * mm
        for line in self.title_lines:
            c.drawString(8 * mm, y, line); y -= 34
        if self.caption:
            c.setFillColor(PAPER); c.setFont("Helvetica", 9); c.drawString(8 * mm, 11 * mm, self.caption)
        c.restoreState()


class StatementPage(Flowable):
    def __init__(self, kicker, lines, accent=EMERALD):
        super().__init__(); self.kicker = kicker; self.lines = lines; self.accent = accent; self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(INK); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(self.accent); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 12 * mm, self.kicker.upper())
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 39); y = h / 2 + len(self.lines) * 15
        for line in self.lines:
            c.drawString(8 * mm, y, line); y -= 43
        c.setStrokeColor(self.accent); c.setLineWidth(2); c.line(8 * mm, 19 * mm, 48 * mm, 19 * mm)
        c.restoreState()


class TypographySpread(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(INK); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 12 * mm, "TYPOGRAPHY / HIERARCHY")
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 40); c.drawString(8 * mm, h - 65 * mm, "LISTEN")
        c.setFillColor(MINT); c.setFont("Helvetica-Bold", 40); c.drawString(8 * mm, h - 104 * mm, "WITH")
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 40); c.drawString(8 * mm, h - 143 * mm, "CONTEXT.")
        c.setStrokeColor(LINE); c.line(8 * mm, 45 * mm, w - 8 * mm, 45 * mm)
        c.setFillColor(MUTED); c.setFont("Helvetica", 8); c.drawString(8 * mm, 34 * mm, "DISPLAY / INTERFACE / DATA")
        c.setFillColor(PAPER); c.setFont("Helvetica", 13); c.drawString(8 * mm, 24 * mm, "Inter Tight       Inter       Geist Mono")
        c.restoreState()


class ColorSpacingSpread(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(INK); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 12 * mm, "FOUNDATION / COLOUR + SPACE")
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 28); c.drawString(8 * mm, h - 49 * mm, "Calm complexity")
        swatches = [("GRAPHITE", "#0B0F0D", INK), ("CHARCOAL", "#171C1A", INK), ("MINT", "#67F3C2", INK), ("EMERALD", "#30DDA1", INK), ("PAPER", "#F7F8F8", INK)]
        y = h - 92 * mm; sw = (w - 16 * mm) / len(swatches)
        for i, (label, hx, textc) in enumerate(swatches):
            c.setFillColor(colors.HexColor(hx)); c.rect(8 * mm + i * sw, y, sw - 2, 28 * mm, fill=1, stroke=0); c.setFillColor(textc); c.setFont("Helvetica-Bold", 6.5); c.drawString(10 * mm + i * sw, y + 5 * mm, label)
        c.setStrokeColor(MINT); c.setLineWidth(1); x = 12 * mm; y0 = 61 * mm
        for i, size in enumerate([8, 16, 24, 32, 48, 64]):
            c.rect(x, y0, size * .8, size * .8, fill=0, stroke=1); c.setFillColor(MUTED); c.setFont("Helvetica", 6.5); c.drawString(x, y0 - 5 * mm, f"{size}px"); x += size * .8 + 14 * mm
        c.setFillColor(MUTED); c.setFont("Helvetica", 8); c.drawString(8 * mm, 23 * mm, "Spacing is a rhythm: 8 · 16 · 24 · 32 · 48 · 64")
        c.restoreState()


class ProductMockupSpread(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def card(self, c, x, y, w, h, title, tag, accent=MINT):
        c.setFillColor(colors.HexColor("#121715")); c.setStrokeColor(LINE); c.roundRect(x, y, w, h, 4, fill=1, stroke=1)
        c.setFillColor(accent); c.setFont("Helvetica-Bold", 6.5); c.drawString(x + 4 * mm, y + h - 9 * mm, tag)
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 11); c.drawString(x + 4 * mm, y + h - 20 * mm, title)
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(INK); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 12 * mm, "PRODUCT / VISUAL PROOF")
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 25); c.drawString(8 * mm, h - 42 * mm, "The product is the brand in motion.")
        # Browser shell
        bx, by, bw, bh = 8 * mm, 77 * mm, 158 * mm, 80 * mm
        c.setFillColor(colors.HexColor("#0E1210")); c.setStrokeColor(LINE); c.roundRect(bx, by, bw, bh, 5, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#171C1A")); c.rect(bx, by, 30 * mm, bh, fill=1, stroke=0)
        if LOGO_MINT.exists(): c.drawImage(ImageReader(str(LOGO_MINT)), bx + 5 * mm, by + bh - 17 * mm, width=9 * mm, height=10 * mm, mask="auto")
        for i, label in enumerate(["Home", "Search", "Library", "Playlists", "Discover", "Taste"]):
            c.setFillColor(PAPER if i == 0 else MUTED); c.setFont("Helvetica", 6.5); c.drawString(bx + 5 * mm, by + bh - (27 + i * 9) * mm, label)
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 15); c.drawString(bx + 38 * mm, by + bh - 18 * mm, "Good to see you")
        c.setFillColor(MUTED); c.setFont("Helvetica", 7); c.drawString(bx + 38 * mm, by + bh - 26 * mm, "Your listening, with context.")
        if ALBUM_ART.exists(): c.drawImage(ImageReader(str(ALBUM_ART)), bx + 38 * mm, by + 18 * mm, width=24 * mm, height=24 * mm, mask="auto")
        for i in range(3):
            c.setFillColor(colors.HexColor("#252D29")); c.roundRect(bx + 68 * mm + i * 25 * mm, by + 32 * mm, 20 * mm, 4 * mm, 2, fill=1, stroke=0); c.roundRect(bx + 68 * mm + i * 25 * mm, by + 24 * mm, 14 * mm, 3 * mm, 1, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#19201C")); c.rect(bx + 30 * mm, by, bw - 30 * mm, 12 * mm, fill=1, stroke=0); c.setFillColor(MINT); c.setFont("Helvetica", 6.5); c.drawString(bx + 38 * mm, by + 5 * mm, "NOW PLAYING   A track with context")
        # Feature cards
        self.card(c, 8 * mm, 23 * mm, 50 * mm, 35 * mm, "Taste Profile", "EXPLAIN")
        self.card(c, 62 * mm, 23 * mm, 50 * mm, 35 * mm, "Playlist Review", "REVIEW", EMERALD)
        self.card(c, 116 * mm, 23 * mm, 50 * mm, 35 * mm, "Discover", "WHY THIS", colors.HexColor("#D8B36A"))
        c.restoreState()


class TrustFlowDiagram(Flowable):
    def __init__(self):
        super().__init__(); self.width = 174 * mm; self.height = 218 * mm
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(INK); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(EMERALD); c.setFont("Helvetica-Bold", 7.5); c.drawString(8 * mm, h - 12 * mm, "INTELLIGENCE / TRUST FLOW")
        c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 27); c.drawString(8 * mm, h - 44 * mm, "Context becomes useful")
        c.setFillColor(MUTED); c.setFont("Helvetica", 9); c.drawString(8 * mm, h - 57 * mm, "Every step should explain what it knows, why it matters, and where the person stays in control.")
        labels = [("Spotify", "source"), ("Listening history", "observed"), ("Taste Engine", "calculated"), ("Playlist Review", "reviewable"), ("Discover", "explorable"), ("Recommendation", "chosen")]
        x, y, box_w, box_h = 16 * mm, h - 90 * mm, 142 * mm, 19 * mm
        for i, (title, tag) in enumerate(labels):
            yy = y - i * 23 * mm; c.setFillColor(colors.HexColor("#16201B")); c.setStrokeColor(MINT if i in (0, 5) else LINE); c.roundRect(x, yy, box_w, box_h, 4, fill=1, stroke=1); c.setFillColor(PAPER); c.setFont("Helvetica-Bold", 11); c.drawString(x + 7 * mm, yy + 10 * mm, title); c.setFillColor(MUTED); c.setFont("Helvetica", 7); c.drawRightString(x + box_w - 7 * mm, yy + 10 * mm, tag.upper())
            if i < len(labels) - 1:
                c.setStrokeColor(EMERALD); c.setLineWidth(1.2); c.line(x + box_w / 2, yy - 1 * mm, x + box_w / 2, yy - 4 * mm); c.line(x + box_w / 2, yy - 4 * mm, x + box_w / 2 - 2 * mm, yy - 2 * mm); c.line(x + box_w / 2, yy - 4 * mm, x + box_w / 2 + 2 * mm, yy - 2 * mm)
        c.setFillColor(MUTED); c.setFont("Helvetica", 8); c.drawString(8 * mm, 17 * mm, "Source → calculation → review → choice")
        c.restoreState()


class VisualPlate(Flowable):
    def __init__(self, kind, title, subtitle=""):
        super().__init__(); self.kind = kind; self.title = title; self.subtitle = subtitle; self.width = 174 * mm; self.height = 82 * mm
    def label(self, x, y, value, size=7.5, colour=MUTED):
        self.canv.setFillColor(colour); self.canv.setFont("Helvetica", size); self.canv.drawString(x, y, value)
    def box(self, x, y, w, h, fill=SURFACE, stroke=LINE, radius=3):
        self.canv.setFillColor(fill); self.canv.setStrokeColor(stroke); self.canv.setLineWidth(.5); self.canv.roundRect(x, y, w, h, radius, fill=1, stroke=1)
    def draw(self):
        c = self.canv; c.saveState(); w, h = self.width, self.height
        c.setFillColor(colors.HexColor("#141412")); c.setStrokeColor(LINE); c.roundRect(0, 0, w, h, 5, fill=1, stroke=1)
        self.label(8 * mm, h - 10 * mm, self.title.upper(), 7.5, EMERALD)
        self.label(8 * mm, h - 16 * mm, self.subtitle, 8, PAPER)
        x0, y0 = 8 * mm, 10 * mm; pw, ph = w - 16 * mm, h - 31 * mm
        if self.kind == "palette":
            cols = [("CANVAS", "#11100F", INK), ("INK", "#F4F0E8", INK), ("MUTED", "#BDB7AD", INK), ("LINE", "#38342F", INK), ("ACCENT", "#D8B36A", colors.HexColor("#201A10"))]
            sw = pw / len(cols)
            for i, (name, hx, textc) in enumerate(cols):
                c.setFillColor(colors.HexColor(hx)); c.rect(x0 + i * sw, y0 + 13 * mm, sw - 2, ph - 13 * mm, fill=1, stroke=0); self.label(x0 + i * sw + 3, y0 + 6 * mm, name, 6.5, textc); self.label(x0 + i * sw + 3, y0 + 2 * mm, hx, 6, textc)
        elif self.kind == "logo":
            self.box(x0, y0, pw, ph, fill=colors.HexColor("#11100F")); self.label(x0 + 8 * mm, y0 + ph / 2 + 5, "RESONANT", 22, PAPER); self.label(x0 + 8 * mm, y0 + ph / 2 - 8, "APPROVED WORKING IDENTITY", 7, MINT); c.setStrokeColor(MINT); c.circle(x0 + pw - 22 * mm, y0 + ph / 2, 13 * mm, stroke=1, fill=0); c.line(x0 + pw - 35 * mm, y0 + ph / 2, x0 + pw - 9 * mm, y0 + ph / 2)
        elif self.kind == "shell":
            self.box(x0, y0, pw, ph, fill=INK); sidebar = 34 * mm; c.setFillColor(colors.HexColor("#181715")); c.rect(x0, y0, sidebar, ph, fill=1, stroke=0); 
            if LOGO_MINT.exists(): c.drawImage(ImageReader(str(LOGO_MINT)), x0 + 5 * mm, y0 + ph - 18 * mm, width=10 * mm, height=11.3 * mm, preserveAspectRatio=True, mask="auto")
            self.label(x0 + 5 * mm, y0 + ph - 19 * mm, "Home", 7, MUTED); self.label(x0 + 5 * mm, y0 + ph - 27 * mm, "Search", 7, MUTED); self.label(x0 + 5 * mm, y0 + ph - 42 * mm, "YOUR MUSIC", 6, MINT); self.label(x0 + 5 * mm, y0 + ph - 52 * mm, "Library", 7, PAPER); self.label(x0 + 5 * mm, y0 + ph - 61 * mm, "Playlists", 7, MUTED); self.label(x0 + 5 * mm, y0 + 7 * mm, "Account", 7, MUTED); self.box(x0 + sidebar + 8 * mm, y0 + ph - 34 * mm, 67 * mm, 22 * mm, fill=colors.HexColor("#201F1C")); self.label(x0 + sidebar + 13 * mm, y0 + ph - 20 * mm, "Listen with context.", 11, PAPER); self.box(x0 + sidebar + 8 * mm, y0 + 16 * mm, pw - sidebar - 16 * mm, 13 * mm, fill=colors.HexColor("#191816")); self.label(x0 + sidebar + 13 * mm, y0 + 23 * mm, "NOW PLAYING     Nothing playing", 7, MUTED)
        elif self.kind == "player":
            self.box(x0, y0 + 18 * mm, pw, ph - 18 * mm, fill=colors.HexColor("#191816")); self.box(x0 + 8 * mm, y0 + 29 * mm, 30 * mm, 30 * mm, fill=colors.HexColor("#24211C")); self.label(x0 + 12 * mm, y0 + 43 * mm, "ART", 8, MINT); self.label(x0 + 46 * mm, y0 + 55 * mm, "NOW PLAYING", 6.5, EMERALD); self.label(x0 + 46 * mm, y0 + 46 * mm, "A track with context", 10, PAPER); self.label(x0 + 46 * mm, y0 + 38 * mm, "Artist · Album", 7, MUTED); self.box(x0 + 102 * mm, y0 + 38 * mm, 18 * mm, 9 * mm, fill=colors.HexColor("#D8B36A"), stroke=colors.HexColor("#D8B36A")); self.label(x0 + 108 * mm, y0 + 41 * mm, "PLAY", 6.5, colors.HexColor("#201A10")); self.label(x0 + 8 * mm, y0 + 7 * mm, "MINI PLAYER → NOW PLAYING → QUEUE / DEVICE / REPEAT", 6.5, MINT)
        elif self.kind == "taste":
            for i, (name, val) in enumerate([("CONFIDENCE", "84%"), ("UPDATED", "Today"), ("SOURCES", "Spotify")]):
                xx = x0 + i * (pw / 3); self.box(xx, y0 + ph - 25 * mm, pw / 3 - 3 * mm, 20 * mm, fill=colors.HexColor("#191816")); self.label(xx + 4 * mm, y0 + ph - 13 * mm, name, 6.5, MUTED); self.label(xx + 4 * mm, y0 + ph - 21 * mm, val, 12, PAPER)
            self.box(x0, y0, pw * .62, ph - 32 * mm, fill=colors.HexColor("#191816")); self.label(x0 + 5 * mm, y0 + ph - 42 * mm, "A profile shaped by your listening.", 11, PAPER); c.setStrokeColor(EMERALD); c.setLineWidth(1.2); pts=[(x0+8*mm,y0+10*mm),(x0+25*mm,y0+20*mm),(x0+43*mm,y0+14*mm),(x0+62*mm,y0+30*mm),(x0+82*mm,y0+22*mm),(x0+100*mm,y0+36*mm)]; c.line(*pts[0],*pts[1]); [c.line(*a,*b) for a,b in zip(pts,pts[1:])]; self.box(x0 + pw * .67, y0, pw * .33, ph - 32 * mm, fill=colors.HexColor("#191816")); self.label(x0 + pw * .67 + 5 * mm, y0 + ph - 42 * mm, "HOW IT IS CALCULATED", 6.5, MINT); self.label(x0 + pw * .67 + 5 * mm, y0 + ph - 53 * mm, "Sources · freshness · notes", 7, MUTED)
        elif self.kind == "playlist":
            self.box(x0, y0 + ph - 23 * mm, pw, 18 * mm, fill=colors.HexColor("#201F1C")); self.label(x0 + 5 * mm, y0 + ph - 14 * mm, "03 SING & SHOUT", 12, PAPER); self.label(x0 + 5 * mm, y0 + ph - 20 * mm, "4h 12m · 67 tracks     PLAY     ANALYZE", 6.5, MINT); cols=["TRACK","ARTIST","ALBUM","DURATION"]; [self.label(x0 + j*38*mm, y0 + ph - 34*mm, v, 6.5, MINT) for j,v in enumerate(cols)]; [self.box(x0, y0 + ph - (43+i*9)*mm, pw, 7*mm, fill=colors.HexColor("#191816")) for i in range(4)]; [self.label(x0 + 4*mm, y0 + ph - (39+i*9)*mm, f"Track {i+1}     Artist / Album", 7, PAPER) for i in range(4)]
        elif self.kind == "discover":
            for i, name in enumerate(["SAFE PICKS", "EXPLORE", "WILDCARD"]):
                xx=x0+i*(pw/3); self.box(xx, y0, pw/3-3*mm, ph, fill=colors.HexColor("#191816")); self.label(xx+4*mm, y0+ph-11*mm, name, 7, MINT); self.box(xx+4*mm,y0+ph-39*mm,pw/3-11*mm,21*mm,fill=colors.HexColor("#24211C")); self.label(xx+7*mm,y0+ph-30*mm,"Album / artist",8,PAPER); self.label(xx+4*mm,y0+15*mm,"Why this belongs here",6.5,MUTED); self.label(xx+4*mm,y0+7*mm,"PLAY   SAVE",6.5,EMERALD)
        elif self.kind == "responsive":
            self.box(x0, y0, 95*mm, ph, fill=colors.HexColor("#191816")); self.label(x0+5*mm,y0+ph-9*mm,"DESKTOP",7,MINT); c.setStrokeColor(LINE); c.line(x0+35*mm,y0+8*mm,x0+35*mm,y0+ph-15*mm); self.label(x0+5*mm,y0+ph-25*mm,"sidebar",7,MUTED); self.label(x0+42*mm,y0+ph-25*mm,"workspace",7,PAPER); self.box(x0+112*mm,y0+3*mm,38*mm,ph-6*mm,fill=colors.HexColor("#191816")); self.label(x0+120*mm,y0+ph-13*mm,"MOBILE",7,MINT); self.label(x0+116*mm,y0+ph-27*mm,"header",6.5,MUTED); self.label(x0+116*mm,y0+20*mm,"player",6.5,MUTED); self.label(x0+116*mm,y0+11*mm,"bottom nav",6.5,PAPER)
        else:
            self.box(x0, y0, pw, ph, fill=colors.HexColor("#191816")); self.label(x0+6*mm,y0+ph-12*mm,"SYSTEM PLATE",9,PAPER); self.label(x0+6*mm,y0+ph-23*mm,"Context, hierarchy, decision, action",9,MUTED); [c.line(x0+6*mm,y0+(14+i*9)*mm,x0+pw-6*mm,y0+(14+i*9)*mm) for i in range(3)]
        c.restoreState()


class BrandDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kw):
        super().__init__(filename, **kw)
        frame = Frame(18 * mm, 18 * mm, A4[0] - 36 * mm, A4[1] - 38 * mm, id="normal")
        self.addPageTemplates([PageTemplate(id="brand", frames=frame, onPage=self.decorate)])
    def decorate(self, canvas, doc):
        canvas.saveState(); w, h = A4
        canvas.setFillColor(INK); canvas.rect(0, 0, w, h, fill=1, stroke=0)
        canvas.setStrokeColor(LINE); canvas.setLineWidth(.5); canvas.line(18 * mm, 13 * mm, w - 18 * mm, 13 * mm)
        canvas.setFillColor(MUTED); canvas.setFont("Helvetica", 7.5)
        canvas.drawString(18 * mm, 8 * mm, f"RESONANT  /  BRAND BOOK {VERSION}")
        canvas.drawRightString(w - 18 * mm, 8 * mm, f"{doc.page:02d}")
        canvas.restoreState()


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverKicker", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=EMERALD, tracking=1.8, alignment=TA_CENTER, spaceAfter=14))
styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=39, leading=42, textColor=PAPER, alignment=TA_CENTER, spaceAfter=14))
styles.add(ParagraphStyle(name="CoverSub", parent=styles["Normal"], fontSize=13, leading=18, textColor=MUTED, alignment=TA_CENTER))
styles.add(ParagraphStyle(name="H1Brand", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=24, leading=28, textColor=PAPER, spaceBefore=8, spaceAfter=9, keepWithNext=True))
styles.add(ParagraphStyle(name="H2Brand", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=MINT, spaceBefore=10, spaceAfter=5, keepWithNext=True))
styles.add(ParagraphStyle(name="H3Brand", parent=styles["Heading3"], fontName="Helvetica-Bold", fontSize=11.5, leading=15, textColor=PAPER, spaceBefore=8, spaceAfter=4, keepWithNext=True))
styles.add(ParagraphStyle(name="BodyBrand", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.4, leading=13.3, textColor=PAPER, spaceAfter=6))
styles.add(ParagraphStyle(name="SmallBrand", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.2, leading=11, textColor=MUTED, spaceAfter=4))
styles.add(ParagraphStyle(name="BulletBrand", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.2, leading=12.5, leftIndent=12, firstLineIndent=-7, bulletIndent=0, textColor=PAPER, spaceAfter=3))
styles.add(ParagraphStyle(name="CodeBrand", parent=styles["Code"], fontName="Courier", fontSize=8.1, leading=10.5, textColor=MINT, backColor=SURFACE, borderPadding=7, spaceBefore=4, spaceAfter=7))
styles.add(ParagraphStyle(name="TOCBrand", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=15, textColor=PAPER, leftIndent=5, spaceAfter=2))
styles.add(ParagraphStyle(name="QuoteBrand", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=16, leading=21, textColor=MINT, leftIndent=9, borderColor=EMERALD, borderWidth=1.2, borderPadding=8, spaceBefore=5, spaceAfter=12))
styles.add(ParagraphStyle(name="SystemLabel", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=7.5, leading=10, textColor=EMERALD, spaceAfter=4, keepWithNext=True))


def inline(text):
    text = escape(text)
    text = re.sub(r"&lt;([^&]+)&gt;", r"&lt;\1&gt;", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r"<font name='Courier' color='#67F3C2'>\1</font>", text)
    text = re.sub(r"\[([^]]+)\]\(([^)]+)\)", r"<font color='#67F3C2'>\1</font>", text)
    return text


def table_flow(rows):
    clean = [[Paragraph(inline(cell.strip()), styles["SmallBrand"]) for cell in row] for row in rows]
    widths = [None] * max(len(r) for r in rows)
    t = Table(clean, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table_styles = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#22312B")),
        ("TEXTCOLOR", (0, 0), (-1, 0), MINT),
        ("BACKGROUND", (0, 1), (-1, -1), SURFACE),
        ("GRID", (0, 0), (-1, -1), .35, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    for row in range(2, len(rows), 2):
        table_styles.append(("BACKGROUND", (0, row), (-1, row), colors.HexColor("#1D2622")))
    t.setStyle(TableStyle(table_styles))
    return t


def parse_md(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    story, paragraph, bullets, table, code, code_lines = [], [], [], [], False, []
    def flush_para():
        nonlocal paragraph
        if paragraph:
            story.append(Paragraph(inline(" ".join(paragraph)), styles["BodyBrand"])); paragraph = []
    def flush_bullets():
        nonlocal bullets
        for item in bullets: story.append(Paragraph(inline(item), styles["BulletBrand"], bulletText="•"))
        bullets = []
    def flush_table():
        nonlocal table
        if table: story.append(table_flow(table)); story.append(Spacer(1, 4)); table = []
    for line in lines:
        if line.startswith("```"):
            flush_para(); flush_bullets(); flush_table()
            if code:
                story.append(Preformatted("\n".join(code_lines), styles["CodeBrand"])); code_lines.clear()
            else:
                story.append(Spacer(1, 3))
            code = not code
            continue
        if code:
            code_lines.append(line)
            continue
        if line.startswith("#"):
            flush_para(); flush_bullets(); flush_table()
            level = len(line) - len(line.lstrip("#")); title = line[level:].strip()
            if level == 1 and title == "Resonant Design System":
                story.append(Paragraph(inline(title), styles["SystemLabel"]))
            else:
                style = styles["H1Brand"] if level <= 2 else styles["H2Brand"] if level == 3 else styles["H3Brand"]
                story.append(Paragraph(inline(title), style))
                if level == 2: story.append(AccentRule(25 * mm))
        elif line.startswith(">"):
            flush_para(); flush_bullets(); flush_table()
            story.append(Paragraph(inline(line[1:].strip()), styles["QuoteBrand"]))
        elif line.startswith("|"):
            flush_para(); flush_bullets()
            cells = [c for c in line.strip().strip("|").split("|")]
            if all(set(c.strip()) <= {"-", ":", " "} for c in cells): continue
            table.append(cells)
        elif re.match(r"^\s*[-*] ", line):
            flush_para(); flush_table(); bullets.append(re.sub(r"^\s*[-*] ", "", line))
        elif not line.strip():
            flush_para(); flush_bullets(); flush_table()
        else:
            flush_bullets(); flush_table(); paragraph.append(line.strip())
    flush_para(); flush_bullets(); flush_table(); return story


def visual_for(path):
    name = path.name
    plates = {
        "05-BRAND_IDENTITY.md": ("shell", "Brand in product", "A personal control center for music"),
        "06-LOGO_SYSTEM.md": None,
        "07-COLOR_SYSTEM.md": ("palette", "Warm nocturnal palette", "Canvas, ink, muted, line, accent"),
        "09-LAYOUT_GRID.md": ("responsive", "One system, two contexts", "Desktop sidebar becomes mobile navigation"),
        "10-COMPONENT_SYSTEM.md": ("shell", "Quiet structure", "Shared shell, surfaces, states, and focus"),
        "11-MUSIC_PLAYER.md": ("player", "Keep the listening thread", "Persistent player context across product areas"),
        "12-AI_SYSTEM.md": ("discover", "AI at the point of need", "Reviewable help, never a dominant chatbot"),
        "13-ANALYTICS_SYSTEM.md": ("taste", "Taste as an estimate", "Confidence, freshness, sources, and methodology"),
        "14-DISCOVERY_SYSTEM.md": ("discover", "Discovery with a reason", "Safe picks · Explore · Wildcard"),
        "15-LIBRARY_SYSTEM.md": ("playlist", "Music as a personal archive", "Artwork, collection, and context"),
        "16-SEARCH_SYSTEM.md": ("shell", "One search, four result types", "Songs · artists · albums · playlists"),
        "20-WEBSITE.md": None,
        "21-MOCKUPS.md": None,
        "31-ACCOUNT_CONNECTIONS.md": ("shell", "Identity and provider stay separate", "Google account · Spotify connection"),
        "32-PLAYLIST_WORKFLOWS.md": ("playlist", "Review before change", "Keep · Remove · Unsure"),
        "33-TASTE_PROFILE.md": ("taste", "Make methodology humane", "Observed patterns plus explicit correction"),
    }
    if name == "06-LOGO_SYSTEM.md":
        return None
    if name == "21-MOCKUPS.md":
        return ImagePlate(APPLICATION_BOARD, "Logo application board", "Concept applications using the approved symbol; UI imagery is illustrative", max_height=122 * mm)
    item = plates.get(name)
    return VisualPlate(*item) if item else None


def build():
    doc = BrandDocTemplate(str(OUT), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=20 * mm, bottomMargin=18 * mm, title=f"Resonant Brand Book {VERSION}", author="Resonant")
    story = [Spacer(1, 16 * mm), LogoCover(), Spacer(1, 8 * mm), Paragraph("RESONANT DESIGN SYSTEM", styles["CoverKicker"]), Paragraph("Brand Book", styles["CoverTitle"]), AccentRule(45 * mm), Spacer(1, 8 * mm), Paragraph(f"Version {VERSION[1:]}", styles["CoverSub"]), Paragraph("A visual system for listening with context", styles["CoverSub"]), Spacer(1, 28 * mm), Paragraph("Your music, with context.", styles["CoverSub"]), PageBreak()]
    story += [Paragraph("Contents", styles["H1Brand"]), AccentRule()]
    for i, path in enumerate(DOCS, 1):
        label = "README" if path.name == "README.md" else path.stem.replace("_", " ").replace("-", " ").title()
        story.append(Paragraph(f"{i:02d}  {inline(label)}", styles["TOCBrand"]))
    story += [PageBreak(), Paragraph("How to read this guide", styles["H1Brand"]), AccentRule(), Paragraph(f"This PDF contains the complete Markdown source of the {VERSION} brand and product guide. Current behaviour is grounded in the verified stephanteig/resonant product repository. The approved logo vectors and PNG variants are included as visual assets; concept imagery is not a product screenshot.", styles["BodyBrand"]), PageBreak()]
    story.extend([EditorialImagePage(HERO_IMAGE, "Opening signal", ["LISTEN", "WITH CONTEXT."], f"Resonant / Brand Book {VERSION}"), PageBreak(), StatementPage("The governing idea", ["Music", "comes first."]), PageBreak(), TypographySpread(), PageBreak(), ColorSpacingSpread(), PageBreak()])
    chapter_openers = {
        "00-START-HERE.md": ChapterOpener(1, "Foundation", ["Music", "comes first."], "The principles that keep Resonant useful, quiet, and human.", HERO_IMAGE),
        "05-BRAND_IDENTITY.md": ChapterOpener(2, "Brand", ["Calm", "complexity."], "A personal system for making listening easier to understand."),
        "06-LOGO_SYSTEM.md": ChapterOpener(3, "Identity", ["A signal", "for listening."], "The mark, its space, and its applications.", accent=MINT),
        "10-COMPONENT_SYSTEM.md": ChapterOpener(4, "Product", ["Quiet", "structure."], "Components should support the listening thread, not compete with it."),
        "12-AI_SYSTEM.md": ChapterOpener(5, "Intelligence", ["Explain", "the assist."], "AI helps at the point of need and keeps the person in control."),
        "24-MOTION.md": ChapterOpener(6, "Behaviour", ["Keep", "the thread."], "Motion explains change without adding noise."),
        "28-DESKTOP.md": ChapterOpener(7, "Platform", ["One system,", "two contexts."], "The same principles adapt across desktop and smaller surfaces."),
        "PROJECT_STATUS.md": ChapterOpener(8, "Release", ["Make it", "repeatable."], "The open work that turns a system into a maintained practice.", accent=LIME),
    }
    editorial_pages = {
        "07-COLOR_SYSTEM.md": ColorFieldPage(),
        "08-TYPOGRAPHY.md": TypographySpecimenPage(),
        "18-ACCESSIBILITY.md": AccessibilityPage(),
        "20-WEBSITE.md": WebsiteStoryPage(),
        "21-MOCKUPS.md": MockupGalleryPage(),
        "24-MOTION.md": MotionTimelinePage(),
    }
    for index, path in enumerate(DOCS):
        if path.name in chapter_openers:
            story.extend([chapter_openers[path.name], PageBreak()])
        visual = visual_for(path)
        if visual:
            story.extend([visual, Spacer(1, 7 * mm)])
        story.extend(parse_md(path))
        if path.name == "06-LOGO_SYSTEM.md":
            story.extend([
                PageBreak(), LogoHeroPage(), PageBreak(), LogoDetailPage(),
                PageBreak(), LogoClearSpacePage(), PageBreak(), LogoSizePage(),
                PageBreak(), LogoVariantPage(), PageBreak(), LogoMisusePlate(),
            ])
        if path.name in editorial_pages:
            story.extend([PageBreak(), editorial_pages[path.name]])
        if index < len(DOCS) - 1: story.append(PageBreak())
    doc.build(story)
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__": build()
