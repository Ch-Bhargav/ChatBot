import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
import os 

_ = load_dotenv(find_dotenv())

genai.configure(
api_key = os.environ.get('API_KEY')
)

try:
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
except Exception as e:
    print(f"Error initializing the model: {e}")
    exit(1)  

while True:
    print("\nMenu:")
    print("1. Enter Chat")
    print("2. Exit")
    
    try:
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice not in ['1', '2']:
            raise ValueError("Invalid choice. Please enter 1 or 2.")
        
        if choice == '2':
            print("Exiting the chat. Goodbye!")
            break  
        
        if choice == '1':
            print("Type 'exit' to leave the chat and return to the main menu.")
            while True:
                try:
                    question = input("You: ").strip()
                    if question.lower() == 'exit':
                        print("Returning to the main menu.")
                        break  
                    
                    if not question:
                        raise ValueError("Input cannot be empty or just whitespace.")
                    
                    response = chat.send_message(question)
                    print(f"AI: {response.text}")
                except ValueError as ve:
                    print(f"Input Error: {ve}")
                except Exception as e:
                    print(f"Error during chat interaction: {e}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")