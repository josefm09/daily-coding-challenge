package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Scene struct {
	Description string
	Options     map[string]string
	NextScenes  map[string]string
}

var scenes = map[string]*Scene{
	"start": {
		Description: "You wake up in a mysterious room. The walls are made of cold stone, and there's a dim light coming from somewhere above. You notice two doors: one wooden and one metal.",
		Options: map[string]string{
			"1": "Try the wooden door",
			"2": "Try the metal door",
			"3": "Look around more carefully",
		},
		NextScenes: map[string]string{
			"1": "wooden_door",
			"2": "metal_door",
			"3": "look_around",
		},
	},
	"wooden_door": {
		Description: "The wooden door creaks open to reveal a cozy library. Shelves of ancient books line the walls, and a comfortable armchair sits in the corner.",
		Options: map[string]string{
			"1": "Examine the books",
			"2": "Sit in the armchair",
			"3": "Go back",
		},
		NextScenes: map[string]string{
			"1": "examine_books",
			"2": "sit_armchair",
			"3": "start",
		},
	},
	"metal_door": {
		Description: "The metal door leads to a high-tech laboratory. Strange machines blink and hum all around you.",
		Options: map[string]string{
			"1": "Investigate the machines",
			"2": "Look for a computer",
			"3": "Go back",
		},
		NextScenes: map[string]string{
			"1": "investigate_machines",
			"2": "find_computer",
			"3": "start",
		},
	},
	"look_around": {
		Description: "As you look more carefully, you notice a small note on the floor and strange symbols carved into the walls.",
		Options: map[string]string{
			"1": "Read the note",
			"2": "Study the symbols",
			"3": "Go back",
		},
		NextScenes: map[string]string{
			"1": "read_note",
			"2": "study_symbols",
			"3": "start",
		},
	},
	"examine_books": {
		Description: "You find a mysterious book about parallel universes. It seems to contain important information.",
		Options: map[string]string{
			"1": "Go back to the library",
		},
		NextScenes: map[string]string{
			"1": "wooden_door",
		},
	},
	"sit_armchair": {
		Description: "As you sit in the armchair, you feel strangely at peace. Maybe this is a good place to rest...",
		Options: map[string]string{
			"1": "Go back to the library",
		},
		NextScenes: map[string]string{
			"1": "wooden_door",
		},
	},
	"investigate_machines": {
		Description: "The machines appear to be some sort of interdimensional travel devices. Best not to touch anything.",
		Options: map[string]string{
			"1": "Return to the laboratory",
		},
		NextScenes: map[string]string{
			"1": "metal_door",
		},
	},
	"find_computer": {
		Description: "You find a computer with strange calculations on the screen. It seems to be running some kind of simulation.",
		Options: map[string]string{
			"1": "Return to the laboratory",
		},
		NextScenes: map[string]string{
			"1": "metal_door",
		},
	},
	"read_note": {
		Description: "The note reads: 'Reality is not what it seems. Choose wisely.'",
		Options: map[string]string{
			"1": "Go back",
		},
		NextScenes: map[string]string{
			"1": "look_around",
		},
	},
	"study_symbols": {
		Description: "The symbols appear to be an ancient script, but their meaning remains a mystery.",
		Options: map[string]string{
			"1": "Go back",
		},
		NextScenes: map[string]string{
			"1": "look_around",
		},
	},
}

func main() {
	fmt.Println("Welcome to the Mystery Room Adventure!")
	fmt.Println("==================================")
	fmt.Println("Enter the number of your choice at each prompt.")
	fmt.Println("==================================")

	currentScene := "start"
	reader := bufio.NewReader(os.Stdin)

	for {
		scene := scenes[currentScene]
		fmt.Println("\n" + scene.Description)
		fmt.Println("\nWhat would you like to do?")

		for key, option := range scene.Options {
			fmt.Printf("%s: %s\n", key, option)
		}

		choice, _ := reader.ReadString('\n')
		choice = strings.TrimSpace(choice)

		if nextScene, exists := scene.NextScenes[choice]; exists {
			currentScene = nextScene
		} else {
			fmt.Println("Invalid choice. Please try again.")
		}
	}
}