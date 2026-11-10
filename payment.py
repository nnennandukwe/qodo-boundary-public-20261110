"""Synthetic payment-event producer. No real customer data."""

def capture(amount_cents: int, request_key: str) -> dict:
    return {"amount_cents": amount_cents, "request_key": request_key, "status": "captured"}
