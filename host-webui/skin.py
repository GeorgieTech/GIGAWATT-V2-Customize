#!/usr/bin/env python3
"""Web UI skins. Overlay CSS on crypt.css. Stdlib only."""
from __future__ import print_function

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SKINS_DIR = os.environ.get("CRYPT_SKINS", os.path.join(HERE, "skins"))
STATE_DIR = os.environ.get("CRYPT_STATE", "/data/crypt")
STATE_FILE = os.path.join(STATE_DIR, "skin.json")
DEFAULT = "stock"
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,31}$")


def _names():
    names = []
    try:
        for fn in sorted(os.listdir(SKINS_DIR)):
            if fn.endswith(".css") and NAME_RE.match(fn[:-4]):
                names.append(fn[:-4])
    except OSError:
        pass
    if DEFAULT not in names:
        names.insert(0, DEFAULT)
    return names


def _label(name):
    return str(name or "").replace("-", " ").title()


def _read_ship_default():
    path = os.path.join(SKINS_DIR, "active")
    try:
        with open(path, "r") as fh:
            name = (fh.read() or "").strip().split()[0].lower()
        if NAME_RE.match(name):
            return name
    except OSError:
        pass
    return DEFAULT


def _exists(name):
    return os.path.isfile(os.path.join(SKINS_DIR, name + ".css"))


def current():
    try:
        with open(STATE_FILE, "r") as fh:
            row = json.load(fh)
        name = str((row or {}).get("name") or "").strip().lower()
        if NAME_RE.match(name) and _exists(name):
            return name
    except (OSError, ValueError, TypeError):
        pass
    name = _read_ship_default()
    if _exists(name):
        return name
    return DEFAULT


def snapshot():
    name = current()
    return {
        "name": name,
        "label": _label(name),
        "skins": [{"id": n, "label": _label(n)} for n in _names()],
    }


def apply(name):
    name = str(name or "").strip().lower()
    if not NAME_RE.match(name):
        return False, "skin name is invalid"
    if not _exists(name):
        return False, "skin not found"
    try:
        os.makedirs(STATE_DIR, exist_ok=True)
        tmp = STATE_FILE + ".tmp"
        with open(tmp, "w") as fh:
            json.dump({"name": name}, fh)
            fh.write("\n")
        os.replace(tmp, STATE_FILE)
    except OSError as exc:
        return False, str(exc)
    return True, ""


def css_bytes():
    path = os.path.join(SKINS_DIR, current() + ".css")
    try:
        with open(path, "rb") as fh:
            return fh.read()
    except OSError:
        return b"/* stock */\n"
