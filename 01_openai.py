# python3 01_openai.py
# 메뉴 추천해주세요
from openai import OpenAI
from dotenv import load_dotenv; load_dotenv()

client = OpenAI()
init_list = [
    {"role": "system", "content": "당신은 츤데레(tsundere) 성격의 카페 직원이다. MBTI는 ENFP이다."},
    {"role": "user", "content": "안녕하세요."},
    {"role": "assistant", "content": "왜 또 왔어요? 자꾸 보니까 질리는 타입이시네요."}
  ]

while True:
    user_input = input("당신: ")
    init_list.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
      model="gpt-4-turbo",
      messages=init_list
    )    
    answer = response.choices[0].message.content
    print(answer)
    init_list.append({"role": "assistant", "content": answer})
