# Day 1: Snake Game

**Date:** June 10, 2025

## Description

Implemented a classic Snake game using Python's curses library with optimized rendering to eliminate screen flickering. The game features smooth gameplay, score tracking, and responsive controls.

## Technologies Used

- Python 3
- curses library (terminal-based UI)
- Git (version control)

## Key Features

- ✨ **Smooth rendering** - Fixed blinking/flickering issues
- 🎮 **Responsive controls** - Arrow key navigation
- 📊 **Score tracking** - Current and high score display
- 🎨 **Color support** - Red food (if terminal supports colors)
- 🏆 **Win condition** - Fill the entire screen
- 🔄 **Restart functionality** - Press 'R' to restart

## Challenges Faced

1. **Screen Flickering**: The original implementation used `stdscr.clear()` on every frame, causing annoying blinking
2. **Solution**: Separated static and dynamic elements, only clearing the game area instead of the entire screen
3. **Optimization**: Created `draw_static_elements()` method for title, border, and instructions that don't change frequently

## What I Learned

- **Efficient terminal rendering** - Avoid clearing entire screen unnecessarily
- **Game loop optimization** - Separate static from dynamic content
- **curses library** - Better understanding of terminal-based UI development
- **Code organization** - Breaking drawing logic into logical components

## Technical Improvements Made

- Removed `stdscr.clear()` from main drawing loop
- Added `draw_static_elements()` for one-time rendering
- Optimized score display updates
- Better error handling for out-of-bounds coordinates

## Running the Code

```bash
python snake_game.py
```

### Controls
- ⬆️⬇️⬅️➡️ **Arrow Keys**: Move the snake
- **R**: Restart game
- **Q**: Quit game

## Game Elements
- `@` - Snake head
- `#` - Snake body segments
- `*` - Food (red if colors supported)

---

*Day 1 of #365DaysOfCode challenge complete! 🎉*

**Next Challenge Ideas:**
- Add sound effects
- Implement difficulty levels
- Add power-ups
- Create multiplayer mode

