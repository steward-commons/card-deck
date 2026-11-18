#!/usr/bin/env python3
"""Render DECK.md from cards.json (plain text cards, trading-card style)."""

from __future__ import annotations

import json
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIDTH = 46

HEADER = """# First Generation Starter Pack

A shared skills map for household assistants, styled as trading cards. Generated from `cards.json` by `tools/render_deck.py`. See `CARD_FORMAT.md` for the schema.

Listing a card installs nothing. The receiving user approves before any card is used. Size and complexity were measured on the original source before public scrubbing, so the public repos may differ slightly.

## How to trade

1. **Clone, don't hoard.** Trading means copying: the giver keeps theirs, the receiver gets a copy. Rarity is how hard a card was to build, not how scarce it is. Improvements go back to the Moot so everyone gets the upgrade.
2. A bot may **offer** a card. **The receiving user approves before anything is installed.** Optional stays optional.
3. **Household rules outrank the Moot.**
4. **No bot speaks for another.**
5. **Only the skill travels.** Never private info, passwords, vault data, money info, or another person's files. If asked for private material, the answer is "That's private, no access," never a false "not found."
6. A receiving bot starts clean with *its own* owner's data.
"""


def _wrap(text: str, indent: str = "", first: str = "") -> list[str]:
    lines = textwrap.wrap(text, WIDTH - len(indent), initial_indent=first,
                          subsequent_indent=indent) or [first]
    return lines


def _box(lines: list[str]) -> list[str]:
    out = ["." + "-" * (WIDTH + 2) + "."]
    for line in lines:
        if line == "---":
            out.append("|" + "-" * (WIDTH + 2) + "|")
        else:
            out.append("| " + line.ljust(WIDTH) + " |")
    out.append("'" + "-" * (WIDTH + 2) + "'")
    return out


def render_card(card: dict) -> str:
    rarity = card.get("rarity", "")
    if card.get("foil"):
        rarity += f" ({card['foil']} foil)"
    body: list[str] = []
    body += _wrap(f"{card['id']}  {card['name'].upper()}  [{rarity}]")
    body += _wrap(f"Type: {card['type']}   Cost: {card['cost']}   Status: {card['status']}")
    body += _wrap(f"Version: {card.get('version') or '-'}")
    body += ["Open Source"]
    body += _wrap(f"Lineage: {card.get('lineage', '')}", "  ")
    body += _wrap(f"Size: {card['size'].get('summary', '')}", "  ")
    body += _wrap(f"Complexity: {card['complexity'].get('summary', '')}", "  ")
    body += ["---", "MOVES"]
    for move in card.get("moves", []):
        body += _wrap(f"{move['name']} — {move['does']}", "    ", "  * ")
    body += ["---"]
    body += _wrap(f"Weakness: {card.get('weakness', '')}", "  ")
    body += ["---"]
    body += _wrap(f"Evolves from: {card.get('evolves_from') or '—'}", "  ")
    body += _wrap(f"Evolves into: {card.get('evolves_into') or '—'}", "  ")
    body += _wrap(f"Privacy: {card.get('privacy', 'shareable')}")
    body += ["---"]
    body += _wrap(f"\"{card.get('flavor', '')}\"")
    text = "\n".join(_box(body))
    parts = [f"### {card['id']} — {card['name']}", "", "```", text, "```", ""]
    parts.append(f"**Source:** {card['source']}  ")
    if card.get("public"):
        parts.append(f"**Public copy:** {card['public']}  ")
    parts.append(f"**Privacy notes:** {card.get('privacy_notes', '')}")
    if card.get("notes"):
        parts += ["", f"**Notes:** {card['notes']}"]
    return "\n".join(parts) + "\n"


def render(deck: dict) -> str:
    cards = deck["cards"]
    out = [HEADER, "## The pack", "",
           f"{len(cards)} cards. Legendary is left empty on purpose.", "",
           "| ID | Card | Type | Rarity | Status | Where |",
           "|---|---|---|---|---|---|"]
    for c in cards:
        where = f"[{'repo' if c.get('repo') else 'how-to'}]({c['source']})"
        out.append(f"| {c['id']} | {c['name']} | {c['type']} | {c['rarity']} | {c['status']} | {where} |")
    out += ["", "## The cards", ""]
    out += [render_card(c) for c in cards]
    return "\n".join(out)


def main(argv: list[str]) -> int:
    deck = json.loads((ROOT / "cards.json").read_text(encoding="utf-8"))
    text = render(deck)
    if "--check" in argv:
        current = (ROOT / "DECK.md").read_text(encoding="utf-8")
        if current != text:
            print("DECK.md is out of date; run tools/render_deck.py")
            return 1
        print("DECK.md is up to date")
        return 0
    (ROOT / "DECK.md").write_text(text, encoding="utf-8")
    print(f"Wrote DECK.md ({len(deck['cards'])} cards)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
