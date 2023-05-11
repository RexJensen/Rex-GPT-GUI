import tkinter as tk
import openai
import threading
import time
import os

# OpenAI API key and initial conversation setup
openai.api_key = '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'
conversation = [{"role": "system", "content": "You are a helpful assistant."}]

def submit_input():
    user_input = user_entry.get()
    conversation.append({"role": "user", "content": user_input})
    conversation_text.insert(tk.END, f"You: {user_input}\n", "user")

    # Delete user input after submission
    user_entry.delete(0, tk.END)

    # Use threading to prevent GUI freezing
    thread = threading.Thread(target=get_response, args=())
    thread.start()

def get_response():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    assistant_response = response['choices'][0]['message']['content']
    conversation.append({"role": "assistant", "content": assistant_response})


    conversation_text.insert(tk.END, f"RexGPT: {assistant_response}\n", "assistant")

# Function to clear conversation
def clear_conversation():
    conversation_text.delete('1.0', tk.END)
    global conversation
    conversation = [{"role": "system", "content": "You are a helpful assistant."}]

# Create tkinter root window
root = tk.Tk()
root.title("RexGPT")
root.configure(background="red")

# Create user input field
user_entry = tk.Entry(root, width=50, font=("Helvetica", 14))

# Configure user input field
user_entry.configure(background="white")
user_entry.configure(foreground="black")

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_input, font=("Helvetica", 14))

# Create conversation text box
conversation_text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
conversation_text.tag_configure("user", foreground="blue")
conversation_text.tag_configure("assistant", foreground="orange")
conversation_text.configure(font=("Helvetica", 18))
conversation_text.configure(background="white")


# Create Clear, Save and Load buttons
clear_button = tk.Button(root, text="Clear Conversation", command=clear_conversation, font=("Helvetica", 14))

# Grid layout manager for better alignment
user_entry.grid(row=1, column=0, padx=20, pady=20)
submit_button.grid(row=1, column=1, padx=20, pady=20)
clear_button.grid(row=1, column=2, padx=20, pady=20)
conversation_text.grid(row=2, column=0, padx=20, pady=20, columnspan=3)

# Centering the buttons
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x-200, y))

# Running tkinter event loop
root.mainloop()


