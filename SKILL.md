---
name: "Sticklight Copy Reviewer"
version: "1.0.0"
description: "Reviews product copy against Sticklight's brand glossary, voice & tone guidelines, and UX writing best practices. Identifies misalignments, explains why, and suggests improved alternatives."
author: "Elementor Content Design"
license: "CC-BY-NC-4.0"
entry_point: "prompts/review.txt"
data:
  - data/glossary.json
  - data/writing-guidelines.json
---

# Sticklight Copy Reviewer

This skill analyzes text or screenshots and checks them against Sticklight's brand glossary, voice & tone guidelines, and UX writing standards.

It identifies misaligned phrases, explains why they miss the mark, and suggests improved, on-brand alternatives — not only for brand compliance, but also for clarity, structure, and usability.

## Features

- Checks all copy against approved terminology and flags avoided terms
- Enforces tone, voice, grammar, and style standards
- Flags UX writing issues: empty states, error messages, CTAs, onboarding, parallel structure
- Explains every issue with a clear rationale
- Suggests an improved rewrite for every flagged phrase
- Outputs structured JSON feedback for easy integration
- Works with Claude Desktop, Claude Code, Cursor, and compatible tools

## Usage

1. Paste copy or upload a screenshot into your tool.
2. Trigger the skill: `"Review this copy for Sticklight style."`
3. Receive structured issues + a fully rewritten version.

## Data files

- `data/glossary.json` — approved terms, avoided terms, usage rules
- `data/writing-guidelines.json` — voice, tone, grammar, and UX writing rules
