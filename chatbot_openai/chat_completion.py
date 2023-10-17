import openai
import time


start = time.time()
result = openai.ChatCompletion.create(
    model="gpt-4",
    max_tokens=256,
    temperature=0,
    messages = [
        {"role": "system", "content": "You are a content creater."},
        {"role": "user", "content": "create a blog about black holes, 100 words limit"},
    ],
    stream = True,
)


end = time.time()

answer = ""
for token in result:
#    print(token)
    print(token.choices[0].delta.get("content", ""), flush=True, end="")
    if "content" in token.choices[0].delta:
#        print(token.choices[0].delta.content)
        answer += token.choices[0].delta["content"]
#    answer += token.choices[0].delta["content"]
#for token in result:
    
#    if "content" in token.choices[0].delta:
#        print(token.choices[0].delta.content)
#        answer += token.choices[0].delta["content"]
print("\n answer:", answer) 
#print("\n time used: ",  end - start, "sec")
