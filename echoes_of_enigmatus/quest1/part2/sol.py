#!/usr/bin/env python3

import re
from os import path


def eni(n: int, exp: int, mod: int) -> int:
    score = pow(n, exp - 5, mod)
    remainders = []
    for _ in range(5):
        score = (score * n) % mod
        remainders.append(score)
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
