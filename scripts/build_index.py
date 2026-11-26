#!/usr/bin/env python3
"""Valida games/*.json e regenera index.json + index.sha256."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--check", action="store_true",
                        help="falha se index.json estiver desatualizado (usado no CI)")
    args = parser.parse_args()
    root = Path(args.root)

    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "translate-deck" / "core" / "src"))
    try:
        from tdeck_core.catalog import CatalogError, load_catalog, write_index
    except ImportError:
        print("erro: instale tdeck-core (pip install -e ../translate-deck/core)", file=sys.stderr)
        return 2

    try:
        games = load_catalog(root)
    except CatalogError as exc:
        print(f"catalogo invalido:\n{exc}", file=sys.stderr)
        return 1

    if args.check:
        expected, _ = write_index(root, root / ".tdeck-index")
        current = root / "index.json"
        if not current.is_file() or current.read_bytes() != expected.read_bytes():
            print("index.json desatualizado: rode scripts/build_index.py", file=sys.stderr)
            return 1
        print(f"ok: {len(games)} jogos, indice em dia")
        return 0

    index, digest = write_index(root, root)
    print(json.dumps({"games": len(games),
                      "translations": sum(len(g.translations) for g in games),
                      "index": str(index), "sha256": digest.read_text().strip()},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
