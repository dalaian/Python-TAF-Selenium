import utils.utils as utils
import utils.read_file as read_file
import sys

# The path of the data file can be sent through the command line,
# if not, by default the file is 'max_edge_case.txt'
path = sys.argv[1] if len(sys.argv) > 1 else "data/max_edge_case.txt"

content = read_file.convert_file_to_list(path)
largest_word = utils.get_largest_word(content)
inverted_word = utils.reverse_word(largest_word)

print "Longest word: ", largest_word
print "Inverted longest word: ", inverted_word
