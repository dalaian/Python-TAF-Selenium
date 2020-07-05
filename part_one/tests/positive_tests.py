import importer
import part_one.utils.utils as utils
import part_one.utils.read_file as read_file

import unittest


class PositiveTests(unittest.TestCase):

    def test_minimum_edge(self):
        """
        Test when the file has the largest word at the first line
        """
        content = read_file.convert_file_to_list("../data/min_edge_case.txt")
        largest_word = utils.get_largest_word(content)
        inverted_word = utils.reverse_word(largest_word)
        self.assertEqual(largest_word, "1234567890",
                         "The largest word is not correct when the largest word is at the first line")
        self.assertEqual(inverted_word, "0987654321",
                         "The largest word inverted is not correct when the largest word is at the first line")

    def test_maximum_edge(self):
        """
        Test when the file has the largest word at the end of the file
        """
        content = read_file.convert_file_to_list("../data/max_edge_case.txt")
        largest_word = utils.get_largest_word(content)
        inverted_word = utils.reverse_word(largest_word)
        self.assertEqual(largest_word, "abcdef",
                         "The largest word is not correct when the largest word is at the end of the file")
        self.assertEqual(inverted_word, "fedcba",
                         "The largest word inverted is not correct when the largest word is at the end of the file")

    def test_duplicates(self):
        """
        Test when the largest words is duplicated in the file
        """
        content = read_file.convert_file_to_list("../data/duplicates_case.txt")
        largest_word = utils.get_largest_word(content)
        inverted_word = utils.reverse_word(largest_word)
        self.assertEqual(largest_word, "aBcDe 01123",
                         "The largest word is not correct when there are duplicates")
        self.assertEqual(inverted_word, "32110 eDcBa",
                         "The inverted largest word is not correct when there are duplicates")

    def test_large_sentences_case(self):
        """
        Test when the file has large sentences
        """
        content = read_file.convert_file_to_list("../data/extra_large_case.txt")
        largest_word = utils.get_largest_word(content)
        inverted_word = utils.reverse_word(largest_word)
        self.assertEqual(largest_word, "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                         "The largest word is not correct when there are duplicates")
        self.assertEqual(inverted_word, ".murobal tse di mina tillom tnuresed aiciffo iuq apluc ni tnus ,tnediorp non tatadipuc taceacco tnis ruetpecxE",
                         "The inverted largest word is not correct when there are duplicates")


if __name__ == '__main__':
    unittest.main()
