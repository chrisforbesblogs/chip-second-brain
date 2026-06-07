from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent


def font(size, bold=False):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for path in paths:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()


F = {
    "xs": font(12),
    "sm": font(14),
    "base": font(16),
    "md": font(18),
    "lg": font(23, True),
    "xl": font(34, True),
    "bold": font(16, True),
    "small_bold": font(13, True),
}


PALETTES = [
    {
        "slug": "01-garmin-clean",
        "name": "Garmin Clean",
        "why": "Crisp, health-first, familiar for wearable users.",
        "bg": "#eef2ed",
        "card": "#ffffff",
        "ink": "#17201a",
        "muted": "#667066",
        "primary": "#1f9d5a",
        "secondary": "#2d6cdf",
        "accent": "#dd7b2a",
        "danger": "#d84d45",
        "line": "#dce3db",
    },
    {
        "slug": "02-performance-dark",
        "name": "Performance Dark",
        "why": "Premium, athlete-led, strong for pro/performance mode.",
        "bg": "#090d10",
        "card": "#151b20",
        "ink": "#f5f7f6",
        "muted": "#9aa7a2",
        "primary": "#4be38b",
        "secondary": "#6aa8ff",
        "accent": "#f6b44b",
        "danger": "#ff6b63",
        "line": "#293139",
    },
    {
        "slug": "03-warm-lifestyle",
        "name": "Warm Lifestyle",
        "why": "Softer, approachable, less intimidating for everyday health.",
        "bg": "#f4f1eb",
        "card": "#fffaf2",
        "ink": "#251e18",
        "muted": "#756b61",
        "primary": "#2f8f6b",
        "secondary": "#4c74a8",
        "accent": "#d97942",
        "danger": "#c64e4e",
        "line": "#e4dcd0",
    },
    {
        "slug": "04-sport-electric",
        "name": "Sport Electric",
        "why": "More energetic and app-store punchy, good for training identity.",
        "bg": "#f3f6fb",
        "card": "#ffffff",
        "ink": "#111827",
        "muted": "#667085",
        "primary": "#00a676",
        "secondary": "#306bff",
        "accent": "#ff8a00",
        "danger": "#ee4266",
        "line": "#d9e1ef",
    },
    {
        "slug": "05-whoop-inspired-performance",
        "name": "WHOOP-Inspired Performance",
        "why": "Dark, serious, recovery-led, and built around daily body signals.",
        "bg": "#050608",
        "card": "#111417",
        "ink": "#f6f8f2",
        "muted": "#8b958f",
        "primary": "#c7ff3d",
        "secondary": "#45d483",
        "accent": "#ffb340",
        "danger": "#ff5f5a",
        "line": "#252a2f",
        "layout": "performance",
    },
]


def rr(draw, box, radius=22, fill="#ffffff", outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, value, palette, font_key="base", fill=None, anchor=None):
    draw.text(xy, value, fill=fill or palette["ink"], font=F[font_key], anchor=anchor)


def progress(draw, x, y, w, pct, palette, color):
    rr(draw, (x, y, x + w, y + 8), radius=4, fill=palette["line"])
    rr(draw, (x, y, x + int(w * pct), y + 8), radius=4, fill=color)


def ring(draw, cx, cy, radius, pct, palette, color, width=13):
    box = (cx - radius, cy - radius, cx + radius, cy + radius)
    draw.arc(box, start=0, end=360, fill=palette["line"], width=width)
    draw.arc(box, start=-90, end=-90 + int(360 * pct), fill=color, width=width)


def draw_performance_option(palette):
    im = Image.new("RGB", (900, 1100), palette["bg"])
    d = ImageDraw.Draw(im)

    text(d, (48, 58), palette["name"], palette, "xl")
    text(d, (50, 94), palette["why"], palette, "sm", palette["muted"])
    text(d, (50, 122), "Reference direction: WHOOP-like intensity, not a copy.", palette, "xs", palette["muted"])

    swatches = [
        ("Recovery", palette["primary"]),
        ("Body", palette["secondary"]),
        ("Load", palette["accent"]),
        ("Alert", palette["danger"]),
        ("Surface", palette["card"]),
    ]
    x = 50
    for label, color in swatches:
        rr(d, (x, 158, x + 118, 218), radius=10, fill=color, outline=palette["line"])
        text(d, (x, 240), label, palette, "xs", palette["muted"])
        text(d, (x, 259), color.upper(), palette, "xs", palette["muted"])
        x += 154

    phone_x, phone_y = 250, 300
    rr(d, (phone_x, phone_y, phone_x + 390, phone_y + 760), radius=42, fill="#010203", outline="#010203")
    rr(d, (phone_x + 12, phone_y + 12, phone_x + 378, phone_y + 748), radius=34, fill=palette["bg"], outline=palette["bg"])

    x0, y0 = phone_x + 34, phone_y + 42
    text(d, (x0, y0), "Life App", palette, "bold")
    rr(d, (phone_x + 320, y0 - 13, phone_x + 356, y0 + 23), radius=6, fill=palette["card"], outline=palette["line"])
    text(d, (phone_x + 338, y0 + 5), "P", palette, "small_bold", palette["primary"], "mm")

    text(d, (x0, y0 + 58), "Today", palette, "xl")
    text(d, (x0, y0 + 94), "Garmin synced 12 min ago", palette, "xs", palette["muted"])

    rr(d, (x0 - 8, y0 + 128, x0 + 326, y0 + 352), radius=14, fill=palette["card"], outline=palette["line"])
    text(d, (x0 + 18, y0 + 160), "RECOVERY", palette, "small_bold", palette["muted"])
    ring(d, x0 + 98, y0 + 258, 64, 0.82, palette, palette["primary"], 14)
    text(d, (x0 + 98, y0 + 250), "82", palette, "xl", palette["primary"], "mm")
    text(d, (x0 + 98, y0 + 282), "%", palette, "sm", palette["muted"], "mm")
    text(d, (x0 + 190, y0 + 218), "Green", palette, "lg", palette["ink"])
    text(d, (x0 + 190, y0 + 248), "Body is ready", palette, "sm", palette["muted"])
    rr(d, (x0 + 190, y0 + 282, x0 + 306, y0 + 314), radius=7, fill=palette["primary"])
    text(d, (x0 + 248, y0 + 300), "TRAIN OK", palette, "xs", "#050608", "mm")

    metrics = [
        ("LOAD", "12.4", palette["accent"], 0.62),
        ("SLEEP", "91%", palette["primary"], 0.91),
        ("HRV", "64ms", palette["secondary"], 0.74),
    ]
    mx = x0 - 8
    yy = y0 + 374
    for label, value, color, pct in metrics:
        rr(d, (mx, yy, mx + 102, yy + 130), radius=12, fill=palette["card"], outline=palette["line"])
        text(d, (mx + 14, yy + 28), label, palette, "xs", palette["muted"])
        ring(d, mx + 51, yy + 72, 28, pct, palette, color, 7)
        text(d, (mx + 51, yy + 76), value, palette, "small_bold", color, "mm")
        mx += 116

    rr(d, (x0 - 8, y0 + 526, x0 + 326, y0 + 612), radius=12, fill=palette["card"], outline=palette["line"])
    text(d, (x0 + 18, y0 + 556), "RECOMMENDED", palette, "xs", palette["muted"])
    text(d, (x0 + 18, y0 + 586), "Zone 2 run only", palette, "lg", palette["primary"])
    text(d, (x0 + 258, y0 + 556), "35 min", palette, "xs", palette["muted"])

    rr(d, (x0 - 10, phone_y + 690, x0 + 328, phone_y + 744), radius=14, fill="#080a0c", outline=palette["line"])
    nav = [("TODAY", palette["primary"]), ("CAL", palette["muted"]), ("TRAIN", palette["muted"]), ("FOOD", palette["muted"]), ("HABITS", palette["muted"])]
    nx = x0 + 28
    for label, color in nav:
        text(d, (nx, phone_y + 722), label, palette, "xs", color, "mm")
        nx += 72

    im.save(OUT / f"{palette['slug']}.png")


def draw_option(palette):
    if palette.get("layout") == "performance":
        draw_performance_option(palette)
        return

    im = Image.new("RGB", (900, 1100), palette["bg"])
    d = ImageDraw.Draw(im)

    text(d, (48, 58), palette["name"], palette, "xl")
    text(d, (50, 94), palette["why"], palette, "sm", palette["muted"])

    swatches = [
        ("Primary", palette["primary"]),
        ("Secondary", palette["secondary"]),
        ("Accent", palette["accent"]),
        ("Danger", palette["danger"]),
        ("Ink", palette["ink"]),
    ]
    x = 50
    for label, color in swatches:
        rr(d, (x, 124, x + 118, 184), radius=18, fill=color, outline=palette["line"])
        text(d, (x, 205), label, palette, "xs", palette["muted"])
        text(d, (x, 224), color.upper(), palette, "xs", palette["muted"])
        x += 154

    phone_x, phone_y = 250, 280
    rr(d, (phone_x, phone_y, phone_x + 390, phone_y + 760), radius=42, fill=palette["ink"], outline=palette["ink"])
    rr(d, (phone_x + 12, phone_y + 12, phone_x + 378, phone_y + 748), radius=34, fill=palette["bg"], outline=palette["bg"])

    x0, y0 = phone_x + 32, phone_y + 42
    text(d, (x0, y0), "Life App", palette, "bold")
    rr(d, (phone_x + 318, y0 - 14, phone_x + 356, y0 + 24), radius=19, fill=palette["primary"])
    text(d, (phone_x + 337, y0 + 5), "P", palette, "bold", "#ffffff", "mm")

    text(d, (x0, y0 + 72), "Today", palette, "xl")
    text(d, (x0, y0 + 108), "Garmin synced 12 min ago", palette, "sm", palette["muted"])

    rr(d, (x0 - 8, y0 + 140, x0 + 326, y0 + 288), radius=28, fill=palette["card"], outline=palette["line"])
    text(d, (x0 + 16, y0 + 172), "Readiness", palette, "small_bold")
    text(d, (x0 + 16, y0 + 194), "Ready to train", palette, "xs", palette["muted"])
    text(d, (x0 + 22, y0 + 248), "82", palette, "xl", palette["primary"])
    text(d, (x0 + 85, y0 + 257), "/100", palette, "md", palette["muted"])
    text(d, (x0 + 258, y0 + 184), "Good", palette, "bold", palette["primary"])
    progress(d, x0 + 16, y0 + 270, 282, 0.82, palette, palette["primary"])

    rr(d, (x0 - 8, y0 + 310, x0 + 326, y0 + 480), radius=24, fill=palette["card"], outline=palette["line"])
    text(d, (x0 + 16, y0 + 342), "Key signals", palette, "small_bold")
    rows = [
        ("Sleep", "7h 42m", "Good", palette["primary"], 0.78),
        ("Recovery", "78%", "Improving", palette["secondary"], 0.78),
        ("Training", "Moderate", "Productive", palette["accent"], 0.56),
    ]
    yy = y0 + 378
    for name, value, state, color, pct in rows:
        text(d, (x0 + 16, yy), name, palette, "sm")
        text(d, (x0 + 122, yy), value, palette, "sm")
        text(d, (x0 + 228, yy), state, palette, "xs", color)
        progress(d, x0 + 16, yy + 24, 282, pct, palette, color)
        yy += 36

    rr(d, (x0 - 8, y0 + 500, x0 + 326, y0 + 638), radius=24, fill=palette["card"], outline=palette["line"])
    text(d, (x0 + 16, y0 + 532), "Today's actions", palette, "small_bold")
    actions = [("Zone 2 run", palette["primary"]), ("Protein target", palette["secondary"])]
    yy = y0 + 564
    for name, color in actions:
        rr(d, (x0 + 16, yy, x0 + 298, yy + 30), radius=15, fill=palette["bg"], outline=palette["line"])
        d.ellipse((x0 + 30, yy + 9, x0 + 42, yy + 21), fill=color)
        text(d, (x0 + 54, yy + 20), name, palette, "sm")
        yy += 38

    rr(d, (x0 - 10, phone_y + 690, x0 + 328, phone_y + 744), radius=26, fill=palette["card"], outline=palette["line"])
    nav = [("Today", palette["primary"]), ("Cal", palette["muted"]), ("Train", palette["muted"]), ("Food", palette["muted"]), ("Habits", palette["muted"])]
    nx = x0 + 28
    for label, color in nav:
        text(d, (nx, phone_y + 722), label, palette, "xs", color, "mm")
        nx += 72

    im.save(OUT / f"{palette['slug']}.png")


def write_readme():
    lines = [
        "# Life App Color Scheme Options",
        "",
        "Date: 2026-06-07",
        "Status: visual exploration",
        "",
        "The first four options use the same Today-screen structure so the team can compare palette, contrast and brand feel.",
        "The WHOOP-inspired option also changes layout and component style to test a more distinct performance identity.",
        "",
    ]
    for p in PALETTES:
        lines.extend([
            f"## {p['name']}",
            "",
            f"File: `{p['slug']}.png`",
            "",
            f"Why: {p['why']}",
            "",
            "Palette:",
            "",
            f"- Background: `{p['bg']}`",
            f"- Card: `{p['card']}`",
            f"- Ink: `{p['ink']}`",
            f"- Muted: `{p['muted']}`",
            f"- Primary: `{p['primary']}`",
            f"- Secondary: `{p['secondary']}`",
            f"- Accent: `{p['accent']}`",
            f"- Danger: `{p['danger']}`",
            "",
        ])
    lines.extend([
        "## Initial Recommendation",
        "",
        "Current preference: WHOOP-Inspired Performance.",
        "Use it as the leading visual direction if the product should feel serious, athlete-led, and recovery-first.",
        "Keep Garmin Clean as the safer mainstream fallback if the dark performance direction feels too intense.",
        "",
    ])
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    for palette in PALETTES:
        draw_option(palette)
    write_readme()
