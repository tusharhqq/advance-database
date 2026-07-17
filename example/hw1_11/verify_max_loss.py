#!/usr/bin/env python3
"""HW1 Q11 reference: max loss = min_{i<j}(price_j - price_i) per ID."""

from __future__ import annotations

import csv
import sys
from collections import defaultdict
from pathlib import Path


def max_loss_by_id(rows: list[tuple[str, int, float]]) -> dict[str, float]:
    by_id: dict[str, list[tuple[int, float]]] = defaultdict(list)
    for sid, date, price in rows:
        by_id[sid].append((date, price))

    out: dict[str, float] = {}
    for sid, items in by_id.items():
        items.sort(key=lambda t: t[0])
        prices = [p for _, p in items]
        if len(prices) < 2:
            out[sid] = 0.0
            continue
        running_max = prices[0]
        worst = float("inf")
        for p in prices[1:]:
            loss = p - running_max
            if loss < worst:
                worst = loss
            if p > running_max:
                running_max = p
        out[sid] = worst if worst != float("inf") else 0.0
    return out


def load_csv(path: Path) -> list[tuple[str, int, float]]:
    rows: list[tuple[str, int, float]] = []
    with path.open() as f:
        for row in csv.DictReader(f):
            rows.append(
                (
                    row["ID"],
                    int(row["date"]),
                    float(row["endofdayprice"]),
                )
            )
    return rows


def main() -> None:
    path = Path(
        sys.argv[1]
        if len(sys.argv) > 1
        else Path(__file__).with_name("example_ticks.csv")
    )
    result = max_loss_by_id(load_csv(path))
    for sid in sorted(result):
        print(f"Worst loss for {sid} is {result[sid]:g}")


if __name__ == "__main__":
    main()
