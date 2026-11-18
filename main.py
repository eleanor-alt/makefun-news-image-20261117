"""Entry for make.fun 'Sum up 17 November's world news in one image'.

Writes the pre-rendered news infographic held in this repository to
/output/entry.png. Deterministic, no network, standard library only.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> None:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
