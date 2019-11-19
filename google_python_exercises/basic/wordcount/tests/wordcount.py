import contextlib
import os
import tempfile
import unittest

from google_python_exercises.basic.wordcount import wordcount


@contextlib.contextmanager
def generate_filename(text):
    try:
        f = tempfile.NamedTemporaryFile(delete=False)
        tmp_name = f.name
        f.write(text.encode('utf-8'))
        f.close()
        yield tmp_name
    finally:
        os.unlink(tmp_name)


class WordcountTestCase(unittest.TestCase):
    def test_functions_exists(self):
        self.assertTrue(callable(wordcount.print_words))
        self.assertTrue(callable(wordcount.print_top))

    def test_print_words(self):
        with generate_filename('word1 word1 word word word1 word1') as filename:
            self.assertListEqual(
                wordcount.gen_words(filename),
                [
                    ('word', 2),
                    ('word1', 4)
                ]
            )

    def test_print_top(self):
        with generate_filename('word1, word1. word: word? word1! word1') as filename:
            self.assertListEqual(
                wordcount.gen_top(filename),
                [
                    ('word1', 4),
                    ('word', 2)
                ]
            )
