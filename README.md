# Sticklight Copy Reviewer

An AI-powered product copy reviewer built for [Sticklight](https://sticklight.io).

This skill checks text or screenshots against Sticklight's **brand glossary**, **voice & tone guidelines**, and **UX writing best practices** — identifies misalignments, explains why, and suggests improved, on-brand alternatives.

Compatible with **Claude Desktop**, **Claude Code**, **Cursor**, and other compatible tools.

---

## What it does

The Sticklight Copy Reviewer helps writers, designers, and product teams ensure all product copy follows official terminology, voice standards, and UX writing principles.

It evaluates copy across three dimensions:

| Dimension | What it checks |
|---|---|
| **Glossary** | Approved terms, avoided terms, correct capitalization and context |
| **Brand voice & tone** | Voice consistency, tone-to-context match, grammar, style |
| **UX writing** | Clarity, structure, empty states, errors, CTAs, onboarding, parallel structure |

---

## Folder structure

```
sticklight-copy-reviewer/
├── SKILL.md                   # Skill metadata for Claude, Cursor, Codex
├── prompts/
│   └── review.txt             # Main analysis prompt with full review logic
├── data/
│   ├── glossary.json          # Approved/avoided terms, definitions, usage rules
│   └── writing-guidelines.json # Voice, tone, grammar, and UX writing rules
└── README.md                  # You're here
```

---

## How it works

1. The skill loads `glossary.json` and `writing-guidelines.json` as its source of truth.
2. When a user pastes copy or uploads a screenshot, the reviewer:
   - Extracts and reads the text
   - Checks it against approved terminology
   - Evaluates tone, voice, grammar, and UX writing quality
   - Returns structured feedback with issue type, rationale, and a concrete suggestion per finding
   - Rewrites the full input as a clean, on-brand alternative

### Output structure

```json
{
  "issues": [
    {
      "type": "Glossary",
      "rule_or_term": "Workspace",
      "issue": "Used 'homepage' instead of 'Workspace'",
      "rationale": "Per glossary, 'Workspace' is the approved term for the main starting screen. 'Homepage' is explicitly avoided.",
      "suggestion": "Back to Workspace"
    },
    {
      "type": "UX Writing",
      "rule_or_term": "ux-07",
      "issue": "'Just click Create to get started' uses 'just', which minimizes the user's effort",
      "rationale": "Per rule ux-07, avoid 'just', 'simply', or 'easy' in instructional copy. These can feel dismissive when a task has real steps.",
      "suggestion": "Click Create to get started"
    }
  ],
  "improved_text": "Back to Workspace. Click Create to get started."
}
```

---

## Getting started

### Clone or download

```bash
git clone https://github.com/gilinoy-uxw/sticklight-copy-reviewer
```

### Use in Claude Desktop

1. Zip the folder
2. Upload via **Settings → Skills → Upload skill**

### Use in Cursor

1. Open **Settings → Rules, Skills, Subagents**
2. Click **New Skill**
3. Paste this prompt:

```
Sticklight Copy Reviewer skill:
Analyze any text or screenshot and check it against Sticklight's brand glossary (data/glossary.json) and writing guidelines (data/writing-guidelines.json). Identify what's off across glossary, voice & tone, and UX writing. Explain why, and suggest improved, on-brand alternatives.
```

4. Add the `/data` folder with both JSON files.
5. Save — Cursor will create the local skill automatically.

### Use in Claude Code

Move or link the folder into your local skills directory:

```bash
~/.claude/skills/sticklight-copy-reviewer/
```

Then trigger it:

```
/use-skill Sticklight Copy Reviewer
```

---

## Example

**Input**

```
Review this copy for Sticklight style:
"Go back to the homepage and use the AI panel to generate your next amazing project!"
```

**Output**

```json
{
  "issues": [
    {
      "type": "Glossary",
      "rule_or_term": "Workspace",
      "issue": "Used 'homepage' instead of the approved term 'Workspace'",
      "rationale": "Per glossary, 'Workspace' is the approved term for the main starting screen. 'Homepage' is explicitly listed as an avoided term.",
      "suggestion": "Back to Workspace"
    },
    {
      "type": "Glossary",
      "rule_or_term": "Chat panel",
      "issue": "Used 'AI panel' instead of the approved term 'Chat panel'",
      "rationale": "Per glossary, 'AI panel' is listed as an avoided term. 'Chat panel' is the approved name for the left-side interaction area.",
      "suggestion": "Open the Chat panel"
    },
    {
      "type": "Glossary",
      "rule_or_term": "Create",
      "issue": "Used 'generate' as the main action verb instead of 'Create'",
      "rationale": "Per glossary, 'Generate' is avoided as the primary CTA. It makes Sticklight feel like a one-shot AI output rather than a controllable creation platform.",
      "suggestion": "create your next project"
    },
    {
      "type": "Voice",
      "rule_or_term": "style-04",
      "issue": "'Amazing' is an empty intensifier that adds noise without meaning",
      "rationale": "Per rule style-04, filler adjectives like 'amazing' or 'stunning' should be cut. The product should speak for itself.",
      "suggestion": "create your next project"
    }
  ],
  "improved_text": "Back to Workspace. Open the Chat panel to create your next project."
}
```

---

## Customization

- **Update `data/glossary.json`** to add or edit approved product terms as Sticklight evolves.
- **Update `data/writing-guidelines.json`** to add new voice, tone, or UX writing rules.
- **Edit `prompts/review.txt`** to change how results are structured or what gets prioritized.

---

## License

Creative Commons Attribution-NonCommercial 4.0 International
© Elementor Ltd., 2025

---

## Contributors

**Elementor Content Design Team**
Built with care for the creators building on Sticklight.
