import sys
import os
from glob import glob

# usage: python make_txt.py <path/to/folder> <output.txt>

if len(sys.argv) < 3:
    exit(1)

folder = sys.argv[1]
out_file = sys.argv[2]

with open(out_file, "w") as f:
    f.write('\n'.join(glob(os.path.join(folder, "*.jpg"))))
