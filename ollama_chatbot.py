import requests
import json

# Local Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/chat"

# Initialize conversation history
history = []

print("🤖 Ollama Chatbot (Mistral) is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break

    # Add user's message to history
    history.append({"role": "user", "content": user_input})

    # Send request to Ollama
    response = requests.post(OLLAMA_URL, json={
        "model": "mistral",
        "messages": history,
        "stream": False  # Set to True if using stream processing
    })

    try:
        # Manually parse the first JSON object in case of extra data
        json_objects = response.text.strip().split('\n')
        first_json = json.loads(json_objects[0])
        reply = first_json['message']['content']
        
        print("Bot:", reply)
        history.append({"role": "assistant", "content": reply})

    except json.JSONDecodeError as e:
        print("❌ JSON Decode Error:", e)
        print("Raw response:\n", response.text)
        break
