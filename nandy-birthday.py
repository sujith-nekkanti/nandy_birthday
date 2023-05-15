import random
from PIL import Image
import tkinter as tk

# Create the questions and answers
questions = [
  "What is the capital of France?",
  "What is the name of the largest ocean in the world?",
  "What is the chemical symbol for gold?"
]
answers = [
  "Paris",
  "The Pacific Ocean",
  "Au"
]

# Create the jigsaw puzzle
puzzle_image = "IMG20230505161453.jpg"
puzzle_pieces = []
for i in range(16):
  puzzle_piece = Image.open(puzzle_image)
  puzzle_pieces.append(puzzle_piece)

# Create the game window
window = tk.Tk()
window.title("Puzzle Game")

# Create the start button
start_button = Button(window, text="Start", command=start_game)
start_button.pack()

# Create the hint button
hint_button = Button(window, text="Hint", command=get_hint)
hint_button.pack()

# Create the jigsaw puzzle canvas
puzzle_canvas = Canvas(window, width=400, height=400)
puzzle_canvas.pack()

# Create the jigsaw puzzle pieces
for i in range(16):
  puzzle_piece = puzzle_pieces[i]
  puzzle_canvas.create_image((i * 100, 0), image=puzzle_piece)

# Start the game
start_game()

# Define the start_game function
def start_game():
  # Clear the current level
  clear_level()

  # Set the current level
  current_level = 1

  # Display the question for the current level
  question_label = Label(window, text=questions[current_level - 1])
  question_label.pack()

  # Get the player's answer
  answer = input("What is the answer? ")

  # Check the player's answer
  if answer == answers[current_level - 1]:
    # The player answered correctly
    print("Correct!")
    # Advance to the next level
    current_level += 1
    start_game()
  else:
    # The player answered incorrectly
    print("Incorrect!")

# Define the clear_level function
def clear_level():
  # Clear the question label
  question_label.destroy()

  # Clear the answer label
  answer_label.destroy()

  # Clear the hint button
  hint_button.destroy()

  # Clear the jigsaw puzzle pieces
  for i in range(16):
    puzzle_canvas.delete("all")

# Define the get_hint function
def get_hint():
  # Display the hint for the current level
  hint_label = Label(window, text="Hint: " + hints[current_level - 1])
  hint_label.pack()

# Run the game
window.mainloop()
