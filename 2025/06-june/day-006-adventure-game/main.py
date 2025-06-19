import os
import platform
import sys

class Scene:
    def __init__(self, description, options, next_scenes):
        self.description = description
        self.options = options
        self.next_scenes = next_scenes

scenes = {
    "start": Scene(
        "You wake up in a mysterious room. The walls are made of cold stone, and there's a dim light coming from somewhere above. You notice two doors: one wooden and one metal.",
        {
            "1": "Try the wooden door",
            "2": "Try the metal door",
            "3": "Look around more carefully",
            "q": "Quit the game"
        },
        {
            "1": "wooden_door",
            "2": "metal_door",
            "3": "look_around",
            "q": "quit"
        }
    ),
    "wooden_door": Scene(
        "The wooden door creaks open to reveal a cozy library. Shelves of ancient books line the walls, and a comfortable armchair sits in the corner.",
        {
            "1": "Examine the books",
            "2": "Sit in the armchair",
            "3": "Go back",
            "q": "Quit the game"
        },
        {
            "1": "examine_books",
            "2": "sit_armchair",
            "3": "start",
            "q": "quit"
        }
    ),
    "metal_door": Scene(
        "The metal door leads to a high-tech laboratory. Strange machines blink and hum all around you.",
        {
            "1": "Investigate the machines",
            "2": "Look for a computer",
            "3": "Go back",
            "q": "Quit the game"
        },
        {
            "1": "investigate_machines",
            "2": "find_computer",
            "3": "start",
            "q": "quit"
        }
    ),
    "look_around": Scene(
        "As you look more carefully, you notice a small note on the floor and strange symbols carved into the walls.",
        {
            "1": "Read the note",
            "2": "Study the symbols",
            "3": "Go back",
            "q": "Quit the game"
        },
        {
            "1": "read_note",
            "2": "study_symbols",
            "3": "start",
            "q": "quit"
        }
    ),
    "examine_books": Scene(
        "You find a mysterious book about parallel universes. It seems to contain important information.",
        {"1": "Go back to the library", "q": "Quit the game"},
        {"1": "wooden_door", "q": "quit"}
    ),
    "sit_armchair": Scene(
        "As you sit in the armchair, you feel strangely at peace. Maybe this is a good place to rest...",
        {"1": "Go back to the library", "q": "Quit the game"},
        {"1": "wooden_door", "q": "quit"}
    ),
    "investigate_machines": Scene(
        "The machines appear to be some sort of interdimensional travel devices. Best not to touch anything.",
        {"1": "Return to the laboratory", "q": "Quit the game"},
        {"1": "metal_door", "q": "quit"}
    ),
    "find_computer": Scene(
        "You find a computer with strange calculations on the screen. It seems to be running some kind of simulation.",
        {"1": "Return to the laboratory", "q": "Quit the game"},
        {"1": "metal_door", "q": "quit"}
    ),
    "read_note": Scene(
        "The note reads: 'Reality is not what it seems. Choose wisely.'",
        {"1": "Go back", "q": "Quit the game"},
        {"1": "look_around", "q": "quit"}
    ),
    "study_symbols": Scene(
        "The symbols appear to be an ancient script, but their meaning remains a mystery.",
        {"1": "Go back", "q": "Quit the game"},
        {"1": "look_around", "q": "quit"}
    )
}

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def print_flush(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()

def main():
    clear_screen()
    print_flush("Welcome to the Mystery Room Adventure!")
    print_flush("==================================")
    print_flush("Enter the number of your choice at each prompt.")
    print_flush("Press 'q' at any time to quit the game.")
    print_flush("==================================")

    current_scene = "start"

    while True:
        clear_screen()
        scene = scenes[current_scene]
        print_flush(scene.description)
        print_flush("\nWhat would you like to do?")

        for key, option in scene.options.items():
            print_flush(f"{key}: {option}")

        try:
            choice = input("\nYour choice: ").strip().lower()

            if choice == "q":
                print_flush("\nThanks for playing! Goodbye!")
                break

            if choice in scene.next_scenes:
                current_scene = scene.next_scenes[choice]
            else:
                input("Invalid choice. Press Enter to try again.")
        except KeyboardInterrupt:
            print_flush("\n\nGame interrupted. Thanks for playing!")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print_flush(f"\nAn error occurred: {e}")
        print_flush("Thanks for playing!")