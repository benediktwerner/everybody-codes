#!/usr/bin/env python3

import re
from os import path


def eni(n: int, exp: int, mod: int) -> int:
    score = 1
    remainders = []
    for _ in range(exp):
        score *= n
        remainders.append(score % mod)
    return int("".join(map(str, reversed(remainders))))


def compute(a: int, b: int, c: int, x: int, y: int, z: int, m: int) -> int:
    return eni(a, x, m) + eni(b, y, m) + eni(c, z, m)


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    print(
        max(
            compute(*map(int, re.findall(r"\d+", line)))
            for line in f.read().splitlines()
        )
    )
