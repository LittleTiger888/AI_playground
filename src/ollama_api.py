from openai import OpenAI

# ============================================================
# Available models (from Open WebUI /api/models)
# Uncomment ONE line below to select the active model
# ============================================================

MODEL = "huihui_ai/Qwen3.8-abliterated:latest"   # 27.3B, Q4_K_M, 262144 ctx - tools, vision, thinking
# MODEL = "dolphin-mixtral:8x7b"                  # 46.7B, Q4_0, 32768 ctx  - completion only
# MODEL = "llama2-uncensored:70b"                 # 65B,   Q4_0, 2048 ctx   - completion only
# MODEL = "llama3.1:70b"                          # 70.6B, Q4_K_M, 131072 ctx - tools
# MODEL = "dolphin-llama3:70b"                    # 71B,   Q4_0, 8192 ctx   - completion only
# MODEL = "llama3.2:1b"                           # 1.2B,  Q8_0, 131072 ctx - tools, fast/lightweight

OPENWEBUI_HOST = 'http://100.97.219.49:3000'
OPENWEBUI_API_KEY = 'sk-c425322e3cdc47e1884a2dd995c5deea'

openai_client = OpenAI(
    base_url=f'{OPENWEBUI_HOST}/api',
    api_key=OPENWEBUI_API_KEY,
)


def ollama_generate_api(model_name, prompt):
    print('*'*10, f'Generating code using model {model_name}', '*'*10)
    response = openai_client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )
    return response.choices[0].message.content


def ollama_chat_api(model_name, system_prompt, user_prompt, seed=42):
    print("=>=>=> TTTTTHHHHHE SEED IS", seed)
    print('\n\n')
    print('*'*10, f'Generating with {model_name}', '*'*10)
    print('\n\n')
    response = openai_client.chat.completions.create(
        model=model_name,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt},
        ],
        temperature=0.8,   # default 0.8
        top_p=0.9,         # default 0.9
        seed=seed,
        stream=False,
        extra_body={'top_k': 40},  # default 40 - passed through if supported by Open WebUI/Ollama backend
    )
    return response.choices[0].message.content


def ollama_openai_chat_api(openai_client, model_name, system_prompt, user_prompt):
    print('*'*10, f'Generating with {model_name}', '*'*10)

    response = openai_client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        stream=False
    )
    return response.choices[0].message.content


def print_model_names():
    models = openai_client.models.list()
    for model in models.data:
        print(model.id)
