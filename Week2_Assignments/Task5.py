#Task 5: Real-World Mini Project            

#ai_prompt_logger.py simulation

#5.1 Accepts a user input (simulating an AI prompt). 

import datetime
print("\n AI Prompt Logger")
prompt = input("Enter ur AI prompt: ")


#5.2. Saves the prompt text in a file named prompt_history.txt.
#5.3. Each time you run the program, new prompts are appended with timestamps.
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Open file in append mode to save prompt with timestamp
with open("prompt_history.txt", "a") as file:
    file.write("[" + timestamp + "] " + prompt + "\n")

print("Prompt saved successfully to prompt_history.txt!")
            
        
    
