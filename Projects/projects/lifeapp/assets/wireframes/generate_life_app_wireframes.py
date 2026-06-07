from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import html

OUT = Path(__file__).resolve().parent


def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
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
    "lg": font(24, True),
    "xl": font(34, True),
    "bold": font(16, True),
    "small_bold": font(13, True),
}

INK = "#17201a"
MUTED = "#667066"
BG = "#eef2ed"
CARD = "#ffffff"
LINE = "#dce3db"
GREEN = "#1f9d5a"
BLUE = "#2d6cdf"
ORANGE = "#dd7b2a"
RED = "#d84d45"

WHOOP = {
    "bg": "#050608",
    "card": "#111417",
    "card2": "#080a0c",
    "ink": "#f6f8f2",
    "muted": "#8b958f",
    "line": "#252a2f",
    "primary": "#c7ff3d",
    "secondary": "#45d483",
    "accent": "#ffb340",
    "danger": "#ff5f5a",
}


def rr(draw, box, radius=22, fill=CARD, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, value, fill=INK, font_key="base", anchor=None):
    draw.text(xy, value, fill=fill, font=F[font_key], anchor=anchor)


def top_bar(draw, title):
    text(draw, (28, 28), title, font_key="bold")
    rr(draw, (336, 20, 374, 58), radius=19, fill="#d8f2e5")
    text(draw, (355, 38), "P", fill=GREEN, font_key="bold", anchor="mm")


def nav(draw, active):
    y = 790
    rr(draw, (16, 772, 374, 832), radius=28, fill="#ffffff", outline=LINE)
    items = [("Today", 52), ("Cal", 122), ("Train", 195), ("Food", 268), ("Habits", 335)]
    for label, x in items:
        fill = GREEN if label == active else MUTED
        if label == active:
            rr(draw, (x - 28, y - 9, x + 28, y + 23), radius=16, fill="#e4f7ed")
        text(draw, (x, y + 7), label, fill=fill, font_key="xs", anchor="mm")


def card_title(draw, x, y, title, subtitle=None):
    text(draw, (x, y), title, font_key="small_bold")
    if subtitle:
        text(draw, (x, y + 20), subtitle, fill=MUTED, font_key="xs")


def progress(draw, x, y, w, pct, color):
    rr(draw, (x, y, x + w, y + 8), radius=4, fill="#eef2ee")
    rr(draw, (x, y, x + int(w * pct), y + 8), radius=4, fill=color)


def phone_canvas():
    return Image.new("RGB", (390, 844), BG)


def draw_today(path):
    im = phone_canvas()
    d = ImageDraw.Draw(im)
    top_bar(d, "Life App")
    text(d, (28, 78), "Today", font_key="xl")
    text(d, (28, 116), "Garmin synced 12 min ago", fill=MUTED, font_key="sm")

    rr(d, (20, 148, 370, 310), radius=28)
    card_title(d, 44, 172, "Readiness", "Ready to train")
    text(d, (52, 244), "82", fill=GREEN, font_key="xl")
    text(d, (113, 254), "/100", fill=MUTED, font_key="md")
    progress(d, 44, 278, 282, 0.82, GREEN)
    text(d, (284, 182), "Good", fill=GREEN, font_key="bold")

    rr(d, (20, 326, 370, 500), radius=24)
    card_title(d, 44, 350, "Key signals")
    rows = [
        ("Sleep", "7h 42m", "Good", GREEN, 0.78),
        ("Recovery", "78%", "Improving", BLUE, 0.78),
        ("Training", "Moderate", "Productive", ORANGE, 0.56),
        ("Nutrition", "64%", "Needs protein", RED, 0.64),
    ]
    y = 386
    for name, value, state, color, pct in rows:
        text(d, (44, y), name, font_key="sm")
        text(d, (150, y), value, font_key="sm")
        text(d, (262, y), state, fill=color, font_key="xs")
        progress(d, 44, y + 24, 282, pct, color)
        y += 36

    rr(d, (20, 516, 370, 746), radius=24)
    card_title(d, 44, 540, "Today's actions", "Built from Garmin, food and habits")
    actions = [
        ("Zone 2 run", "35 min easy pace", GREEN),
        ("Protein target", "Hit 150g by dinner", BLUE),
        ("Sleep plan", "Lights out before 11:00", ORANGE),
        ("Steps", "8k target", GREEN),
    ]
    y = 584
    for title, sub, color in actions:
        rr(d, (44, y, 326, y + 31), radius=15, fill="#f5f8f5")
        d.ellipse((58, y + 9, 70, y + 21), fill=color)
        text(d, (82, y + 7), title, font_key="sm")
        text(d, (204, y + 8), sub, fill=MUTED, font_key="xs")
        y += 39
    nav(d, "Today")
    im.save(path)


def draw_training(path):
    im = phone_canvas()
    d = ImageDraw.Draw(im)
    top_bar(d, "Training")
    text(d, (28, 78), "Training", font_key="xl")

    rr(d, (24, 124, 366, 166), radius=21, fill="#ffffff", outline=LINE)
    rr(d, (30, 130, 190, 160), radius=15, fill="#e4f7ed")
    text(d, (110, 145), "Today", fill=GREEN, font_key="sm", anchor="mm")
    text(d, (275, 145), "Workouts", fill=MUTED, font_key="sm", anchor="mm")

    rr(d, (20, 190, 370, 370), radius=28)
    card_title(d, 44, 214, "Recommended workout", "Based on recovery and training load")
    text(d, (44, 274), "Zone 2 Run", font_key="lg")
    text(d, (44, 308), "35 min - easy pace - low fatigue", fill=MUTED, font_key="sm")
    rr(d, (44, 330, 146, 354), radius=12, fill="#e4f7ed")
    text(d, (95, 342), "Start plan", fill=GREEN, font_key="xs", anchor="mm")

    rr(d, (20, 388, 370, 560), radius=24)
    card_title(d, 44, 412, "Garmin signals")
    metrics = [("Load", "Moderate"), ("HRV", "Stable"), ("Recovery", "Good"), ("Last run", "5.2 km")]
    xys = [(44, 454), (198, 454), (44, 504), (198, 504)]
    for (label, value), (x, y) in zip(metrics, xys):
        rr(d, (x, y, x + 128, y + 40), radius=16, fill="#f5f8f5")
        text(d, (x + 12, y + 15), label, fill=MUTED, font_key="xs")
        text(d, (x + 118, y + 25), value, font_key="sm", anchor="ra")

    rr(d, (20, 578, 370, 746), radius=24)
    card_title(d, 44, 602, "Workout history")
    for i, (kind, detail) in enumerate([("Run", "Yesterday - 5.2 km"), ("Strength", "2 days ago - upper"), ("Ride", "4 days ago - 42 min")]):
        y = 640 + i * 34
        text(d, (44, y), kind, font_key="sm")
        text(d, (152, y), detail, fill=MUTED, font_key="xs")
    nav(d, "Train")
    im.save(path)


def whoop_text(draw, xy, value, font_key="base", fill=None, anchor=None):
    draw.text(xy, value, fill=fill or WHOOP["ink"], font=F[font_key], anchor=anchor)


def whoop_rr(draw, box, radius=14, fill=None, outline=None, width=1):
    draw.rounded_rectangle(
        box,
        radius=radius,
        fill=fill or WHOOP["card"],
        outline=outline or WHOOP["line"],
        width=width,
    )


def ring(draw, cx, cy, radius, pct, color, width=12):
    box = (cx - radius, cy - radius, cx + radius, cy + radius)
    draw.arc(box, start=0, end=360, fill=WHOOP["line"], width=width)
    draw.arc(box, start=-90, end=-90 + int(360 * pct), fill=color, width=width)


def whoop_top_bar(draw, title):
    whoop_text(draw, (28, 28), title, "bold")
    whoop_rr(draw, (336, 20, 374, 58), radius=6, fill=WHOOP["card"], outline=WHOOP["line"])
    whoop_text(draw, (355, 38), "P", "bold", WHOOP["primary"], "mm")


def whoop_nav(draw, active):
    y = 790
    whoop_rr(draw, (16, 772, 374, 832), radius=14, fill=WHOOP["card2"], outline=WHOOP["line"])
    items = [("Today", 52), ("Cal", 122), ("Train", 195), ("Food", 268), ("Habits", 335)]
    for label, x in items:
        fill = WHOOP["primary"] if label == active else WHOOP["muted"]
        whoop_text(draw, (x, y + 7), label.upper(), "xs", fill, "mm")


def draw_today_whoop(path):
    im = Image.new("RGB", (390, 844), WHOOP["bg"])
    d = ImageDraw.Draw(im)
    whoop_top_bar(d, "Life App")
    whoop_text(d, (28, 78), "Today", "xl")
    whoop_text(d, (28, 112), "Garmin synced 12 min ago", "xs", WHOOP["muted"])

    whoop_rr(d, (20, 144, 370, 362), radius=14)
    whoop_text(d, (44, 178), "RECOVERY", "small_bold", WHOOP["muted"])
    ring(d, 116, 262, 62, 0.82, WHOOP["primary"], 14)
    whoop_text(d, (116, 254), "82", "xl", WHOOP["primary"], "mm")
    whoop_text(d, (116, 288), "%", "sm", WHOOP["muted"], "mm")
    whoop_text(d, (220, 242), "Green", "lg")
    whoop_text(d, (220, 270), "Body is ready", "sm", WHOOP["muted"])
    whoop_rr(d, (220, 296, 332, 328), radius=7, fill=WHOOP["primary"], outline=WHOOP["primary"])
    whoop_text(d, (276, 314), "TRAIN OK", "xs", WHOOP["bg"], "mm")

    metrics = [
        ("LOAD", "12.4", WHOOP["accent"], 0.62),
        ("SLEEP", "91%", WHOOP["primary"], 0.91),
        ("HRV", "64ms", WHOOP["secondary"], 0.74),
    ]
    x = 20
    for label, value, color, pct in metrics:
        whoop_rr(d, (x, 382, x + 110, 514), radius=14)
        whoop_text(d, (x + 16, 416), label, "xs", WHOOP["muted"])
        ring(d, x + 55, 466, 28, pct, color, 7)
        whoop_text(d, (x + 55, 470), value, "small_bold", color, "mm")
        x += 120

    whoop_rr(d, (20, 536, 370, 632), radius=14)
    whoop_text(d, (44, 570), "RECOMMENDED", "xs", WHOOP["muted"])
    whoop_text(d, (44, 604), "Zone 2 run only", "lg", WHOOP["primary"])
    whoop_text(d, (302, 570), "35 min", "xs", WHOOP["muted"])

    whoop_rr(d, (20, 650, 370, 746), radius=14)
    whoop_text(d, (44, 682), "TODAY'S ACTIONS", "xs", WHOOP["muted"])
    actions = [("Protein target", WHOOP["secondary"]), ("Sleep before 11", WHOOP["accent"])]
    y = 708
    for title, color in actions:
        d.ellipse((44, y - 7, 56, y + 5), fill=color)
        whoop_text(d, (68, y), title, "sm")
        y += 22

    whoop_nav(d, "Today")
    im.save(path)


def draw_training_whoop(path):
    im = Image.new("RGB", (390, 844), WHOOP["bg"])
    d = ImageDraw.Draw(im)
    whoop_top_bar(d, "Training")
    whoop_text(d, (28, 78), "Training", "xl")

    whoop_rr(d, (24, 124, 366, 166), radius=12, fill=WHOOP["card2"])
    whoop_rr(d, (30, 130, 190, 160), radius=8, fill=WHOOP["primary"], outline=WHOOP["primary"])
    whoop_text(d, (110, 145), "TODAY", "xs", WHOOP["bg"], "mm")
    whoop_text(d, (275, 145), "WORKOUTS", "xs", WHOOP["muted"], "mm")

    whoop_rr(d, (20, 190, 370, 380), radius=14)
    whoop_text(d, (44, 224), "RECOMMENDED WORKOUT", "xs", WHOOP["muted"])
    whoop_text(d, (44, 276), "Zone 2 Run", "lg", WHOOP["primary"])
    whoop_text(d, (44, 306), "35 min - easy pace - low fatigue", "sm", WHOOP["muted"])
    ring(d, 300, 282, 42, 0.62, WHOOP["accent"], 10)
    whoop_text(d, (300, 286), "12.4", "small_bold", WHOOP["accent"], "mm")
    whoop_rr(d, (44, 330, 154, 356), radius=7, fill=WHOOP["primary"], outline=WHOOP["primary"])
    whoop_text(d, (99, 344), "START PLAN", "xs", WHOOP["bg"], "mm")

    whoop_rr(d, (20, 402, 370, 578), radius=14)
    whoop_text(d, (44, 434), "BODY SIGNALS", "xs", WHOOP["muted"])
    metrics = [
        ("LOAD", "Moderate", WHOOP["accent"]),
        ("HRV", "Stable", WHOOP["secondary"]),
        ("RECOVERY", "Good", WHOOP["primary"]),
        ("LAST RUN", "5.2 km", WHOOP["muted"]),
    ]
    xys = [(44, 468), (204, 468), (44, 522), (204, 522)]
    for (label, value, color), (x, y) in zip(metrics, xys):
        whoop_rr(d, (x, y, x + 126, y + 36), radius=10, fill=WHOOP["card2"])
        whoop_text(d, (x + 12, y + 14), label, "xs", WHOOP["muted"])
        whoop_text(d, (x + 116, y + 24), value, "xs", color, "ra")

    whoop_rr(d, (20, 598, 370, 746), radius=14)
    whoop_text(d, (44, 630), "WORKOUT HISTORY", "xs", WHOOP["muted"])
    history = [("RUN", "Yesterday - 5.2 km", WHOOP["primary"]), ("STRENGTH", "2 days ago - upper", WHOOP["secondary"]), ("RIDE", "4 days ago - 42 min", WHOOP["accent"])]
    for i, (kind, detail, color) in enumerate(history):
        y = 660 + i * 28
        d.ellipse((44, y - 8, 56, y + 4), fill=color)
        whoop_text(d, (70, y), kind, "sm")
        whoop_text(d, (160, y), detail, "xs", WHOOP["muted"])

    whoop_nav(d, "Train")
    im.save(path)


SCREENS = [
    ("Today", ["Readiness score", "Key Garmin signals", "Today's actions", "Garmin sync state"]),
    ("Calendar", ["Week strip", "Today plan", "Upcoming training", "Habit/nutrition markers"]),
    ("Training", ["Tabs: Today / Workouts", "Recommended workout", "Garmin load/HRV", "Workout history"]),
    ("Nutrition", ["Calories and macros", "Protein gap insight", "Quick add meal/snack", "Training fuel context"]),
    ("Habits", ["Daily checklist", "Streaks", "Garmin step goal", "Sleep routine"]),
    ("Profile", ["Profile top right", "Connected apps", "Goals", "Simple / Performance mode"]),
]


def svg_text(x, y, value, size=16, weight=400, fill=INK):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}">{html.escape(value)}</text>'


def svg_rect(x, y, w, h, r=18, fill="#fff", stroke=LINE):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>'


def make_svg_board(path):
    w, h = 1260, 1260
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        f'<rect width="{w}" height="{h}" fill="{BG}"/>',
        svg_text(48, 70, "Life App MVP Wireframes", 32, 700),
        svg_text(48, 104, "Working title. Garmin-compatible MVP. Profile lives top right, like Garmin Connect.", 16, 400, MUTED),
    ]
    x0, y0 = 48, 140
    phone_w, phone_h = 350, 500
    for idx, (title, bullets) in enumerate(SCREENS):
        col = idx % 3
        row = idx // 3
        x = x0 + col * 405
        y = y0 + row * 540
        parts.append(svg_rect(x, y, phone_w, phone_h, 34, "#101713", "#101713"))
        parts.append(svg_rect(x + 12, y + 12, phone_w - 24, phone_h - 24, 28, "#ffffff", "#ffffff"))
        parts.append(svg_text(x + 32, y + 52, title, 22, 700))
        parts.append(f'<circle cx="{x + phone_w - 44}" cy="{y + 44}" r="18" fill="#d8f2e5"/>')
        parts.append(svg_text(x + phone_w - 50, y + 50, "P", 16, 700, GREEN))
        yy = y + 88
        for bullet in bullets:
            parts.append(svg_rect(x + 32, yy, phone_w - 64, 52, 16, "#f5f8f5", "#e5ebe4"))
            parts.append(f'<circle cx="{x + 54}" cy="{yy + 26}" r="6" fill="{GREEN}"/>')
            parts.append(svg_text(x + 74, yy + 32, bullet, 14, 400))
            yy += 66
        parts.append(svg_rect(x + 32, y + phone_h - 72, phone_w - 64, 42, 21, "#f8faf8", "#e4eae3"))
        nav = "Today   Calendar   Training   Nutrition   Habits"
        parts.append(svg_text(x + 56, y + phone_h - 46, nav, 12, 400, MUTED))
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def make_html(path):
    cards = []
    for title, bullets in SCREENS:
        items = "\n".join(f"<li>{html.escape(item)}</li>" for item in bullets)
        cards.append(f"""
        <section class=\"phone\">
          <header><h2>{html.escape(title)}</h2><div class=\"avatar\">P</div></header>
          <ul>{items}</ul>
          <nav>Today <span>Calendar</span> <span>Training</span> <span>Nutrition</span> <span>Habits</span></nav>
        </section>
        """)
    content = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>Life App MVP Wireframes</title>
  <style>
    body {{ margin: 0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: {BG}; color: {INK}; }}
    main {{ max-width: 1240px; margin: 0 auto; padding: 42px 28px; }}
    h1 {{ margin: 0 0 8px; font-size: 34px; }}
    p {{ margin: 0 0 28px; color: {MUTED}; }}
    .grid {{ display: grid; grid-template-columns: repeat(3, minmax(280px, 1fr)); gap: 28px; }}
    .phone {{ min-height: 440px; border-radius: 34px; background: white; border: 10px solid #101713; padding: 24px; box-shadow: 0 16px 40px rgba(15, 23, 18, .12); display: flex; flex-direction: column; }}
    header {{ display: flex; align-items: center; justify-content: space-between; }}
    h2 {{ margin: 0; font-size: 24px; }}
    .avatar {{ width: 38px; height: 38px; border-radius: 19px; background: #d8f2e5; color: {GREEN}; display: grid; place-items: center; font-weight: 700; }}
    ul {{ list-style: none; padding: 0; margin: 28px 0; display: grid; gap: 14px; }}
    li {{ background: #f5f8f5; border: 1px solid #e5ebe4; border-radius: 16px; padding: 15px 16px; }}
    nav {{ margin-top: auto; background: #f8faf8; border: 1px solid #e4eae3; border-radius: 22px; color: {MUTED}; font-size: 12px; padding: 14px 12px; display: flex; justify-content: space-between; gap: 8px; white-space: nowrap; }}
    nav::first-letter {{ color: {GREEN}; }}
    @media (max-width: 980px) {{ .grid {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
  <main>
    <h1>Life App MVP Wireframes</h1>
    <p>Working title. Garmin-compatible MVP. Profile sits top right, inspired by Garmin Connect.</p>
    <div class=\"grid\">{''.join(cards)}</div>
  </main>
</body>
</html>"""
    path.write_text(content, encoding="utf-8")


def make_markdown(path):
    path.write_text("""# Life App MVP Wireframes

Date: 2026-06-07
Status: Working wireframe v1

## Decisions Captured

- Working title: Life App.
- Core promise: clear daily health, fitness, recovery, nutrition and habit actions.
- First user: Garmin/fitness wearable users.
- MVP requirement: Garmin compatibility from the first version.
- Navigation: Today, Calendar, Training, Nutrition, Habits.
- Profile/settings: top-right profile entry, inspired by Garmin Connect.
- Training section: two sub-tabs, Today and Workouts.

## Screen Map

1. Today
   - Readiness score.
   - Key Garmin-derived signals: sleep, recovery, training, nutrition.
   - Today's actions.
   - Garmin sync state.

2. Calendar
   - Week strip.
   - Today plan.
   - Upcoming training, nutrition and habit items.

3. Training
   - Today / Workouts tabs.
   - Recommended workout.
   - Garmin load, HRV, recovery and last workout data.
   - Workout history.

4. Nutrition
   - Calories and macro progress.
   - Protein / fueling insight based on today's training.
   - Quick add actions.

5. Habits
   - Daily habit checklist.
   - Streaks.
   - Step goal and sleep routine.

6. Profile
   - Garmin Connect connection.
   - Optional Apple Health and Strava connections.
   - Goals.
   - Simple mode / Performance mode.

## Saved Assets

- `mock-today-dashboard.png`
- `mock-training-workouts.png`
- `mock-today-dashboard-whoop-vibe.png`
- `mock-training-workouts-whoop-vibe.png`
- `life-app-wireframe-board.svg`
- `life-app-wireframe-board.html`
""", encoding="utf-8")


if __name__ == "__main__":
    draw_today(OUT / "mock-today-dashboard.png")
    draw_training(OUT / "mock-training-workouts.png")
    draw_today_whoop(OUT / "mock-today-dashboard-whoop-vibe.png")
    draw_training_whoop(OUT / "mock-training-workouts-whoop-vibe.png")
    make_svg_board(OUT / "life-app-wireframe-board.svg")
    make_html(OUT / "life-app-wireframe-board.html")
    make_markdown(OUT / "life-app-wireframe-v1.md")
