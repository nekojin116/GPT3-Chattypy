import openai

# Function to generate a response for a given prompt and chat history
# using the specified OpenAI model
def generate_response(prompt, chat_history, model, temperature=0.5):
    # Concatenate the chat history and the prompt
    full_prompt = chat_history + "\n" + prompt
    
    # Use the Completion API to generate a response
    completions = openai.Completion.create(
        engine=model,
        prompt=full_prompt,
        temperature=temperature,
        max_tokens=1024,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Get the response text from the first completion choice
    message = completions.choices[0].text
    
    # Return the response
    return message

# Set the API key
openai.api_key = ""

# Initialize the chat history to an empty string
chat_history = ""

# Run the chatbot in a loop
while True:
    # Get user input
    user_input = input("User: ")
    
    # Generate a response using the generate_response function
    response = generate_response(prompt=user_input, chat_history=chat_history, model="text-davinci-002")
    
    # Print the chatbot's response
    print("Chatbot: " + response)
    
    # Update the chat history with the user's message and the chatbot's response
    chat_history += "\n" + user_input + "\n" + response
