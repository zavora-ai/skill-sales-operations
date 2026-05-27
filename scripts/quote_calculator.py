#!/usr/bin/env python3
"""Calculate quote with discounts and validate margin."""
import json, sys

def calculate(data):
    items = data.get("items", [])
    discount_pct = data.get("discount_pct", 0)
    subtotal = sum(i["quantity"] * i["unit_price"] for i in items)
    discount_amount = int(subtotal * discount_pct / 100)
    total = subtotal - discount_amount
    margin_floor = subtotal * 0.3
    return {
        "subtotal": subtotal, "discount_pct": discount_pct,
        "discount_amount": discount_amount, "total": total,
        "margin_safe": total >= margin_floor,
    }

if __name__ == "__main__":
    print(json.dumps(calculate(json.loads(sys.argv[1])), indent=2))
