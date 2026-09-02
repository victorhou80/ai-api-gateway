#!/usr/bin/env python3
"""Convert a relay C-value into token purchasing power.

C is the CNY paid for the amount of tokens whose official standard API
list-price value is USD 1. This script performs arithmetic only; it does not
endorse a relay, validate model authenticity, or establish upstream legality.
"""

from __future__ import annotations

import argparse


def positive_float(value: str) -> float:
    number = float(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return number


def share_float(value: str) -> float:
    number = float(value)
    if not 0 <= number <= 1:
        raise argparse.ArgumentTypeError("must be between 0 and 1")
    return number


def format_tokens(value: float) -> str:
    return f"{value:,.0f}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate tokens purchasable per CNY from a relay C-value."
    )
    parser.add_argument(
        "--c",
        type=positive_float,
        required=True,
        help="CNY paid for USD 1 of official standard list-price usage",
    )
    parser.add_argument(
        "--input-price",
        type=positive_float,
        required=True,
        help="official input price in USD per 1M tokens",
    )
    parser.add_argument(
        "--output-price",
        type=positive_float,
        required=True,
        help="official output price in USD per 1M tokens",
    )
    parser.add_argument(
        "--input-share",
        type=share_float,
        default=0.9,
        help="input share of total tokens, from 0 to 1 (default: 0.9)",
    )
    args = parser.parse_args()

    official_usd_power = 1 / args.c
    input_tokens = 1_000_000 / (args.c * args.input_price)
    output_tokens = 1_000_000 / (args.c * args.output_price)
    mixed_price = args.c * (
        args.input_share * args.input_price
        + (1 - args.input_share) * args.output_price
    )
    mixed_tokens = 1_000_000 / mixed_price

    print(f"C value: CNY {args.c:.6g} per official USD 1 of usage")
    print(f"Official list-price purchasing power per CNY: USD {official_usd_power:.6f}")
    print(f"Input tokens per CNY:  {format_tokens(input_tokens)}")
    print(f"Output tokens per CNY: {format_tokens(output_tokens)}")
    print(
        "Mixed tokens per CNY "
        f"({args.input_share:.0%} input / {1-args.input_share:.0%} output): "
        f"{format_tokens(mixed_tokens)}"
    )
    print(f"Token multiple versus C=1.00: {1 / args.c:.4f}x")
    print(f"Token multiple versus C=0.68: {0.68 / args.c:.4f}x")


if __name__ == "__main__":
    main()
