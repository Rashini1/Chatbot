from groq import Groq

# Initialize the client with your Groq API key
client = Groq(api_key=" ")

def chat():
    print("🤖 Llama Chatbot (Free via Groq): Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("🤖 Chatbot: Goodbye!")
            break

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Free model from Groq
            messages=[
                {"role": "system", "content": "You are a friendly AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        print("🤖 Chatbot:", response.choices[0].message.content)

if __name__ == "__main__":
    chat()
