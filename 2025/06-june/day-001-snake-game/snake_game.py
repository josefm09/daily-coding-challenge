#!/usr/bin/env python3

import curses
import random
import time

class SnakeGame:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        
    def setup_screen(self, stdscr):
        """Initialize the game screen"""
        curses.curs_set(0)  # Hide cursor
        stdscr.nodelay(1)   # Non-blocking input
        stdscr.timeout(150) # Game speed (milliseconds)
        
        # Get screen dimensions
        self.height, self.width = stdscr.getmaxyx()
        
        # Check minimum terminal size
        if self.height < 10 or self.width < 40:
            raise Exception(f"Terminal too small. Need at least 40x10, got {self.width}x{self.height}")
        
        # Create game window
        self.win = curses.newwin(self.height - 3, self.width - 2, 1, 1)
        self.win.keypad(1)
        self.win.border(0)
        
        # Game area dimensions (inside border)
        self.game_height = self.height - 5
        self.game_width = self.width - 4
        
    def init_snake(self):
        """Initialize snake position and direction"""
        # Snake starts in the middle of the screen
        start_x = self.game_width // 2
        start_y = self.game_height // 2
        
        # Snake body (list of [y, x] coordinates)
        self.snake = [
            [start_y, start_x],
            [start_y, start_x - 1],
            [start_y, start_x - 2]
        ]
        
        # Initial direction (moving right)
        self.direction = [0, 1]
        
    def create_food(self):
        """Create food at random position"""
        # Prevent infinite loop if snake fills most of the screen
        max_attempts = 100
        attempts = 0
        
        while attempts < max_attempts:
            food_y = random.randint(1, self.game_height - 2)
            food_x = random.randint(1, self.game_width - 2)
            
            # Make sure food doesn't spawn on snake
            if [food_y, food_x] not in self.snake:
                self.food = [food_y, food_x]
                return
            attempts += 1
            
        # Fallback: find any free space
        for y in range(1, self.game_height - 1):
            for x in range(1, self.game_width - 1):
                if [y, x] not in self.snake:
                    self.food = [y, x]
                    return
                    
        # If no space found, game is essentially won
        self.food = None
                
    def draw_static_elements(self, stdscr):
        """Draw static elements that don't change often"""
        # Draw title
        title = "SNAKE GAME"
        stdscr.addstr(0, (self.width - len(title)) // 2, title, curses.A_BOLD)
        
        # Draw instructions
        instructions = "Use arrow keys to move, 'q' to quit, 'r' to restart"
        if len(instructions) < self.width - 4:
            stdscr.addstr(self.height - 1, 2, instructions)
        
        # Draw game border
        self.win.border(0)
        stdscr.refresh()
        
    def draw_screen(self, stdscr):
        """Draw the game screen efficiently"""
        # Only clear the game area, not the entire screen
        for y in range(1, self.game_height - 1):
            for x in range(1, self.game_width - 1):
                try:
                    self.win.addch(y, x, ' ')
                except curses.error:
                    pass
        
        # Update score (this changes frequently)
        score_text = f"Score: {self.score}  High Score: {self.high_score}"
        # Clear the score line first
        try:
            stdscr.addstr(self.height - 2, 2, "" * min(len(score_text) + 10, self.width - 4))
            stdscr.addstr(self.height - 2, 2, score_text)
        except curses.error:
            pass
        
        # Draw snake
        for i, segment in enumerate(self.snake):
            y, x = segment
            try:
                if i == 0:  # Head
                    self.win.addch(y, x, '@', curses.A_BOLD)
                else:  # Body
                    self.win.addch(y, x, '#')
            except curses.error:
                # Skip if coordinates are out of bounds
                pass
                
        # Draw food (if it exists)
        if self.food is not None:
            try:
                if self.has_colors:
                    self.win.addch(self.food[0], self.food[1], '*', curses.A_BOLD | curses.color_pair(1))
                else:
                    self.win.addch(self.food[0], self.food[1], '*', curses.A_BOLD)
            except curses.error:
                # Skip if coordinates are out of bounds
                pass
        
        self.win.refresh()
        stdscr.refresh()
        
    def move_snake(self):
        """Move snake in current direction"""
        # Calculate new head position
        head = self.snake[0]
        new_head = [head[0] + self.direction[0], head[1] + self.direction[1]]
        
        # Check wall collision (fixed boundary detection)
        if (new_head[0] < 1 or new_head[0] >= self.game_height - 1 or
            new_head[1] < 1 or new_head[1] >= self.game_width - 1):
            return False
            
        # Check self collision
        if new_head in self.snake:
            return False
            
        # Add new head
        self.snake.insert(0, new_head)
        
        # Check if food eaten
        if self.food is not None and new_head == self.food:
            self.score += 10
            if self.score > self.high_score:
                self.high_score = self.score
            self.create_food()
            
            # Check for win condition (no more space for food)
            if self.food is None:
                return 'win'
        else:
            # Remove tail if no food eaten
            self.snake.pop()
            
        return True
        
    def handle_input(self, key):
        """Handle user input"""
        # Arrow key controls
        if key == curses.KEY_UP and self.direction != [1, 0]:
            self.direction = [-1, 0]
        elif key == curses.KEY_DOWN and self.direction != [-1, 0]:
            self.direction = [1, 0]
        elif key == curses.KEY_LEFT and self.direction != [0, 1]:
            self.direction = [0, -1]
        elif key == curses.KEY_RIGHT and self.direction != [0, -1]:
            self.direction = [0, 1]
        elif key == ord('q') or key == ord('Q'):
            return 'quit'
        elif key == ord('r') or key == ord('R'):
            return 'restart'
            
        return 'continue'
        
    def game_over_screen(self, stdscr):
        """Display game over screen"""
        game_over_text = "GAME OVER!"
        final_score_text = f"Final Score: {self.score}"
        restart_text = "Press 'r' to restart or 'q' to quit"
        
        # Display messages with bounds checking
        try:
            stdscr.addstr(self.height // 2 - 1, max(0, (self.width - len(game_over_text)) // 2), 
                         game_over_text, curses.A_BOLD)
            stdscr.addstr(self.height // 2, max(0, (self.width - len(final_score_text)) // 2), 
                         final_score_text)
            stdscr.addstr(self.height // 2 + 1, max(0, (self.width - len(restart_text)) // 2), 
                         restart_text)
        except curses.error:
            # If text doesn't fit, just show basic message
            stdscr.addstr(1, 1, "Game Over! Press 'r' to restart or 'q' to quit")
        
        stdscr.refresh()
        
        # Wait for input
        while True:
            key = stdscr.getch()
            if key == ord('r') or key == ord('R'):
                return 'restart'
            elif key == ord('q') or key == ord('Q'):
                return 'quit'
                
    def win_screen(self, stdscr):
        """Display win screen"""
        win_text = "YOU WIN!"
        final_score_text = f"Perfect Score: {self.score}"
        restart_text = "Press 'r' to restart or 'q' to quit"
        
        # Display messages with bounds checking
        try:
            stdscr.addstr(self.height // 2 - 1, max(0, (self.width - len(win_text)) // 2), 
                         win_text, curses.A_BOLD)
            stdscr.addstr(self.height // 2, max(0, (self.width - len(final_score_text)) // 2), 
                         final_score_text)
            stdscr.addstr(self.height // 2 + 1, max(0, (self.width - len(restart_text)) // 2), 
                         restart_text)
        except curses.error:
            # If text doesn't fit, just show basic message
            stdscr.addstr(1, 1, "You Win! Press 'r' to restart or 'q' to quit")
        
        stdscr.refresh()
        
        # Wait for input
        while True:
            key = stdscr.getch()
            if key == ord('r') or key == ord('R'):
                return 'restart'
            elif key == ord('q') or key == ord('Q'):
                return 'quit'
                
    def reset_game(self):
        """Reset game state"""
        self.score = 0
        self.init_snake()
        self.create_food()
        
    def run(self, stdscr):
        """Main game loop"""
        # Setup colors if supported
        self.has_colors = False
        if curses.has_colors():
            try:
                curses.start_color()
                curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
                self.has_colors = True
            except curses.error:
                # Color initialization failed, continue without colors
                pass
        
        self.setup_screen(stdscr)
        self.reset_game()
        
        # Draw static elements once
        self.draw_static_elements(stdscr)
        
        while True:
            self.draw_screen(stdscr)
            
            # Get input
            key = self.win.getch()
            action = self.handle_input(key)
            
            if action == 'quit':
                break
            elif action == 'restart':
                self.reset_game()
                # Redraw static elements after restart
                stdscr.clear()
                self.draw_static_elements(stdscr)
                continue
                
            # Move snake
            move_result = self.move_snake()
            if move_result == False:
                # Game over
                action = self.game_over_screen(stdscr)
                if action == 'quit':
                    break
                elif action == 'restart':
                    self.reset_game()
                    # Redraw static elements after restart
                    stdscr.clear()
                    self.draw_static_elements(stdscr)
            elif move_result == 'win':
                # Player won (filled entire screen)
                action = self.win_screen(stdscr)
                if action == 'quit':
                    break
                elif action == 'restart':
                    self.reset_game()
                    # Redraw static elements after restart
                    stdscr.clear()
                    self.draw_static_elements(stdscr)
                    
def main():
    """Main function to start the game"""
    game = SnakeGame()
    curses.wrapper(game.run)
    
if __name__ == "__main__":
    print("Starting Snake Game...")
    print("Use arrow keys to move, 'q' to quit, 'r' to restart")
    print("Press any key to start...")
    input()
    
    try:
        main()
        print("\nThanks for playing Snake Game!")
    except KeyboardInterrupt:
        print("\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Make sure your terminal supports the required features.")

