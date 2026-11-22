
import os
import time

from google import genai

from .cost_calculator import create_provider_result


def call_gemini(prompt: str):
    model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

    input_price = float(os.getenv("GEMINI_INPUT_PRICE", "0.30"))
    output_price = float(os.getenv("GEMINI_OUTPUT_PRICE", "2.50"))

    billing_mode = os.getenv("GEMINI_BILLING_MODE", "free")

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or api_key == "your_gemini_api_key":
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Please add your Gemini API key to the .env file."
        )

    client = genai.Client(api_key=api_key)

    start_time = time.perf_counter()

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    end_time = time.perf_counter()

    usage = response.usage_metadata

    if usage is None:
        raise RuntimeError(
            "Gemini did not return token usage metadata."
        )

    input_tokens = usage.prompt_token_count or 0
    output_tokens = usage.candidates_token_count or 0

    return create_provider_result(
        provider="Google Gemini",
        model=model,
        response=response.text or "",
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        latency_seconds=end_time - start_time,
        input_price=input_price,
        output_price=output_price,
        billing_mode=billing_mode
    )
