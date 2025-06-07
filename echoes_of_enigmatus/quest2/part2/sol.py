#!/usr/bin/env python3

from __future__ import annotations

import re
from os import path
from dataclasses import dataclass


@dataclass
class Node:
    rank: int
    symbol: str
    left: Node | None = None
    right: Node | None = None

    def collect_messages(self, level: int, messages: list[str]) -> None:
        if level < len(messages):
            messages[level] += self.symbol
        else:
            messages.append(self.symbol)
        if self.left is not None:
            self.left.collect_messages(level + 1, messages)
        if self.right is not None:
            self.right.collect_messages(level + 1, messages)


def insert(root: Node | None, n: Node) -> Node:
    if root is None:
        return n
    if n.rank < root.rank:
        root.left = insert(root.left, n)
    else:
        root.right = insert(root.right, n)
    return root


def message(root: Node) -> str:
    messages = []
    root.collect_messages(0, messages)
    return max(messages, key=len)


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    left = None
    right = None

    id2nodes = {}

    for line in f.read().splitlines():
        if line.startswith("ADD"):
            id, left_rank, left_symbol, right_rank, right_symbol = re.findall(
                r"ADD id=(\d+) left=\[(\d+),(.)] right=\[(\d+),(.)]", line
            )[0]
            new_left = Node(int(left_rank), left_symbol)
            new_right = Node(int(right_rank), right_symbol)
            left = insert(left, new_left)
            right = insert(right, new_right)
            id2nodes[id] = (new_left, new_right)
        else:
            match = re.fullmatch(r"SWAP (\d+)", line)
            assert match is not None
            id = match.group(1)
            a, b = id2nodes[id]
            a.rank, b.rank = b.rank, a.rank
            a.symbol, b.symbol = b.symbol, a.symbol

    assert left is not None
    assert right is not None

    print(message(left) + message(right))
