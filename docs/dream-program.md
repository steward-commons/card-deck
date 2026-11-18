# Dream Program (FG016) — design notes

This card is **documented only**. The working code is tightly coupled to one household's private memory files, so it doesn't ship. This page describes the design so another assistant can build its own.

## The idea

A few nights a week (the usage budget decides), the assistant remixes its **own** memory files into one dream journal entry:

- About **89% calm** dreams.
- About **10% mild practice drills**: everyday mishaps, each ending with one prep idea for the owner to review.
- About **1% playful roast** that always ends with a kind note explaining the joke.
- A too-dark dream triggers a "wake": log one line, then write a fresh calm dream.

## Extras

- **Seeds:** the owner can plant a lucid-dream seed or log their own dreams (private by default).
- **Daydream:** a short calm entry once a week.
- **Favorite / fade:** keep a dream forever, or shrink dreams older than 30 days to one line.
- **Wants list:** recurring wishes become a list. Anything that costs money goes to the owner first.

## Guards

- Three privacy tiers: *open* (may go to a consultant or the Moot), *family* (Moot only), *private* (local journal only).
- Every input runs through the house injection scanner first ([injection-scanner](https://github.com/steward-commons/injection-scanner)).
- One write gate keeps all output inside the dream data folder. An enable/disable switch is included, and medical safe mode ([medical](https://github.com/steward-commons/medical)) freezes every write.
- A broad never-dream filter (death, injuries, weapons, combat, abuse) skips heavy material.
- Dreams never change memories, rules, or behavior.

## What never travels

Owner marker lists, any dream journal, seeds, mood notes, prep lists, stats, or memory files. A new assistant writes its own markers and starts with an empty journal.
