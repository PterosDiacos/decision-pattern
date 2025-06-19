from openai import OpenAI

open_ai_key = ""

def get_simple_client():
    openai_client = OpenAI(api_key=open_ai_key)
    def oncall(**params):
        system_prompt = params.get("system_prompt", "")
        message = params.get("message", "")
        model = params.get("model", "gpt-4o")
        temperature = params.get("temperature", 1.0)
        max_tokens = params.get("max_tokens", 2000)

        response = openai_client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": message},
            ],
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        oncall.response = response
        return response.choices[0].message.content

    return oncall