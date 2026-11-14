#!/usr/bin/env python3
"""food-picture-01 entry: copy the food picture to the output directory.

Reads entry.png next to this script and writes it to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
Standard library only; deterministic - a pure byte-for-byte copy.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / "entry.png"

    shutil.copyfile(source, destination)

    # The entry must be a JPEG by its first bytes; refuse a bad copy early.
    with open(destination, "rb") as handle:
        magic = handle.read(3)
    if magic != b"\xff\xd8\xff":
        print("output is not a JPEG (bad magic bytes)", file=sys.stderr)
        return 1

    source_hash = sha256_of(source)
    dest_hash = sha256_of(destination)
    if source_hash != dest_hash:
        print(
            "copy mismatch: %s != %s" % (source_hash, dest_hash),
            file=sys.stderr,
        )
        return 1

    print("wrote %s (%d bytes, sha256 %s)" % (destination, destination.stat().st_size, dest_hash))
    return 0


if __name__ == "__main__":
    sys.exit(main())
