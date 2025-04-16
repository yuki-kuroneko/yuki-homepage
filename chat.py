from llama_cpp import Llama

# モデルのロード
llm = Llama(
    model_path="C:/LLMs/Llama-3-ELYZA-JP-8B-q4_k_m.gguf",  # ダウンロードしたモデルのパス
    chat_format="llama-3",  # Llama 3のフォーマット指定
    n_ctx=1024,  # コンテキストの長さ
)

# チャットのリクエスト
response = llm.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": "あなたは誠実で優秀な日本人のアシスタントです。特に指示が無い場合は、常に日本語で回答してください。",
        },
        {
            "role": "user",
            "content": "カワウソについて、教えてください。",
        },
    ],
    max_tokens=1024,  # 最大トークン数
)

# 結果の出力
print(response["choices"][0]["message"]["content"])


