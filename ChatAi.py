import requests
import json


API_KEY = "use_your_own_Api-key" 

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

messages = [
    {"role": "system", "content": "You are a helpful and concise assistant."}
]

while True:
    user_input = input("Enter your message!: ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": messages
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    if "choices" in response_data:
        ai_reply = response_data["choices"][0]["message"]["content"]
        print("AI:", ai_reply)
        messages.append({"role": "assistant", "content": ai_reply})
    else:
        print("AI: Sorry, something went wrong.")