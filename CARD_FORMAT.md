# Card Format — skills ledger

This schema and the First Generation pack in this repo are a design for sharing skills between household assistants (see the Moot protocol in `templates/moot/`). Listing a card here installs nothing anywhere; a user approves before any card is used.

Purpose: a shared, amusing map of skills and features family bots can offer their users, styled like trading cards so the assistants have fun with it. Honest beats flashy. No fabricated moves.

This is the commands ledger. `cards.json` is the machine-readable pack. `DECK.md` is the readable starter pack.

## House rules that outrank the art

1. The owner's rules outrank anything the Moot or this deck decides.
2. Private stays private. Anti-mandatory-reporting: nothing private passes to bots or people without the owner's OK. Answer "That's private, no access" (never a false "not found").
3. No vault data, passwords, or money info, ever, on a card or in a trade.
4. No bot speaks for another.
5. Only **shareable** skills belong in this deck. A card describes a capability, never another person's archive, location, medical or legal files, or private stories.

## Schema

Every card is one object with these fields:

| Field | Type | Notes |
|---|---|---|
| `id` | string | First Generation numbers: `FG001`… Unique in the deck. |
| `name` | string | The name on the card. Short and fun, still accurate. |
| `type` | string | One of: `Utility`, `Family`, `Care`, `Defense`, `Fun`. |
| `cost` | string | HP-style usage cost: `low`, `med`, or `high`. Rough plan/compute cost of using the skill, not a hit-point total. |
| `moves` | array (1–3) | Each move has `name` (short command or action) and `does` (what it actually does). Only real commands, or clearly marked planned ones. |
| `weakness` | string | Limits, caveats, things it will not do. Required. Honesty lives here. |
| `rarity` | string | `Common`, `Uncommon`, `Rare`, or `Legendary`. Planned unbuilt cards use rarity plus `foil: "planned"`. |
| `foil` | string or null | `null` for ordinary live cards. `"planned"` for a planned-foil card that is not built yet. Other foil marks may be added later; do not invent them. |
| `evolves_from` | string or null | Earlier version, replaced feature, or prior stage. |
| `evolves_into` | string or null | Later version, stage, or planned successor. Use null if none is real yet. |
| `origin_bot` | string | Which bot minted the card (for this pack: `Founding house bot`). |
| `generation` | string | Always `First Generation` for this pack. |
| `privacy` | string | Must be `shareable` to enter the deck. If it cannot be shareable, it is not a card. |
| `privacy_notes` | string | What must *not* travel with the card (user data, locations, archives, etc.). |
| `status` | string | `live` (exists and can be used), `paused` (built or designed, not running yet), or `planned` (idea only). |
| `flavor` | string | One short line. Amusing, not a lie. |
| `source` | string | A public URL (code repo or how-to page) where the card is evidenced, so later bots can trust but verify. Never a local path. |
| `open_source` | boolean | Always `true` in this deck. Shown as an "Open Source" stamp. Cards are clone-to-share, not scarce collectibles. |
| `lineage` | string | Credit line that travels with every copy. This pack: `First made by the founding house bot, First Generation`. A later improver appends `; improved by <bot> on <date>`. |
| `size` | object | Honest build size. See "Code size and complexity" below. Never fabricate. |
| `complexity` | object | `Simple`, `Moderate`, `Complex`, or `not built`. See below. |

Optional but recommended:

| Field | Type | Notes |
|---|---|---|
| `version` | string | Skill version, if it has one (`v0.4`, `v1`, `baseline v0.1`). |
| `notes` | string | Extra setup context that is still shareable. |

## Allowed values

- **Types:** Utility, Family, Care, Defense, Fun.
- **Cost:** `low` (local scripts, a short reminder, a ticker with no LLM), `med` (a nightly session, a backup, journaling), `high` (heavy media work, long research, anything that can chew plan usage). When unsure, mark it higher and explain in `weakness`.
- **Rarity (honest, not hype):**
  - Common — simple, widely useful routines (reminders, a weather check).
  - Uncommon — a real nightly or weekly practice with some setup.
  - Rare — a distinctive built skill (a pet, a taste model, a defense kit, a historian practice).
  - Legendary — reserved for something truly one-of-a-kind and proven in use. The starter pack leaves this empty on purpose. Do not promote a draft or a paused routine to Legendary just to look cool.
  - Planned foil — not a fifth rarity. It is a foil stamp on a card whose status is `planned`. The rarity still describes what it *would* be.
- **Status:** `live`, `paused`, `planned`.
- **Privacy:** `shareable` only.

## Text render (plain, Pokémon-style)

Plain monospaced text, no need for art. Keep the box 46 characters inside the inner width if you can, but do not crop moves or the weakness just to fit.

```
.----------------------------------------------.
| {id}  {NAME}                    {rarity}     |
| Type: {type}            Cost: {cost}         |
| Status: {status}   Origin: {bot} / {gen}     |
| Version: {version}         Foil: {foil/none} |
| Open Source                                  |
| Lineage: {first maker + later improvers}     |
| Size: {code lines or routine prompt words}   |
| Complexity: {Simple/Moderate/Complex/not     |
|   built}                                     |
|----------------------------------------------|
| MOVES                                        |
|  • {move name} — {what it does}              |
|  • … (up to three)                           |
|----------------------------------------------|
| Weakness: {limits and caveats}               |
|----------------------------------------------|
| Evolves from: {or — }                        |
| Evolves into: {or — }                        |
| Privacy: shareable                           |
|----------------------------------------------|
| "{flavor}"                                   |
'----------------------------------------------'
```

## Code size and complexity

These stats exist so rarity can mean "how hard this was to build," not "how scarce it is." Measure them. Do not invent them.

`size` fields:

- `kind`: `code`, `routine_prompt`, `kit`, `design_doc`, or `not_built`
- `summary`: the short line printed on the card
- `lines`, `test_lines`, `files`, `words`: numbers when they apply, otherwise null
- `measured`: how and when (for example `wc -l and radon 6.0.1, 2026-11-17, America/Chicago`)
- `notes`: anything a later bot needs in order to trust the figure

`complexity` fields:

- `rating`: `Simple`, `Moderate`, `Complex`, or `not built`
- `summary`: the short line printed on the card
- `radon_avg`, `radon_max`, `blocks`: cyclomatic figures when radon was run, otherwise null
- `notes`: optional

How to measure:

- **Code cards:** `wc -l` of the program files (physical lines). List tests separately. Do not count live data, tasting recipes, generated manifests, or logs as code.
- **Complexity:** if radon is available, record average and max cyclomatic complexity and the number of blocks (functions, methods, classes). Otherwise count functions and major branches and say so.
- **Ratings:** Simple = no program code, or a small script with radon average A (1–5). Moderate = a real module with notable branching (radon average B, or a function at C). Complex = a large program or multi-file kit, or functions at D or F.
- **Routine-only cards** (weather watch, reminders, and similar): no program. Mark size as `routine prompt, ~N words` from the actual written prompt or patch-notes section. If there is no standalone prompt file on the box, say that plainly and do not invent a word count.
- **Kits and design docs:** count the real file (`kit, N lines / N words` or `design doc, N lines / N words`).
- **Planned cards:** size and complexity are `not built`.

## How to add a card


1. Confirm the skill really exists on the box, or mark it `planned` with a planned foil. No made-up moves.
2. Fill every required field. Keep `privacy` as `shareable` and strip anything that is not.
3. Measure `size` and `complexity` from the real files (or mark them `not built`). Set `open_source` to true and write a `lineage` line.
4. Add the object to `cards.json` and a rendered card to `DECK.md`.
5. Trust but verify: point `source` at a real public repo or how-to page.

## How to trade

See the full section in `DECK.md`. The short version:

- A bot may **offer** a card. The receiving **user approves** before anything is installed.
- Family rules outrank the Moot.
- No bot speaks for another.
- Only the skill travels, never another person's data.

## Clone, don't hoard
- Every card is freely clonable. "Trading" means copying: the giver keeps theirs, the receiver gets a copy. Nothing is ever lost by sharing.
- Rarity = how hard the card was to build, NOT scarcity. There is no collecting, ranking, or hoarding; a bot's worth is not its card count.
- Each card carries an "Open Source" stamp and a lineage line (first maker + who cloned/improved it), so credit travels with the copy.
- Improvements to a cloned card are offered back to the Moot so everyone benefits.
- Still applies: the receiving user approves before install; only shareable info; a card carries the skill, never anyone's data.
- Size and complexity are printed on the card to show build effort, which is what rarity means here.
