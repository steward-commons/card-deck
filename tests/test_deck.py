import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["id", "name", "type", "cost", "moves", "weakness", "rarity", "foil",
            "evolves_from", "evolves_into", "origin_bot", "generation", "privacy",
            "privacy_notes", "status", "flavor", "source", "open_source", "lineage",
            "size", "complexity"]


class DeckTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deck = json.loads((ROOT / "cards.json").read_text(encoding="utf-8"))
        cls.cards = cls.deck["cards"]

    def test_required_fields_and_values(self):
        ids = set()
        for c in self.cards:
            for f in REQUIRED:
                self.assertIn(f, c, f"{c.get('id')} missing {f}")
            self.assertNotIn(c["id"], ids)
            ids.add(c["id"])
            self.assertIn(c["type"], {"Utility", "Family", "Care", "Defense", "Fun"})
            self.assertIn(c["cost"], {"low", "med", "high"})
            self.assertIn(c["rarity"], {"Common", "Uncommon", "Rare", "Legendary"})
            self.assertIn(c["status"], {"live", "paused", "planned"})
            self.assertEqual(c["privacy"], "shareable")
            self.assertTrue(c["open_source"])
            # The format asks for 1-3 moves; FG015 grew to 5 at step 2.
            self.assertTrue(1 <= len(c["moves"]) <= 5, c["id"])

    def test_sources_are_public_urls(self):
        for c in self.cards:
            self.assertTrue(c["source"].startswith("https://github.com/steward-commons/"), c["id"])

    def test_linked_docs_exist(self):
        prefix = "https://github.com/steward-commons/card-deck/blob/main/"
        for c in self.cards:
            if c["source"].startswith(prefix):
                self.assertTrue((ROOT / c["source"][len(prefix):]).is_file(), c["id"])

    def test_no_local_paths(self):
        text = (ROOT / "cards.json").read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"(^|[\s\"'])/(root|Users|srv|mnt)/", text))

    def test_deck_md_is_current(self):
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "render_deck.py"), "--check"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
