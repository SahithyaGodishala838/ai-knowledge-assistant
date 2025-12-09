from typing import Optional
from config import OPENAI_API_KEY, GEMINI_API_KEY, HF_API_TOKEN

# We use try/except so that missing libraries or keys don't crash the app.

# --- OpenAI ---
try:
    from openai import OpenAI
    openai_client: Optional[OpenAI] = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
except ImportError:
    openai_client = None

# --- Gemini ---
try:
    import google.generativeai as genai
    if GEMINI_API_KEY:
        genai.configure(api_key=GEMINI_API_KEY)
        gemini_model = genai.GenerativeModel("gemini-1.5-flash")
    else:
        gemini_model = None
except ImportError:
    gemini_model = None

# --- HuggingFace ---
try:
    from huggingface_hub import InferenceClient
    hf_client = InferenceClient(
        model="HuggingFaceH4/zephyr-7b-beta",
        token=HF_API_TOKEN
    ) if HF_API_TOKEN else None
except ImportError:
    hf_client = None


def generate_openai(prompt: str) -> str:
    if not openai_client:
        return "[OpenAI not configured – missing library or API key]"
    resp = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers based only on the given context."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=400,
    )
    return resp.choices[0].message.content.strip()


def generate_gemini(prompt: str) -> str:
    if not gemini_model:
        return "[Gemini not configured – missing library or API key]"
    resp = gemini_model.generate_content(prompt)
    return resp.text.strip()


def generate_hf(prompt: str) -> str:
    if not hf_client:
        return "[HuggingFace not configured – missing library or API token]"
    resp = hf_client.text_generation(
        prompt,
        max_new_tokens=256,
        temperature=0.4,
        do_sample=True,
    )
    return resp.strip()


def generate_local(prompt: str) -> str:
    """
    Local fallback – no external API required.
    For now, it just echoes a structured answer using the prompt/context.
    """
    header = "[Local generator – no API used]\n\n"
    return header + "Here is a response based on the provided context:\n\n" + prompt[:900]


def generate_with_provider(provider: str, prompt: str) -> str:
    provider = provider.lower()
    if provider == "openai":
        return generate_openai(prompt)
    if provider == "gemini":
        return generate_gemini(prompt)
    if provider == "huggingface":
        return generate_hf(prompt)
    if provider == "local":
        return generate_local(prompt)
    return "[Unknown provider. Use: openai, gemini, huggingface, or local]"
