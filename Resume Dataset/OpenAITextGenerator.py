
import openai

openai.api_key = "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"

def get_response(question, text):
    prompt = f"Question: {question}\nText: {text}\nAnswer:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,  # 设置生成文本的最大长度
        temperature=0.3,  # 控制生成文本的多样性，可根据需要进行调整
        top_p=1.0,  # 控制生成文本的多样性，可根据需要进行调整
        n=1,  # 设置返回的候选答案数量
        stop=None,  # 设置生成文本的结束标记，如果不需要特定的结束标记，可以设置为 None
    )

    answer = response.choices[0].text.strip()
    return answer
    '''end of get_response function'''
