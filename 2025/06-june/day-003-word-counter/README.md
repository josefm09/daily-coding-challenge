# Day 003 - Word Counter Tool

**Date:** June 14, 2025  
**Difficulty:** Beginner  
**Estimated Time:** 30-60 minutes

## Challenge Description

Create a comprehensive word counter tool that can analyze text files and provide detailed statistics about the content.

## Features Implemented

- ✅ Basic text counting (characters, words, lines, sentences, paragraphs)
- ✅ Advanced statistics (unique words, averages, extremes)
- ✅ Word frequency analysis
- ✅ Reading time estimation
- ✅ Multiple input methods (file, stdin, interactive)
- ✅ Command-line interface with options
- ✅ Beautiful formatted output with emojis
- ✅ Unicode and UTF-8 support

## Usage

### Basic file analysis
```bash
python3 word_counter.py document.txt
```

### Analysis with word frequency
```bash
python3 word_counter.py document.txt --frequency
```

### Show top 20 most frequent words
```bash
python3 word_counter.py document.txt -f -t 20
```

### Interactive mode
```bash
python3 word_counter.py --interactive
```

### Pipe text directly
```bash
echo "Hello world! This is a test." | python3 word_counter.py
```

### Analyze README file
```bash
python3 word_counter.py README.md --frequency
```

## Statistics Provided

### Basic Counts
- Characters (with and without spaces)
- Total words
- Unique words
- Lines
- Sentences
- Paragraphs

### Advanced Analysis
- Average word length
- Average sentence length
- Longest word
- Shortest word
- Estimated reading time (based on 200 WPM)
- Word frequency distribution

## Command Line Options

- `--frequency`, `-f`: Show word frequency analysis
- `--top`, `-t N`: Number of top frequent words to show (default: 10)
- `--interactive`, `-i`: Interactive mode for direct text input
- `--help`, `-h`: Show help message

## Example Output

```
==================================================
📊 TEXT ANALYSIS RESULTS
==================================================

📝 Basic Counts:
   Characters (with spaces):    1,234
   Characters (without spaces): 987
   Words:                       234
   Unique words:                156
   Lines:                       45
   Sentences:                   23
   Paragraphs:                  8

📏 Averages:
   Average word length:         4.2 characters
   Average sentence length:     10.2 words

🔍 Extremes:
   Longest word:                'comprehensive'
   Shortest word:               'a'

⏱️  Reading time:                1.2 minutes

🔥 Top 10 Most Frequent Words:
    1. 'the' - 15 times (6.4%)
    2. 'and' - 12 times (5.1%)
    3. 'to' - 8 times (3.4%)
    ...
```

## Technical Implementation

### Text Processing
- Uses regex for word extraction and sentence detection
- Handles punctuation removal intelligently
- Supports Unicode characters
- Case-insensitive word counting

### Input Methods
1. **File Input**: Read from specified file path
2. **Standard Input**: Pipe text from other commands
3. **Interactive Mode**: Direct text entry in terminal

### Error Handling
- File not found errors
- Empty text validation
- Encoding issues
- User interruption (Ctrl+C)

## Testing Examples

Create test files to try different scenarios:

```bash
# Test with a simple text
echo "Hello world! This is a test sentence." > test.txt
python3 word_counter.py test.txt

# Test with frequency analysis
python3 word_counter.py test.txt --frequency

# Test interactive mode
python3 word_counter.py --interactive
# Then type: "The quick brown fox jumps over the lazy dog."
# Press Ctrl+D to finish

# Test with piped input
curl -s https://www.gutenberg.org/files/11/11-0.txt | head -100 | python3 word_counter.py -f
```

## What I Learned

- Advanced Python collections (Counter, defaultdict)
- Regular expressions for text processing
- Command-line argument parsing with argparse
- Text encoding and Unicode handling
- Multiple input stream handling (stdin, files)
- Type hints for better code documentation
- Text analysis algorithms and statistics

## Possible Improvements

- Add language detection
- Implement readability scores (Flesch-Kincaid, etc.)
- Support for multiple file formats (PDF, DOCX)
- Sentiment analysis
- Export results to JSON/CSV
- Web interface with HTML output
- Syntax highlighting for code files
- Word cloud generation
- Comparison between multiple documents

