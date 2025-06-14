#!/usr/bin/env python3
"""
Unit tests for the Word Counter Tool
"""

import unittest
from word_counter import WordCounter


class TestWordCounter(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        self.simple_text = "Hello world! This is a test."
        self.complex_text = """The Art of Programming

Programming is both an art and a science. It requires creativity, logic, and persistence.

Every programmer knows that writing code is just the beginning of a long journey."""
        
    def test_basic_counts(self):
        """Test basic counting functionality."""
        counter = WordCounter(self.simple_text)
        
        self.assertEqual(counter.character_count(True), 28)  # "Hello world! This is a test." = 28 chars
        self.assertEqual(counter.character_count(False), 23)
        self.assertEqual(counter.word_count(), 6)
        self.assertEqual(counter.sentence_count(), 2)
        self.assertEqual(counter.line_count(), 1)
        
    def test_word_extraction(self):
        """Test word extraction and cleaning."""
        counter = WordCounter("Hello, world! This is a test...")
        words = counter.words
        
        # Should remove punctuation and convert to lowercase
        expected_words = ['hello', 'world', 'this', 'is', 'a', 'test']
        self.assertEqual(words, expected_words)
        
    def test_unique_word_count(self):
        """Test unique word counting."""
        counter = WordCounter("the cat and the dog and the bird")
        
        self.assertEqual(counter.word_count(), 8)  # the cat and the dog and the bird = 8 words
        self.assertEqual(counter.unique_word_count(), 5)  # the, cat, and, dog, bird
        
    def test_word_frequency(self):
        """Test word frequency analysis."""
        counter = WordCounter("apple banana apple cherry apple banana")
        frequency = counter.word_frequency(3)
        
        self.assertEqual(frequency[0], ('apple', 3))
        self.assertEqual(frequency[1], ('banana', 2))
        self.assertEqual(frequency[2], ('cherry', 1))
        
    def test_averages(self):
        """Test average calculations."""
        counter = WordCounter("cat dog elephant")
        
        # Average word length: (3 + 3 + 8) / 3 = 4.67
        self.assertAlmostEqual(counter.average_word_length(), 4.67, places=2)
        
    def test_extremes(self):
        """Test longest and shortest word detection."""
        counter = WordCounter("a comprehensive test")
        
        self.assertEqual(counter.longest_word(), 'comprehensive')
        self.assertEqual(counter.shortest_word(), 'a')
        
    def test_empty_text(self):
        """Test handling of empty text."""
        counter = WordCounter("")
        
        self.assertEqual(counter.word_count(), 0)
        self.assertEqual(counter.character_count(), 0)
        self.assertEqual(counter.sentence_count(), 0)
        self.assertEqual(counter.longest_word(), "")
        self.assertEqual(counter.shortest_word(), "")
        
    def test_multiline_text(self):
        """Test multiline text processing."""
        counter = WordCounter(self.complex_text)
        
        self.assertGreater(counter.line_count(), 1)
        self.assertGreater(counter.paragraph_count(), 1)
        self.assertGreater(counter.sentence_count(), 2)
        
    def test_paragraph_count(self):
        """Test paragraph counting."""
        text_with_paragraphs = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."
        counter = WordCounter(text_with_paragraphs)
        
        self.assertEqual(counter.paragraph_count(), 3)
        
    def test_reading_time(self):
        """Test reading time estimation."""
        # 200 words should take 1 minute at 200 WPM
        text = " ".join(["word"] * 200)
        counter = WordCounter(text)
        
        self.assertEqual(counter.reading_time(200), 1.0)
        
    def test_set_text(self):
        """Test changing text after initialization."""
        counter = WordCounter("initial text")
        self.assertEqual(counter.word_count(), 2)
        
        counter.set_text("new longer text with more words")
        self.assertEqual(counter.word_count(), 6)
        
    def test_comprehensive_stats(self):
        """Test comprehensive statistics dictionary."""
        counter = WordCounter(self.simple_text)
        stats = counter.get_comprehensive_stats()
        
        # Check that all expected keys are present
        expected_keys = [
            'characters_with_spaces', 'characters_without_spaces',
            'words', 'unique_words', 'lines', 'sentences', 'paragraphs',
            'average_word_length', 'average_sentence_length',
            'longest_word', 'shortest_word', 'estimated_reading_time_minutes'
        ]
        
        for key in expected_keys:
            self.assertIn(key, stats)
            
        # Check some specific values
        self.assertEqual(stats['words'], 6)
        self.assertEqual(stats['sentences'], 2)


if __name__ == '__main__':
    print("Running Word Counter tests...")
    unittest.main(verbosity=2)

