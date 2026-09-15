#!/usr/bin/env python3
"""Emit the Constitution's axiom figures as SVGs computed from tcg_models.

The three figures this replaces were hand-made PNGs. Nothing connected them to
the equations they claimed to illustrate, so retuning a coefficient left the
picture quietly asserting the old one. Every curve here is sampled from a
function in tcg_models.py, so the figures cannot drift from the math without
the diff check failing.

    python3 models/make_figures.py            # write the SVGs
    python3 models/make_figures.py --check    # regenerate and fail on diff

Deliberately dependency-free, like tcg_models.py and the two checkers in
tools/linting/. The SVG is written by hand rather than by a
plotting library so that the diff check runs anywhere Python does, the output
is byte-for-byte reproducible, and the prefers-color-scheme block is authored
directly rather than injected by post-processing.

VALE DOES NOT READ SVG. Vale's scope is *.md, so the labels below escape the
banned-word list, the emoji ban, and the retired-terms rule. They are checked
by check_figure_text() at the bottom of this file, which reads the same
RetiredTerms.yml and AntiHype.yml the Markdown is held to.

CALIBRATION: every parameter driving these curves is a reasoned starting value
carried from the documents, not an empirical estimate. Each figure carries that
statement in its own subtitle, because a picture reads as evidence in a way
prose does not.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tcg_models as m

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSETS = os.path.join(ROOT, "theory", "01-foundation", "assets")
STYLES = os.path.join(ROOT, "tools", "linting", "styles", "TCG")

W, H = 760, 470
PAD_L, PAD_R, PAD_T, PAD_B = 78, 34, 92, 74
PLOT_W = W - PAD_L - PAD_R
PLOT_H = H - PAD_T - PAD_B

# One theme block, shared by all three figures. The light palette is defined on
# bare :root so it is never the case that a colour exists only inside a media
# query; the dark block redefines the same tokens and nothing else.
THEME = """
  :root {
    --ink: #16181d;
    --muted: #5d636e;
    --axis: #333740;
    --grid: #e3e5ea;
    --bg: #ffffff;
    --panel: #f7f8fa;
    --primary: #1f5f8b;
    --primary-fill: rgba(31, 95, 139, 0.13);
    --alert: #a4373a;
    --alert-fill: rgba(164, 55, 58, 0.11);
    --good: #1d6f52;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --ink: #e9ebef;
      --muted: #a2a9b5;
      --axis: #99a0ac;
      --grid: #2f333b;
      --bg: #14161a;
      --panel: #1b1e24;
      --primary: #7fb6dd;
      --primary-fill: rgba(127, 182, 221, 0.17);
      --alert: #e58e90;
      --alert-fill: rgba(229, 142, 144, 0.15);
      --good: #6cc39c;
    }
  }
  .bg { fill: var(--bg); }
  .panel { fill: var(--panel); }
  .axis { stroke: var(--axis); stroke-width: 1.4; fill: none; }
  .grid { stroke: var(--grid); stroke-width: 1; fill: none; }
  .curve { fill: none; stroke-width: 2.6; stroke-linejoin: round;
           stroke-linecap: round; }
  .primary { stroke: var(--primary); }
  .alert { stroke: var(--alert); }
  .good { stroke: var(--good); }
  .dashed { stroke-dasharray: 7 5; }
  .thin { stroke-width: 1.6; }
  text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
         "Helvetica Neue", Arial, sans-serif; fill: var(--ink); }
  .title { font-size: 19px; font-weight: 650; }
  .subtitle { font-size: 12.5px; fill: var(--muted); }
  .axis-label { font-size: 13px; fill: var(--muted); }
  .tick { font-size: 11.5px; fill: var(--muted); }
  .note { font-size: 12.5px; font-weight: 600; }
  .note-muted { font-size: 12px; fill: var(--muted); }
"""


def _n(value):
    """Format a coordinate so output is byte-for-byte reproducible."""
    return "{:.2f}".format(value + 0.0).rstrip("0").rstrip(".") or "0"


class Axes:
    """A single linear plotting area. Data coordinates in, SVG string out."""

    def __init__(self, x_range, y_range):
        self.x0, self.x1 = x_range
        self.y0, self.y1 = y_range

    def px(self, x):
        return PAD_L + (x - self.x0) / (self.x1 - self.x0) * PLOT_W

    def py(self, y):
        return PAD_T + PLOT_H - (y - self.y0) / (self.y1 - self.y0) * PLOT_H

    def path(self, points, css):
        d = " ".join(
            ("M" if i == 0 else "L") + _n(self.px(x)) + " " + _n(self.py(y))
            for i, (x, y) in enumerate(points))
        return '  <path class="curve {}" d="{}"/>'.format(css, d)

    def hline(self, y, css="grid"):
        return '  <line class="{}" x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(
            css, _n(PAD_L), _n(self.py(y)), _n(PAD_L + PLOT_W), _n(self.py(y)))

    def vline(self, x, css="grid"):
        return '  <line class="{}" x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(
            css, _n(self.px(x)), _n(PAD_T), _n(self.px(x)),
            _n(PAD_T + PLOT_H))

    def label(self, x, y, text, css="note", anchor="start", dy=0):
        return '  <text class="{}" x="{}" y="{}" text-anchor="{}">{}</text>'\
            .format(css, _n(self.px(x)), _n(self.py(y) + dy), anchor,
                    _escape(text))

    def dot(self, x, y, css="primary"):
        return '  <circle cx="{}" cy="{}" r="4.2" fill="var(--{})"/>'.format(
            _n(self.px(x)), _n(self.py(y)),
            "primary" if css == "primary" else css)


def _escape(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def _frame(title, subtitle, axes, x_label, y_label, x_ticks, y_ticks, body,
           desc):
    """Assemble one figure. Title, axes, ticks, then the caller's marks."""
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {} {}" '
        'width="{}" height="{}" role="img" aria-labelledby="figtitle figdesc">'
        .format(W, H, W, H),
        '<title id="figtitle">{}</title>'.format(_escape(title)),
        '<desc id="figdesc">{}</desc>'.format(_escape(desc)),
        '<style>{}</style>'.format(THEME),
        '  <rect class="bg" x="0" y="0" width="{}" height="{}"/>'.format(W, H),
        '  <rect class="panel" x="{}" y="{}" width="{}" height="{}"/>'.format(
            _n(PAD_L), _n(PAD_T), _n(PLOT_W), _n(PLOT_H)),
        '  <text class="title" x="{}" y="34">{}</text>'.format(
            PAD_L, _escape(title)),
        '  <text class="subtitle" x="{}" y="55">{}</text>'.format(
            PAD_L, _escape(subtitle)),
    ]
    for value, text in x_ticks:
        out.append(axes.vline(value))
        out.append(
            '  <text class="tick" x="{}" y="{}" text-anchor="middle">{}</text>'
            .format(_n(axes.px(value)), _n(PAD_T + PLOT_H + 20),
                    _escape(text)))
    for value, text in y_ticks:
        out.append(axes.hline(value))
        out.append(
            '  <text class="tick" x="{}" y="{}" text-anchor="end">{}</text>'
            .format(_n(PAD_L - 10), _n(axes.py(value) + 4), _escape(text)))
    out.append(
        '  <path class="axis" d="M{} {} L{} {} L{} {}"/>'.format(
            _n(PAD_L), _n(PAD_T), _n(PAD_L), _n(PAD_T + PLOT_H),
            _n(PAD_L + PLOT_W), _n(PAD_T + PLOT_H)))
    out.extend(body)
    # Axis titles last, well clear of the tick row so nothing overlaps.
    out.append(
        '  <text class="axis-label" x="{}" y="{}" text-anchor="middle">{}'
        '</text>'.format(_n(PAD_L + PLOT_W / 2), _n(H - 22), _escape(x_label)))
    out.append(
        '  <text class="axis-label" x="0" y="0" text-anchor="middle" '
        'transform="translate({} {}) rotate(-90)">{}</text>'.format(
            _n(22), _n(PAD_T + PLOT_H / 2), _escape(y_label)))
    out.append('</svg>')
    return "\n".join(out) + "\n"


def _legend(entries, x, y):
    """A legend block in plot coordinates, so labels never sit on a curve."""
    out = []
    for i, (css, dash, text) in enumerate(entries):
        row = y + i * 21
        out.append(
            '  <line class="curve {} {}" x1="{}" y1="{}" x2="{}" y2="{}"/>'
            .format(css, dash, _n(x), _n(row), _n(x + 30), _n(row)))
        out.append(
            '  <text class="note-muted" x="{}" y="{}">{}</text>'.format(
                _n(x + 39), _n(row + 4.5), _escape(text)))
    return out


UNFITTED = ("Parameters are reasoned starting values, not fitted to deal "
            "data. Read the shape, not the numbers.")


# ==========================================================================
# Panel 1 — Axiom I. Value decay against the next-best floor.
# ==========================================================================

def panel_1():
    """V_effective(t) = V_0 * exp(-delta t) against V_next_best.

    Illustrates Axiom I's time dynamics and the only term in delta a seller can
    move. delta comes from the structural form of 02-mathematical-models.md
    section 4.2, so the two curves differ only in the external catalyst.
    """
    v0, v_next_best = 100.0, 40.0
    months = [t / 4.0 for t in range(0, 97)]  # 0 to 24 months
    inertia = 0.4

    d_none = m.decay_rate(inertia, e_external=0.0)
    d_catalyst = m.decay_rate(inertia, e_external=8.0)

    no_catalyst = [(t, m.value_decay(v0, d_none, t)) for t in months]
    catalyst = [(t, m.value_decay(v0, d_catalyst, t)) for t in months]

    axes = Axes((0, 24), (0, 112))
    body = [
        '  <line class="curve good thin" x1="{}" y1="{}" x2="{}" y2="{}"/>'
        .format(_n(PAD_L), _n(axes.py(v_next_best)),
                _n(PAD_L + PLOT_W), _n(axes.py(v_next_best))),
        axes.label(23.5, v_next_best + 5, "Value of the next best alternative",
                   "note-muted", anchor="end"),
        axes.path(no_catalyst, "alert dashed"),
        axes.path(catalyst, "primary"),
    ]
    body += _legend([
        ("alert", "dashed", "Organizational inertia alone"),
        ("primary", "", "With a named external catalyst"),
    ], PAD_L + PLOT_W - 250, PAD_T + 26)

    # Where each curve reaches the floor, the deal has stopped existing.
    for series in (no_catalyst, catalyst):
        crossing = _first_crossing(series, v_next_best)
        if crossing is None or crossing > 24:
            continue
        body.append(axes.dot(crossing, v_next_best))
        # Anchor each label away from its own curve rather than centring it,
        # since both curves pass close to the floor near their crossing.
        body.append(axes.label(
            crossing - 0.4, v_next_best - 9,
            "month {:.0f}".format(crossing), "note", anchor="end"))
    body.append(axes.label(
        12.0, 12.0, "Below the line the buyer keeps the status quo",
        "note-muted", anchor="middle"))
    return _frame(
        title="Axiom I: urgency decays from the triggering event",
        subtitle=UNFITTED,
        axes=axes,
        x_label="Months since the triggering event",
        y_label="Perceived value of solving",
        x_ticks=[(0, "0"), (6, "6"), (12, "12"), (18, "18"), (24, "24")],
        y_ticks=[(0, "0"), (40, "40"), (80, "80")],
        body=body,
        desc="Two exponential decay curves falling from a peak perceived "
             "value of 100 toward a horizontal floor at 40, the value of the "
             "buyer's next best alternative. The curve driven by "
             "organizational inertia alone reaches the floor in the second "
             "month. The curve with a named external catalyst decays roughly "
             "five times more slowly and does not reach the floor until the "
             "eleventh. Below the floor the buyer keeps the status quo.")


def _first_crossing(series, level):
    for (x0, y0), (x1, y1) in zip(series, series[1:]):
        if y0 >= level >= y1 and y0 != y1:
            return x0 + (y0 - level) / (y0 - y1) * (x1 - x0)
    return None


# ==========================================================================
# Panel 2 — Axiom II. Convexity, and why discounting fails.
# ==========================================================================

def panel_2():
    """y = a * gap^2 + c against a linear counterfactual.

    Section 1.2 says the reduced form's whole value is argumentative: it shows
    why cutting the constant term through discounting cannot offset a large
    gap. That argument is exactly a comparison of three curves, so the figure
    is the argument rather than a decoration on it.
    """
    # In annual contract values, per 02-mathematical-models.md section 1.7.
    # A deal at list price is 1 ACV of direct cost; the discounted line is the
    # same deal at 40 percent of it, which is a steeper concession than any
    # real desk would approve and still does not reach the quadratic term.
    c_list, c_discounted = 1.0, 0.4
    samples = [x / 100.0 for x in range(0, 101)]
    gaps = [m.NormalizedGap(x) for x in samples]

    quoted = [(float(g), m.reduced_cost(g, c=c_list)) for g in gaps]
    discounted = [(float(g), m.reduced_cost(g, c=c_discounted)) for g in gaps]
    # A linear cost of uncertainty, pinned to the same endpoints, is the
    # intuition the convex form displaces.
    top = m.reduced_cost(m.NormalizedGap(1.0), c=c_list)
    linear = [(x, c_list + (top - c_list) * x) for x in samples]

    axes = Axes((0, 1), (0, 3.6))
    body = [
        axes.path(linear, "good dashed thin"),
        axes.path(discounted, "primary dashed"),
        axes.path(quoted, "alert"),
    ]
    body += _legend([
        ("alert", "", "Perceived cost at list price"),
        ("primary", "dashed", "The same deal after a deep discount"),
        ("good", "dashed thin", "What a linear cost of uncertainty would do"),
    ], PAD_L + 16, PAD_T + 26)

    # The claim the figure exists to make: a discount lowers c and leaves the
    # quadratic term untouched, so the bracket below is the part of perceived
    # cost that no price concession reaches.
    wide = 0.9
    floor_y = c_discounted
    curve_y = m.reduced_cost(m.NormalizedGap(wide), c=c_discounted)
    body += [
        '  <line class="grid thin" stroke-dasharray="3 4" x1="{}" y1="{}" '
        'x2="{}" y2="{}" stroke="var(--muted)"/>'.format(
            _n(PAD_L), _n(axes.py(floor_y)),
            _n(axes.px(wide)), _n(axes.py(floor_y))),
        axes.label(0.02, floor_y - 0.24, "Discounted price on its own",
                   "note-muted"),
        '  <line class="curve thin" stroke="var(--ink)" x1="{}" y1="{}" '
        'x2="{}" y2="{}"/>'.format(
            _n(axes.px(wide)), _n(axes.py(floor_y)),
            _n(axes.px(wide)), _n(axes.py(curve_y))),
        axes.dot(wide, curve_y),
        axes.label(0.985, floor_y - 0.24,
                   "What uncertainty adds. No discount reaches it.",
                   "note", anchor="end"),
    ]
    return _frame(
        title="Axiom II: perceived cost is convex in uncertainty",
        subtitle=UNFITTED,
        axes=axes,
        x_label="Normalized bilateral asymmetry gap",
        y_label="Perceived cost, in annual contract values",
        x_ticks=[(0, "0"), (0.25, "0.25"), (0.5, "0.5"), (0.75, "0.75"),
                 (1, "1.0")],
        y_ticks=[(0, "0"), (1, "1"), (2, "2"), (3, "3")],
        body=body,
        desc="Perceived transaction cost plotted against the normalized "
             "bilateral asymmetry gap. The list-price curve is convex, rising "
             "slowly at a narrow gap and steeply at a wide one. A deep "
             "discount shifts the whole curve downward by a constant amount "
             "without changing its shape. A dashed straight line shows what a "
             "linear cost of uncertainty would look like instead. At a wide "
             "gap a bracket marks the vertical distance between the "
             "discounted price and the discounted curve: the share of "
             "perceived cost that comes from uncertainty, which no price "
             "concession removes.")


# ==========================================================================
# Panel 3 — Axiom III. Asymmetry drift after signature.
# ==========================================================================

def panel_3():
    """gap_hat_implementation(t) = gap_hat(0) + gamma_impl * t.

    Section 7.2 of 04-seller-surplus-model.md argues the durable asset is
    asymmetric information rather than lock-in: after a forward-deployed
    engagement the incumbent's implementation gap approaches zero while a
    challenger starts near the ceiling. The incumbent's advantage is the
    vertical distance between the two, and it erodes at gamma_implementation
    unless C_sustain holds that rate down.

    The component matters. Constitution v17.0 splits drift into three rates,
    and the drivers this curve runs on, staff turnover, workflow change and
    systems installed unseen, are all implementation drivers. An incumbent
    whose consensus gap reopens loses the account a different way, faster and
    without a curve.
    """
    start = m.NormalizedGap(0.08)
    challenger = 1.0
    months = [t / 2.0 for t in range(0, 73)]  # 0 to 36 months

    unmaintained = [(t, float(m.asymmetry_drift(start, 0.026, t)))
                    for t in months]
    maintained = [(t, float(m.asymmetry_drift(start, 0.005, t)))
                  for t in months]

    axes = Axes((0, 36), (0, 1.15))
    body = [
        '  <line class="curve alert thin" x1="{}" y1="{}" x2="{}" y2="{}"/>'
        .format(_n(PAD_L), _n(axes.py(challenger)),
                _n(PAD_L + PLOT_W), _n(axes.py(challenger))),
        axes.label(35.4, challenger + 0.045, "Challenger starts here",
                   "note-muted", anchor="end"),
        axes.path(unmaintained, "alert dashed"),
        axes.path(maintained, "good"),
        axes.label(26.5, float(m.asymmetry_drift(start, 0.026, 26.5)) + 0.075,
                   "Without sustaining spend", "note", anchor="middle"),
        axes.label(20.0, float(m.asymmetry_drift(start, 0.005, 20.0)) + 0.075,
                   "With sustaining spend", "note", anchor="middle"),
        axes.dot(0, float(start), "good"),
        axes.label(1.2, float(start) - 0.055, "At go-live", "note-muted"),
    ]
    return _frame(
        title="Axiom III: the incumbent advantage erodes unless it is held",
        subtitle=UNFITTED,
        axes=axes,
        x_label="Months after signature",
        y_label="Incumbent implementation gap",
        x_ticks=[(0, "0"), (12, "12"), (24, "24"), (36, "36")],
        y_ticks=[(0, "0"), (0.5, "0.5"), (1.0, "1.0")],
        body=body,
        desc="Two rising lines starting from a near-zero asymmetry gap at "
             "go-live, plotted against a horizontal line marking where a "
             "challenger begins. The unmaintained line climbs steadily and "
             "approaches the challenger line within three years, closing the "
             "incumbent advantage. The maintained line rises far more slowly "
             "and stays well below it.")


FIGURES = {
    "axiom-1-urgency-decay.svg": panel_1,
    "axiom-2-cost-convexity.svg": panel_2,
    "axiom-3-asymmetry-drift.svg": panel_3,
}


# ==========================================================================
# The rule Vale cannot enforce, because its scope is *.md.
# ==========================================================================

EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF☀-➿←-⇿️⬀-⯿]")


def _retired_terms():
    """Read the swap: block of RetiredTerms.yml. Same source Vale uses."""
    path = os.path.join(STYLES, "RetiredTerms.yml")
    terms, in_swap = [], False
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("swap:"):
                in_swap = True
                continue
            if in_swap:
                if line.strip() and not line.startswith((" ", "\t")):
                    break
                if ":" in line and line.strip():
                    terms.append(line.split(":", 1)[0].strip().strip("'\""))
    return terms


def _banned_words():
    """Read the tokens: block of AntiHype.yml."""
    path = os.path.join(STYLES, "AntiHype.yml")
    words, in_tokens = [], False
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("tokens:"):
                in_tokens = True
                continue
            if in_tokens:
                if line.strip().startswith("-"):
                    words.append(line.strip()[1:].strip().strip("'\""))
                elif line.strip() and not line.startswith((" ", "\t")):
                    break
    return words


def check_figure_text(svg, name):
    """Hold SVG label text to the rules Vale applies to Markdown.

    Vale's scope is *.md, so nothing else stops a banned word, an emoji, or a
    retired term from entering the repository inside a figure. This closes that
    hole for the figures this file generates.
    """
    errors = []
    visible = " ".join(re.findall(r">([^<>]+)<", svg))
    if EMOJI.search(visible):
        errors.append("{}: contains an emoji".format(name))
    lowered = visible.lower()
    for word in _banned_words():
        if re.search(r"\b" + re.escape(word.lower()) + r"\b", lowered):
            errors.append("{}: uses the banned word {!r}".format(name, word))
    # RetiredTerms.yml sets ignorecase: false, and AntiHype.yml sets it true.
    # Honour each rule's own flag so a figure is held to exactly what the
    # Markdown is held to, no more and no less.
    for term in _retired_terms():
        try:
            pattern = re.compile(term)
        except re.error:
            continue
        if pattern.search(visible):
            errors.append("{}: uses the retired term {!r}".format(name, term))
    return errors


def render_all():
    return {name: builder() for name, builder in sorted(FIGURES.items())}


def main(argv):
    check_only = "--check" in argv
    rendered = render_all()

    style_errors = []
    for name, svg in rendered.items():
        style_errors.extend(check_figure_text(svg, name))
    if style_errors:
        for error in style_errors:
            print("FAIL {}".format(error))
        return 1

    if not os.path.isdir(ASSETS):
        os.makedirs(ASSETS)

    stale = []
    for name, svg in rendered.items():
        path = os.path.join(ASSETS, name)
        current = None
        if os.path.exists(path):
            with open(path, encoding="utf-8") as handle:
                current = handle.read()
        if current == svg:
            continue
        if check_only:
            stale.append(name)
            continue
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(svg)
        print("wrote theory/01-foundation/assets/{}".format(name))

    if check_only:
        if stale:
            print("FAIL these figures no longer match the equations that "
                  "generate them:")
            for name in stale:
                print("  theory/01-foundation/assets/{}".format(name))
            print("Run: python3 models/make_figures.py")
            return 1
        print("All {} figures match the equations that generate "
              "them.".format(len(rendered)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
