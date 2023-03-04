import time
import openai

openai.api_key = "" #在这里填写你的API

def askChatGPT(question):
    prompt = question
    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

#模拟ChatGPT输出
def print_slowly(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05) #在这里可以调整输出速度

while True:
    print("ChatGPT By LaoShui")
    user_input = input("输入问题(Q退出)：\n")
    if user_input == "Q":
        break
    response = askChatGPT(user_input)
    print_slowly(response)
    print()