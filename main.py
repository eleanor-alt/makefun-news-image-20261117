"""Entry for make.fun 'Sum up 17 November's world news in one image'.

Writes the pre-rendered news infographic held in this repository to
/output/entry.png. Deterministic, no network, standard library only.
The image bytes are verified against the competition's gate (PNG magic,
at most 1 MiB, at most 1024x1024) before they are written, and the write
is atomic: a partial file can never be graded.
"""
import os
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"
MAX_BYTES = 1_048_576
MAX_DIM = 1024


def verified_bytes() -> bytes:
    with open(SRC, "rb") as fh:
        data = fh.read()
    if len(data) > MAX_BYTES:
        raise ValueError(f"image is {len(data)} bytes, over the 1 MiB cap")
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        width, height = struct.unpack(">II", data[16:24])
        if width > MAX_DIM or height > MAX_DIM:
            raise ValueError(f"image is {width}x{height}, over 1024x1024")
    elif not data[:3] == b"\xff\xd8\xff":
        raise ValueError("image is neither PNG nor JPEG")
    return data


def main() -> None:
    data = verified_bytes()
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    tmp = DST + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(data)
    os.replace(tmp, DST)


if __name__ == "__main__":
    main()
