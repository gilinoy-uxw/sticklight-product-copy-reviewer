---
name: "Sticklight Copy Reviewer"
version: "2.0.0"
description: "Reviews in-product UI copy and conversational design against Sticklight's brand glossary, voice & tone guidelines, and UX writing best practices. Supports both the Sticklight builder and the Pink hosting product."
author: "Elementor Content Design"
license: "CC-BY-NC-4.0"
entry_point: "prompts/review.txt"
data:
  - data/glossary.json
  - data/pink-glossary.json
  - data/writing-guidelines.json
  - reference/term-clashes.md
  - reference/calibration.md
---

# Sticklight Copy Reviewer

Reviews copy for the Sticklight product family — the AI-powered web builder and the Pink hosting and deployment product.

## Structure

```
data/
  glossary.json              # Sticklight terms — source of truth
  pink-glossary.json         # Pink terms — source of truth
  writing-guidelines.json    # 50 rules with reviewer_behavior field
reference/
  term-clashes.md            # Cross-product clash reference (single source)
  calibration.md             # Good/bad examples per dimension
prompts/
  review.txt                 # Instructions + output format only
```

## Separation of concerns

| File | Purpose |
|---|---|
| `glossary.json` / `pink-glossary.json` | WHAT terms are approved, avoided, or allowed |
| `writing-guidelines.json` | WHAT rules apply and HOW each should be handled (flag/silent/scope) |
| `reference/term-clashes.md` | WHERE terms differ between products |
| `reference/calibration.md` | WHAT acceptable copy looks like per dimension |
| `prompts/review.txt` | HOW to run the review and format the output |

## reviewer_behavior field

Every rule in `writing-guidelines.json` has a `reviewer_behavior` field:
- `"flag"` — creates an issue card in the output
- `"silent"` — applied in improved_text only, no issue card created
- `"scope"` — skipped; not a review criterion

Currently: 41 flag rules, 8 silent rules, 1 scope rule.

## Product scope

| Product | Glossary | When to use |
|---|---|---|
| Sticklight | `data/glossary.json` | Builder UI, onboarding, editor, chat, modes, skills, templates |
| Pink | `data/pink-glossary.json` | Hosting setup, deployment, environments, domains, variables |

The writing guidelines and reference files apply to both products.

## Usage

```
PRODUCT: sticklight
[copy to review]
```

```
PRODUCT: pink
[copy to review]
```

## Updating

- **New glossary term** → add to `glossary.json` or `pink-glossary.json`. If it's a cross-product clash, also update `reference/term-clashes.md`.
- **New rule** → add to `writing-guidelines.json` with a `reviewer_behavior` field.
- **New examples** → add to `reference/calibration.md`.
- **After any JSON update** → regenerate fallback constants in `ui.html` by running the logic in `data/_fallbacks.py`.
