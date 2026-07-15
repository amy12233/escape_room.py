# ─────────────────────────────────────────────────────────────
# SDE Escape Room
#
# This file grows across SDE lessons 5–9 and is polished in L10.
#   L5  Input & If/Else      — print intro + ask the player's name
#   L6  Random & While Loops — random rooms + a main game loop
#   L7  2D Maps & Movement   — grid map + N/S/E/W movement
#   L8  Puzzle Functions     — refactor puzzles into functions + walls
#   L9  Final Customization  — theme, story, win/lose screens
#   L10 Polish & Stretch     — pick from key item, time limit,
#                              hunger, math puzzle, etc.
#
# Keep working in this single file unless your instructor says
# otherwise. Save often — your work persists between lessons.
# ─────────────────────────────────────────────────────────────

print("Welcome to the Escape Room!")
# TODO (L5): ask the player for their name and greet them.
name = input("What is your name? ")
print(f"Welcome, {name}!")

print("You see three doors. Which do you open?")
door = input("Pick a door (1, 2, or 3): ")

if door == "2":
    print("You escaped!")
else:
    print("The door is locked. Try again next run.")
