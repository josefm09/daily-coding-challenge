#!/usr/bin/env python3
import subprocess
import sys

# Test piping functionality
test_text = "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet!"

# Run the word counter with piped input
process = subprocess.Popen(
    [sys.executable, "word_counter.py", "--frequency"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

stdout, stderr = process.communicate(input=test_text)
print(stdout)
if stderr:
    print("Errors:", stderr)

