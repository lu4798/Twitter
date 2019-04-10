import unittest
from unittest.mock import Mock, MagicMock

from PruebaListas import twitter_things

class MyTestCase(unittest.TestCase):
    def test_example(self):
        real = twitter_things()
        mock = MagicMock()
        real.twitter_word_count(mock)
        mock.iterate.assert_called_with()

if __name__ == '__main__':
    unittest.main()


