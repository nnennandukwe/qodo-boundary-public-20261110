"""Synthetic payment-event producer. No real customer data."""

def capture(amount_cents: int, request_key: str) -> dict:
    return {"amount": amount_cents, "request_key": request_key, "status": "complete"}
