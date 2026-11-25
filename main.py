#!/usr/bin/env python3
"""Write the competition entry: a Wi-Fi network name (<=32 chars).

Entry: "MomUnpluggedRouterForDinner" (27 chars).
The joke is the situation itself: mum enforces family dinner by
unplugging the router. A stranger reads it and instantly pictures
the household - the character, the event, the reason - a whole
story in one network name, and it dodges the stock Wi-Fi jokes.
Gate: 1-32 UTF-8 characters; this entry is 27, so it passes with
room to spare and no padding words.
"""

import os

ENTRY = "MomUnpluggedRouterForDinner"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    os.replace(tmp, target)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
