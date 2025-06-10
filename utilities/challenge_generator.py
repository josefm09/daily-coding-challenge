#!/usr/bin/env python3
"""
Daily Challenge Generator for 365 Days of Code

Generates random coding challenge ideas to keep you motivated!
"""

import random
from datetime import datetime

# Challenge categories with difficulty levels
CHALLENGES = {
    "beginner": [
        "Build a simple calculator",
        "Create a password generator",
        "Make a number guessing game",
        "Build a unit converter",
        "Create a simple todo list",
        "Make a rock-paper-scissors game",
        "Build a basic file organizer",
        "Create a word counter tool",
        "Make a simple timer/stopwatch",
        "Build a random quote generator"
    ],
    "intermediate": [
        "Create a web scraper",
        "Build a weather app using API",
        "Make a text-based adventure game",
        "Create a basic chat application",
        "Build a file encryption tool",
        "Make a simple database CRUD app",
        "Create a URL shortener",
        "Build a basic web server",
        "Make a log file analyzer",
        "Create a simple REST API"
    ],
    "advanced": [
        "Build a mini compiler/interpreter",
        "Create a machine learning model",
        "Make a real-time multiplayer game",
        "Build a distributed system",
        "Create a blockchain implementation",
        "Make a computer vision application",
        "Build a search engine",
        "Create a performance monitoring tool",
        "Make a code formatter/linter",
        "Build a containerized microservice"
    ],
    "creative": [
        "ASCII art generator",
        "Music composition algorithm",
        "Procedural art creator",
        "Poetry generator using AI",
        "Interactive story creator",
        "Color palette generator",
        "Maze generator and solver",
        "Fractal visualizer",
        "Sound synthesizer",
        "Photo filter creator"
    ]
}

TECHNOLOGIES = [
    "Python", "JavaScript", "Go", "Rust", "TypeScript", "Swift", "Kotlin",
    "React", "Vue.js", "Flask", "Django", "Express.js", "FastAPI",
    "PostgreSQL", "MongoDB", "Redis", "Docker", "AWS", "TensorFlow", "PyTorch"
]

def get_random_challenge(difficulty="random"):
    """Get a random challenge based on difficulty level"""
    if difficulty == "random":
        difficulty = random.choice(list(CHALLENGES.keys()))
    
    challenge = random.choice(CHALLENGES.get(difficulty, CHALLENGES["beginner"]))
    tech_stack = random.sample(TECHNOLOGIES, random.randint(1, 3))
    
    return {
        "challenge": challenge,
        "difficulty": difficulty,
        "technologies": tech_stack,
        "estimated_time": get_estimated_time(difficulty)
    }

def get_estimated_time(difficulty):
    """Get estimated time based on difficulty"""
    time_estimates = {
        "beginner": "30-60 minutes",
        "intermediate": "1-2 hours",
        "advanced": "2-4 hours",
        "creative": "1-3 hours"
    }
    return time_estimates.get(difficulty, "1-2 hours")

def get_daily_suggestion():
    """Get today's suggested challenge based on day of week"""
    day_of_week = datetime.now().weekday()
    
    # Monday: Beginner, Tuesday: Intermediate, etc.
    difficulty_schedule = {
        0: "beginner",     # Monday - Start week easy
        1: "intermediate", # Tuesday
        2: "advanced",     # Wednesday - Mid-week challenge
        3: "intermediate", # Thursday
        4: "creative",     # Friday - Fun creative project
        5: "beginner",     # Saturday - Weekend relaxed
        6: "intermediate"  # Sunday - Prepare for next week
    }
    
    suggested_difficulty = difficulty_schedule[day_of_week]
    return get_random_challenge(suggested_difficulty)

def print_challenge_card(challenge_info):
    """Print a nicely formatted challenge card"""
    print("\n" + "="*50)
    print("🎯 TODAY'S CODING CHALLENGE")
    print("="*50)
    print(f"📅 Date: {datetime.now().strftime('%B %d, %Y')}")
    print(f"🎲 Challenge: {challenge_info['challenge']}")
    print(f"📊 Difficulty: {challenge_info['difficulty'].title()}")
    print(f"⏱️  Estimated Time: {challenge_info['estimated_time']}")
    print(f"🛠️  Suggested Tech: {', '.join(challenge_info['technologies'])}")
    print("="*50)
    print("💡 Tips:")
    print("   • Start with a simple version first")
    print("   • Document your process")
    print("   • Don't worry about perfection")
    print("   • Have fun and learn something new!")
    print("\n🚀 Ready to code? Let's build something awesome!\n")

def main():
    import sys
    
    if len(sys.argv) > 1:
        difficulty = sys.argv[1].lower()
        if difficulty not in CHALLENGES and difficulty != "random":
            print(f"❌ Unknown difficulty: {difficulty}")
            print(f"Available: {', '.join(CHALLENGES.keys())}, random")
            sys.exit(1)
        challenge = get_random_challenge(difficulty)
    else:
        challenge = get_daily_suggestion()
    
    print_challenge_card(challenge)

if __name__ == "__main__":
    main()

