# Program 8 — File Operations

""" Create function save_note(title, content):
- Saves to "my_notes.txt"
- Format: "TITLE: x | CONTENT: x\n"
- Append mode

Create function read_notes():
- Reads and prints all notes
- Handles FileNotFoundError

Call save_note() 3 times
Call read_notes() once """

def save_note(title, content):
	
	file = open("my_notes.txt", "a")
	
	file.write(f"TITLE: {title} | CONTENT: {content}\n")
	
	file.close()
	

def read_notes():
	
	try :
		
		file = open("my_notes.txt", "r")
		content = file.read()
		print(content)
		file.close()
		
	except FileNotFoundError :
		print("File Not Found")
		
save_note("College", "Morning 7AM to Afternoon 12:30PM")
save_note("Vacation", "Trip to Dwaraka")
save_note("Dinner", "Paneer Tikka Masala")

read_notes()