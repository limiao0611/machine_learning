import openai

my_messages = [
        {"role": "system", "content": "You are a content creater."},
        {"role": "user", "content": "create a blog about black holes, 100 words limit"},
 ]

print("initial_prompts:", my_messages)

val = "hello"
while (val != "exit"):
    result = openai.ChatCompletion.create(
    	model = "gpt-3.5-turbo-16k",
    	max_tokens = 256,
    	temperature = 0,
    	messages = my_messages,
    	stream = True
    	)

    answer = ""
    for token in result:
    	print(token.choices[0].delta.get("content", ""), flush=True, end="")
    	if "content" in token.choices[0].delta:
            answer += token.choices[0].delta["content"]
    my_messages.append(
		{"role": "assistant", "content": answer}
		)

    val = input("\n\n **** New Prompt ****:\n")

    my_messages.append(
		{"role": "user", "content": val}
		)

    #print("updated msg:", my_messages)
	
