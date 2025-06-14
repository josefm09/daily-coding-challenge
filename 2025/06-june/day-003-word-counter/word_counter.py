#!/usr/bin/env python3
"""
Daily Coding Challenge - Day 003
Word Counter Tool

A comprehensive command-line tool for analyzing text with various counting features.

Author: Jose
Date: June 14, 2025
"""

import os
import sys
import re
import argparse
from collections import Counter, defaultdict
from typing import Dict, List, Tuple
import string


class WordCounter:
    """A comprehensive text analysis tool."""
    
    def __init__(self, text: str = ""):
        self.text = text
        self.lines = text.split('\n') if text else []
        self.words = self._extract_words(text) if text else []
        self.sentences = self._extract_sentences(text) if text else []
    
    def _extract_words(self, text: str) -> List[str]:
        """Extract words from text, removing punctuation."""
        # Remove punctuation and convert to lowercase
        text_clean = re.sub(r'[^\w\s]', ' ', text.lower())
        return [word for word in text_clean.split() if word]
    
    def _extract_sentences(self, text: str) -> List[str]:
        """Extract sentences from text."""
        # Split on sentence endings, filter empty
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def load_from_file(self, filepath: str) -> bool:
        """Load text from a file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.text = f.read()
            self.lines = self.text.split('\n')
            self.words = self._extract_words(self.text)
            self.sentences = self._extract_sentences(self.text)
            return True
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            return False
    
    def set_text(self, text: str):
        """Set new text to analyze."""
        self.text = text
        self.lines = text.split('\n')
        self.words = self._extract_words(text)
        self.sentences = self._extract_sentences(text)
    
    def character_count(self, include_spaces: bool = True) -> int:
        """Count characters in text."""
        if include_spaces:
            return len(self.text)
        else:
            return len(re.sub(r'\s', '', self.text))
    
    def word_count(self) -> int:
        """Count total words in text."""
        return len(self.words)
    
    def line_count(self) -> int:
        """Count lines in text."""
        return len(self.lines)
    
    def sentence_count(self) -> int:
        """Count sentences in text."""
        return len(self.sentences)
    
    def paragraph_count(self) -> int:
        """Count paragraphs (separated by empty lines)."""
        paragraphs = self.text.split('\n\n')
        return len([p for p in paragraphs if p.strip()])
    
    def word_frequency(self, top_n: int = 10) -> List[Tuple[str, int]]:
        """Get most frequent words."""
        counter = Counter(self.words)
        return counter.most_common(top_n)
    
    def unique_word_count(self) -> int:
        """Count unique words."""
        return len(set(self.words))
    
    def average_word_length(self) -> float:
        """Calculate average word length."""
        if not self.words:
            return 0.0
        return sum(len(word) for word in self.words) / len(self.words)
    
    def average_sentence_length(self) -> float:
        """Calculate average sentence length in words."""
        if not self.sentences:
            return 0.0
        total_words = sum(len(self._extract_words(sentence)) for sentence in self.sentences)
        return total_words / len(self.sentences)
    
    def longest_word(self) -> str:
        """Find the longest word."""
        return max(self.words, key=len) if self.words else ""
    
    def shortest_word(self) -> str:
        """Find the shortest word."""
        return min(self.words, key=len) if self.words else ""
    
    def reading_time(self, wpm: int = 200) -> float:
        """Estimate reading time in minutes (default 200 words per minute)."""
        return self.word_count() / wpm
    
    def character_frequency(self) -> Dict[str, int]:
        """Get character frequency (excluding spaces)."""
        text_no_spaces = re.sub(r'\s', '', self.text.lower())
        return dict(Counter(text_no_spaces))
    
    def get_comprehensive_stats(self) -> Dict:
        """Get all statistics in one dictionary."""
        return {
            'characters_with_spaces': self.character_count(True),
            'characters_without_spaces': self.character_count(False),
            'words': self.word_count(),
            'unique_words': self.unique_word_count(),
            'lines': self.line_count(),
            'sentences': self.sentence_count(),
            'paragraphs': self.paragraph_count(),
            'average_word_length': round(self.average_word_length(), 2),
            'average_sentence_length': round(self.average_sentence_length(), 2),
            'longest_word': self.longest_word(),
            'shortest_word': self.shortest_word(),
            'estimated_reading_time_minutes': round(self.reading_time(), 2)
        }


def print_analysis(counter: WordCounter, show_frequency: bool = False, top_words: int = 10):
    """Print comprehensive text analysis."""
    stats = counter.get_comprehensive_stats()
    
    print("\n" + "="*50)
    print("📊 TEXT ANALYSIS RESULTS")
    print("="*50)
    
    print(f"\n📝 Basic Counts:")
    print(f"   Characters (with spaces):    {stats['characters_with_spaces']:,}")
    print(f"   Characters (without spaces): {stats['characters_without_spaces']:,}")
    print(f"   Words:                       {stats['words']:,}")
    print(f"   Unique words:                {stats['unique_words']:,}")
    print(f"   Lines:                       {stats['lines']:,}")
    print(f"   Sentences:                   {stats['sentences']:,}")
    print(f"   Paragraphs:                  {stats['paragraphs']:,}")
    
    print(f"\n📏 Averages:")
    print(f"   Average word length:         {stats['average_word_length']} characters")
    print(f"   Average sentence length:     {stats['average_sentence_length']} words")
    
    print(f"\n🔍 Extremes:")
    print(f"   Longest word:                '{stats['longest_word']}'")
    print(f"   Shortest word:               '{stats['shortest_word']}'")
    
    print(f"\n⏱️  Reading time:                {stats['estimated_reading_time_minutes']} minutes")
    
    if show_frequency and counter.word_count() > 0:
        print(f"\n🔥 Top {top_words} Most Frequent Words:")
        for i, (word, count) in enumerate(counter.word_frequency(top_words), 1):
            percentage = (count / counter.word_count()) * 100
            print(f"   {i:2d}. '{word}' - {count} times ({percentage:.1f}%)")
    
    print("\n" + "="*50)


def main():
    parser = argparse.ArgumentParser(
        description="Word Counter Tool - Comprehensive text analysis"
    )
    parser.add_argument(
        'input', 
        nargs='?',
        help='Input file path (if not provided, reads from stdin)'
    )
    parser.add_argument(
        '--frequency', '-f',
        action='store_true',
        help='Show word frequency analysis'
    )
    parser.add_argument(
        '--top', '-t',
        type=int,
        default=10,
        help='Number of top frequent words to show (default: 10)'
    )
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Interactive mode - enter text directly'
    )
    
    args = parser.parse_args()
    
    counter = WordCounter()
    
    # Determine input source
    if args.interactive:
        print("📝 Interactive Mode - Enter your text (press Ctrl+D when finished):")
        try:
            text = sys.stdin.read()
            counter.set_text(text)
        except KeyboardInterrupt:
            print("\n❌ Cancelled by user")
            sys.exit(1)
    elif args.input:
        if not os.path.exists(args.input):
            print(f"❌ File not found: {args.input}")
            sys.exit(1)
        if not counter.load_from_file(args.input):
            sys.exit(1)
        print(f"📁 Analyzing file: {args.input}")
    else:
        # Read from stdin if available
        if sys.stdin.isatty():
            print("❌ No input provided. Use --interactive, provide a file, or pipe text.")
            print("Examples:")
            print("  python word_counter.py myfile.txt")
            print("  python word_counter.py --interactive")
            print("  echo 'Hello world' | python word_counter.py")
            sys.exit(1)
        else:
            text = sys.stdin.read()
            counter.set_text(text)
    
    # Perform analysis
    if counter.word_count() == 0:
        print("⚠️  No text to analyze!")
        sys.exit(1)
    
    print_analysis(counter, args.frequency, args.top)


if __name__ == "__main__":
    main()

