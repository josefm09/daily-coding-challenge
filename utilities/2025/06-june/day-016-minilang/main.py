#!/usr/bin/env python3
"""
Day 16: MiniLang
Date: June 25, 2025

365 Days of Code Challenge

A simple stack-based mini language interpreter that supports:
- PUSH n: Push number n onto the stack
- POP: Remove the top item from the stack
- ADD: Pop two items and push their sum
- SUB: Pop two items and push their difference (second - first)
- MUL: Pop two items and push their product
- DIV: Pop two items and push their quotient (second / first)
- PRINT: Print the top item without removing it

Example program:
    PUSH 5
    PUSH 3
    ADD
    PRINT  # Outputs: 8
"""

class MiniLang:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(int(value))
    
    def pop(self):
        if not self.stack:
            raise ValueError("Stack is empty")
        return self.stack.pop()
    
    def add(self):
        b = self.pop()
        a = self.pop()
        self.push(a + b)
    
    def sub(self):
        b = self.pop()
        a = self.pop()
        self.push(a - b)
    
    def mul(self):
        b = self.pop()
        a = self.pop()
        self.push(a * b)
    
    def div(self):
        b = self.pop()
        a = self.pop()
        if b == 0:
            raise ValueError("Division by zero")
        self.push(a // b)
    
    def print_top(self):
        if not self.stack:
            raise ValueError("Stack is empty")
        print(self.stack[-1])
    
    def execute(self, program):
        for line in program.strip().split('\n'):
            tokens = line.strip().split()
            if not tokens:
                continue
            
            command = tokens[0].upper()
            if command == 'PUSH':
                if len(tokens) != 2:
                    raise ValueError("PUSH requires a value")
                self.push(tokens[1])
            elif command == 'POP':
                self.pop()
            elif command == 'ADD':
                self.add()
            elif command == 'SUB':
                self.sub()
            elif command == 'MUL':
                self.mul()
            elif command == 'DIV':
                self.div()
            elif command == 'PRINT':
                self.print_top()
            else:
                raise ValueError(f"Unknown command: {command}")

def main():
    # Example program
    program = """
    PUSH 15
    PUSH 5
    DIV
    PRINT
    PUSH 3
    MUL
    PRINT
    PUSH 4
    ADD
    PRINT
    """
    
    interpreter = MiniLang()
    try:
        interpreter.execute(program)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
