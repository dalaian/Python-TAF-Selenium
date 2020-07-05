import importer
import part_one.utils.utils as utils
import part_one.utils.read_file as read_file

import unittest


class NegativeTests(unittest.TestCase):

    def test_invalid_file(self):
        """
        Test when the file is invalid
        """
        with self.assertRaises(IOError):
            read_file.convert_file_to_list("../data/invalid_file.txt")

    def test_several_matches(self):
        """
        Test when the file has two or more words that share the largest word length
        """
        content = read_file.convert_file_to_list("../data/several_matches_case.txt")
        with self.assertRaises(Exception) as context:
            utils.get_largest_word(content)
        self.assertTrue("More than 1 result was found" in context.exception)

    def test_several_matches_with_the_same_word(self):
        """
        Test when the file has the same word duplicated, but one
        is in lower case, and the another is in upper case
        """
        content = read_file.convert_file_to_list("../data/several_matches_same_word_case.txt")
        with self.assertRaises(Exception) as context:
            utils.get_largest_word(content)
        self.assertTrue("More than 1 result was found" in context.exception)


if __name__ == '__main__':
    unittest.main()
