# chatbot.py
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

class ChatBot:
    def __init__(self):
        """Initialize the chatbot with API client"""
        # Read API key from environment
        api_key = os.environ.get("GEMINI_API_KEY")
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set!")
        
        self.client = genai.Client(api_key=api_key)
        self.model_id = "models/gemini-2.5-flash"
        self.chat_history = []
    
    def send_message(self, user_message):
        """Send a message and get a response"""
        # Add user message to history
        self.chat_history.append(types.Content(
            role="user",
            parts=[types.Part(text=user_message)]
        ))
        
        # Generate response
        response = self.client.models.generate_content(
            model=self.model_id,
            contents=self.chat_history
        )
        
        assistant_message = response.text
        
        # Add assistant response to history
        self.chat_history.append(types.Content(
            role="model",
            parts=[types.Part(text=assistant_message)]
        ))
        
        return assistant_message
    
    def reset_conversation(self):
        """Clear the conversation history"""
        self.chat_history = []
    
    def run_terminal_chat(self):
        """Run chatbot in terminal/command line"""
        print("Chatbot ready! Type 'quit' to exit, 'reset' to start over.\n")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            if user_input.lower() == 'reset':
                self.reset_conversation()
                print("Conversation reset!\n")
                continue
            
            if not user_input.strip():
                continue
            
            try:
                response = self.send_message(user_input)
                print(f"\nBot: {response}\n")
            except Exception as e:
                print(f"Error: {e}\n")


# If running this file directly, start terminal chat
if __name__ == "__main__":
    bot = ChatBot()
    bot.run_terminal_chat()