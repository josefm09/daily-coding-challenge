#!/usr/bin/env python3
"""
Daily Commit Utility for 365 Days of Code Challenge

This script helps automate daily commits and track progress.
"""

import os
import sys
from datetime import datetime
import subprocess

def get_current_day():
    """Calculate current day number since June 10, 2025"""
    start_date = datetime(2025, 6, 10)
    current_date = datetime.now()
    return (current_date - start_date).days + 1

def create_daily_structure(day_num, project_name):
    """Create directory structure for today's project"""
    current_date = datetime.now()
    month_dir = f"2025/{current_date.month:02d}-{current_date.strftime('%B').lower()}"
    day_dir = f"{month_dir}/day-{day_num:03d}-{project_name.lower().replace(' ', '-')}"
    
    os.makedirs(day_dir, exist_ok=True)
    
    # Create a basic project file
    project_file = f"{day_dir}/main.py"
    if not os.path.exists(project_file):
        with open(project_file, 'w') as f:
            f.write(f'#!/usr/bin/env python3\n')
            f.write(f'"""\n')
            f.write(f'Day {day_num}: {project_name}\n')
            f.write(f'Date: {current_date.strftime("%B %d, %Y")}\n')
            f.write(f'\n')
            f.write(f'365 Days of Code Challenge\n')
            f.write(f'"""\n\n')
            f.write(f'def main():\n')
            f.write(f'    print("Day {day_num}: {project_name}")\n')
            f.write(f'    # TODO: Implement your daily challenge here\n')
            f.write(f'    pass\n\n')
            f.write(f'if __name__ == "__main__":\n')
            f.write(f'    main()\n')
    
    # Create README for the day
    readme_file = f"{day_dir}/README.md"
    if not os.path.exists(readme_file):
        with open(readme_file, 'w') as f:
            f.write(f'# Day {day_num}: {project_name}\n\n')
            f.write(f'**Date:** {current_date.strftime("%B %d, %Y")}\n\n')
            f.write(f'## Description\n\n')
            f.write(f'[Brief description of what you built today]\n\n')
            f.write(f'## Technologies Used\n\n')
            f.write(f'- Python\n')
            f.write(f'- [Add other technologies]\n\n')
            f.write(f'## Challenges Faced\n\n')
            f.write(f'[What problems did you encounter and how did you solve them?]\n\n')
            f.write(f'## What I Learned\n\n')
            f.write(f'[Key takeaways from today\'s coding session]\n\n')
            f.write(f'## Running the Code\n\n')
            f.write(f'```bash\n')
            f.write(f'python main.py\n')
            f.write(f'```\n\n')
            f.write(f'---\n\n')
            f.write(f'*Part of the #365DaysOfCode challenge*\n')
    
    return day_dir

def commit_daily_progress(day_num, project_name, message=""):
    """Create and commit daily progress"""
    if not message:
        message = f"Day {day_num}: {project_name}\n\n✨ Daily coding challenge completed!\n\n#365DaysOfCode #DailyCoding"
    
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        print(f"✅ Day {day_num} committed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to commit: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python daily_commit.py <project_name> [commit_message]")
        print("Example: python daily_commit.py 'Calculator App'")
        sys.exit(1)
    
    project_name = sys.argv[1]
    custom_message = sys.argv[2] if len(sys.argv) > 2 else ""
    
    day_num = get_current_day()
    
    print(f"🚀 Starting Day {day_num}: {project_name}")
    
    # Create project structure
    project_dir = create_daily_structure(day_num, project_name)
    print(f"📁 Created project directory: {project_dir}")
    
    # Commit progress
    if commit_daily_progress(day_num, project_name, custom_message):
        print(f"\n🎉 Day {day_num} complete! Keep the streak alive!")
        print(f"💡 Don't forget to push to GitHub: git push")
    
if __name__ == "__main__":
    main()

