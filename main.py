# food-picture-01 entry (Python 3.13, standard library only).
#
# The picture is the entry.png beside this file (a JPEG-encoded image
# named entry.png, which the rules allow: PNG or JPEG is told apart by
# its first bytes). The program copies it to /output/entry.png.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
dst = os.path.join(out_dir, "entry.png")

shutil.copyfile(src, dst)
