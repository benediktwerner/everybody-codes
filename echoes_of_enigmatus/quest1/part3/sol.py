#!/usr/bin/env python3

import re
from os import path


def eni(n: int, exp: int, mod: int) -> int:
    result = 0
    score = 1
    remainders = {}
    for i in range(exp):
        score = (score * n) % mod
        if score in remainders:
            prev_i, prev_result = remainders[score]
            cycle = i - prev_i
            diff = result - prev_result
            div, rem = divmod(exp - i, cycle)
            return result + div * diff + eni(score, rem, mod)
        remainders[score] = (i, result)
        result += score
    return result


def compute(a: int, b: int, c: int, x: int, y: int, z: int, m: int) -> int:
    return eni(a, x, m) + eni(b, y, m) + eni(c, z, m)


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    print(
        max(
            compute(*map(int, re.findall(r"\d+", line)))
            for line in f.read().splitlines()
        )
    )
