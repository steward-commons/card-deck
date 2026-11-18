# Nightly Backup (FG005) — how-to

A routine card. It's a practice, not a program.

## Set it up

1. Ask the owner where off-site copies should live (a cloud drive folder, a notes app, email to themselves, or a USB drive) and how big the folder can get.
2. Create a nightly routine (around 11 PM local works well) that:
   - writes a dated memory backup, for example `memory-YYYY-MM-DD.md`;
   - also saves a current snapshot if a pet program lives on the box (see [pixel-pet](https://github.com/steward-commons/pixel-pet));
   - copies the files to the owner's chosen off-site place when it's connected;
   - keeps the newest 30 dated backups and stays under the owner's size cap (1 GB is a sensible default).
3. Write a short restore guide next to the backups so a future assistant (or person) knows which file to open first.

## Rules

- Never put passwords, vault data, money info, or verification phrases in a backup.
- Private files stay out of any shared package.
- After a restore, rebuild the integrity baseline on the new box (see [house-defense](https://github.com/steward-commons/house-defense)).
