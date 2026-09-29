#!/usr/bin/env python3
"""Skin overlay helpers. No live host."""
import os
import shutil
import tempfile
import unittest

import skin


class SkinTests(unittest.TestCase):
    def setUp(self):
        self.skins = tempfile.mkdtemp(prefix="skins-")
        self.state = tempfile.mkdtemp(prefix="crypt-")
        self.old_skins = skin.SKINS_DIR
        self.old_state = skin.STATE_DIR
        self.old_file = skin.STATE_FILE
        skin.SKINS_DIR = self.skins
        skin.STATE_DIR = self.state
        skin.STATE_FILE = os.path.join(self.state, "skin.json")
        for name, body in (
            ("stock", "/* stock */\n"),
            ("halloween", ":root { --ember: #ff6a00; }\n"),
            ("sports", ":root { --ember: #d4af37; }\n"),
            ("la-rams", "/* skin: LA Rams */\n:root { --ember: #ffd100; }\n"),
            ("lv-raiders", "/* skin: Las Vegas Raiders */\n:root { --ember: #a5acaf; }\n"),
            ("phi-eagles", "/* skin: Philadelphia Eagles */\n:root { --ember: #acc0c6; }\n"),
            ("dal-cowboys", "/* skin: Dallas Cowboys */\n:root { --ember: #869397; }\n"),
        ):
            with open(os.path.join(self.skins, name + ".css"), "w") as fh:
                fh.write(body)
        with open(os.path.join(self.skins, "active"), "w") as fh:
            fh.write("stock\n")

    def tearDown(self):
        skin.SKINS_DIR = self.old_skins
        skin.STATE_DIR = self.old_state
        skin.STATE_FILE = self.old_file
        shutil.rmtree(self.skins, ignore_errors=True)
        shutil.rmtree(self.state, ignore_errors=True)

    def test_default_stock(self):
        self.assertEqual(skin.current(), "stock")
        snap = skin.snapshot()
        ids = [row["id"] for row in snap["skins"]]
        self.assertEqual(ids, ["dal-cowboys", "halloween", "la-rams", "lv-raiders", "phi-eagles", "sports", "stock"])
        labels = {row["id"]: row["label"] for row in snap["skins"]}
        self.assertEqual(labels["dal-cowboys"], "Dallas Cowboys")
        self.assertEqual(labels["la-rams"], "LA Rams")
        self.assertEqual(labels["lv-raiders"], "Las Vegas Raiders")
        self.assertEqual(labels["phi-eagles"], "Philadelphia Eagles")
        self.assertEqual(labels["halloween"], "Halloween")

    def test_apply_halloween(self):
        ok, err = skin.apply("halloween")
        self.assertTrue(ok, err)
        self.assertEqual(skin.current(), "halloween")
        css = skin.css_bytes().decode("utf-8")
        self.assertIn("#ff6a00", css)

    def test_rejects_path(self):
        ok, err = skin.apply("../etc")
        self.assertFalse(ok)
        self.assertTrue(err)
        self.assertEqual(skin.current(), "stock")

    def test_ship_default_file(self):
        with open(os.path.join(self.skins, "active"), "w") as fh:
            fh.write("sports\n")
        self.assertEqual(skin.current(), "sports")


if __name__ == "__main__":
    unittest.main()
