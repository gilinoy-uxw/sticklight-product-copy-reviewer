---
name: "Sticklight Copy Reviewer"
version: "1.2.0"
description: "Reviews product copy against Sticklight's brand glossary, voice & tone guidelines, and UX writing best practices. Supports both the Sticklight builder and the Pink hosting product."
author: "Elementor Content Design"
license: "CC-BY-NC-4.0"
entry_point: "prompts/review.txt"
data:
  - data/glossary.json
  - data/pink-glossary.json
  - data/writing-guidelines.json
---

# Sticklight Copy Reviewer

Reviews copy for the Sticklight product family — the AI-powered web builder and the Pink hosting and deployment product.

Evaluates copy across three dimensions: glossary compliance, brand voice & tone, and UX writing quality.

## Product scope

This skill supports two products with separate glossaries:

| Product | Glossary file | When to use |
|---|---|---|
| Sticklight | `data/glossary.json` | Builder UI, onboarding, editor, chat, modes, skills, templates |
| Pink | `data/pink-glossary.json` | Hosting setup, deployment, environments, domains, variables |

The `writing-guidelines.json` rules apply to both products.

**Key term clashes to be aware of:**
- **Workspace** — creation start screen in Sticklight / account and team container in Pink
- **Project** — saved builder output in Sticklight / managed hosted app in Pink
- **Build** — flexible copy alongside Create in Sticklight / specific pipeline step in Pink

## Usage

Trigger the review with a product declaration at the start of the input:

```
PRODUCT: sticklight
[copy to review]
```

```
PRODUCT: pink
[copy to review]
```

## Data files

- `data/glossary.json` — Sticklight builder terms
- `data/pink-glossary.json` — Pink product terms
- `data/writing-guidelines.json` — shared voice, tone, grammar, and UX writing rules
