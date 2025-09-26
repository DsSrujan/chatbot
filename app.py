import google.generativeai as genai
API_KEY="AIzaSyAJ9To6TWl968KMJVUv3cpyRDPGPz6g16Q"
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel("gemini-2.0-flash")
chat=model.start_chat()
print("Welcome to the Gemini 2.0 Flash Chatbot!")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    response = chat.send_message(user_input)
    print(f"Chatbot: {response.text}")  