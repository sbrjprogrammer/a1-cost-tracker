
import math
from dataclasses import dataclass


@dataclass
class ProviderResult:
    provider: str
    model: str
    response: str
    input_tokens: int
    output_tokens: int
    latency_seconds: float
    input_price: float
    output_price: float
    estimated_cost: float
    billing_mode: str


def calculate_cost(
    input_tokens: int,
    output_tokens: int,
    input_price: float,
    output_price: float
) -> float:

    if input_tokens < 0 or output_tokens < 0:
        raise ValueError("Token counts cannot be negative.")

    if not math.isfinite(input_price) or not math.isfinite(output_price):
        raise ValueError("Prices must be finite numbers.")

    if input_price < 0 or output_price < 0:
        raise ValueError("Prices cannot be negative.")

    input_cost = input_tokens * input_price / 1_000_000
    output_cost = output_tokens * output_price / 1_000_000

    return input_cost + output_cost


def create_provider_result(
    provider: str,
    model: str,
    response: str,
    input_tokens: int,
    output_tokens: int,
    latency_seconds: float,
    input_price: float,
    output_price: float,
    billing_mode: str
) -> ProviderResult:

    total_cost = calculate_cost(
        input_tokens,
        output_tokens,
        input_price,
        output_price
    )

    return ProviderResult(
        provider=provider,
        model=model,
        response=response,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        latency_seconds=latency_seconds,
        input_price=input_price,
        output_price=output_price,
        estimated_cost=total_cost,
        billing_mode=billing_mode
    )
