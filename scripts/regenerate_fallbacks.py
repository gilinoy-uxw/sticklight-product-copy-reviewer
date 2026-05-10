"""
regenerate_fallbacks.py

Reads data/glossary.json, data/pink-glossary.json, and data/writing-guidelines.json
and replaces the FALLBACK_GLOSSARY, FALLBACK_PINK_GLOSSARY, and FALLBACK_RULES
constants in ui.html with freshly generated versions.

Run automatically by the 'Regenerate fallbacks' GitHub Action whenever a data file changes.
"""

import json

from pathlib import Path

ROOT = Path(__file__).parent.parent.parent  # repo root


def load(path):
    with open(ROOT / path, encoding="utf-8") as f:
        return json.load(f)


def gen_glossary_fallback(terms_data):
    terms = terms_data.get("terms", [])
    lines = []
    for t in terms:
        term = t.get("term", "")
        approved = '", "'.join(t.get("approved", [term])[:2])
        avoid = t.get("avoid", [])
        also = t.get("also_allowed", [])
        clash = t.get("clash_warning", "")
        definition = t.get("definition", "").split(".")[0] if t.get("definition") else ""

        avoid_str = ('", "'.join([a.split("(")[0].strip() for a in avoid[:4]])) if avoid else ""
        also_str = ('", "'.join(also[:2])) if also else ""

        line = f'- CORRECT: "{approved}"'
        if avoid_str:
            line += f' NOT: "{avoid_str}"'
        if also_str:
            line += f' Also allowed: "{also_str}"'
        if definition:
            line += f" — {definition}"
        if clash:
            line += f" ⚠ {clash}"
        lines.append(line)
    return "\n".join(lines)


def gen_rules_fallback(rules_data):
    rules = rules_data.get("rules", [])
    flag_rules = [r for r in rules if r.get("reviewer_behavior") == "flag"]
    silent_rules = [r for r in rules if r.get("reviewer_behavior") == "silent"]

    flag_lines = "\n".join(
        f"{i + 1}. [{r['id']}] {r['rule']}"
        for i, r in enumerate(flag_rules)
    )
    silent_lines = "\n".join(
        f"• {r['rule']}"
        for r in silent_rules
    )
    return (
        flag_lines
        + "\n\nSILENT IMPROVEMENTS — apply in improved_text only, do NOT flag:\n"
        + silent_lines
    )


def escape_for_js_template_literal(s):
    """Escape backticks and ${} for use inside a JS template literal."""
    s = s.replace("\\", "\\\\")
    s = s.replace("`", "\\`")
    s = s.replace("${", "\\${")
    return s


def replace_constant(html, const_name, new_value):
    """Replace const NAME = `...`; in the HTML string.
    Uses a line-by-line approach to avoid catastrophic backtracking or
    accidental large-span matches from the regex engine.
    """
    escaped = escape_for_js_template_literal(new_value)
    marker_open = f"const {const_name} = `"
    marker_close = "`;\n"

    start = html.find(marker_open)
    if start == -1:
        raise ValueError(f"Could not find constant: {const_name}")

    # Walk forward from after the opening backtick to find the closing `;\n
    content_start = start + len(marker_open)
    pos = content_start
    while pos < len(html):
        if html[pos] == '\\':
            pos += 2  # skip escaped character
            continue
        if html[pos:pos + 3] == '`;\n':
            end = pos + 3
            break
        pos += 1
    else:
        raise ValueError(f"Could not find closing backtick for: {const_name}")

    return html[:start] + f"const {const_name} = `{escaped}`;\n" + html[end:]


def main():
    glossary = load("data/glossary.json")
    pink_glossary = load("data/pink-glossary.json")
    writing_guidelines = load("data/writing-guidelines.json")

    fb_glossary = gen_glossary_fallback(glossary)
    fb_pink = gen_glossary_fallback(pink_glossary)
    fb_rules = gen_rules_fallback(writing_guidelines)

    ui_path = ROOT / "ui.html"
    html = ui_path.read_text(encoding="utf-8")

    html = replace_constant(html, "FALLBACK_GLOSSARY", fb_glossary)
    html = replace_constant(html, "FALLBACK_PINK_GLOSSARY", fb_pink)
    html = replace_constant(html, "FALLBACK_RULES", fb_rules)

    ui_path.write_text(html, encoding="utf-8")

    glossary_terms = len(glossary.get("terms", []))
    pink_terms = len(pink_glossary.get("terms", []))
    flag_rules = sum(1 for r in writing_guidelines.get("rules", []) if r.get("reviewer_behavior") == "flag")
    silent_rules = sum(1 for r in writing_guidelines.get("rules", []) if r.get("reviewer_behavior") == "silent")

    print(f"✓ FALLBACK_GLOSSARY regenerated ({glossary_terms} terms)")
    print(f"✓ FALLBACK_PINK_GLOSSARY regenerated ({pink_terms} terms)")
    print(f"✓ FALLBACK_RULES regenerated ({flag_rules} flag rules, {silent_rules} silent rules)")
    print("✓ ui.html updated")


if __name__ == "__main__":
    main()
