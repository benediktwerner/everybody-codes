#!/usr/bin/env python3

from __future__ import annotations

import re
from os import path


def point_to_length(x: int, y: int) -> int:
    return x + y - 1


def point_to_pos(x: int, y: int) -> int:
    return x - 1


def pos_to_point(pos: int, length: int) -> tuple[int, int]:
    # x = pos + 1
    # length = x + y - 1
    # length = pos + y
    # y = length - pos
    return pos + 1, length - pos


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    result = 0
    for line in f.read().splitlines():
        x, y = map(int, re.findall(r"\d+", line))
        length = point_to_length(x, y)
        pos = point_to_pos(x, y)
        pos = (pos + 100) % length
        x, y = pos_to_point(pos, length)
        result += x + 100 * y
    print(result)
