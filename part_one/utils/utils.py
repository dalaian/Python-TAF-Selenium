

def get_largest_word(words):
    """ Get the largest word from a list of strs
    Only one word can be returned
    If the largest word is found several times, it counts as just one result, which is good
    If there are multiple words that share the largest words attribute, an exception is thrown
    since only one word can be the largest word
    The case is not ignored, so, "HI" and "hi" count as two different matches, so, an exception is thrown
    since only one word can be returned
    This logic was implemented to add more negative tests
    :param words: str[], the words where the code will search for the largest word
    :return: str, the largest word
    """
    # length of the largest word(s) found, so, the method len(largestWord) won't be called unnecessarily
    largest_length = 0
    # keeps the value(s) of the largest word(s)
    largest_words = []

    # goes through all the words
    for word in words:
        # checks if word is larger than the current largest word
        if len(word) > largest_length:
            # creates a new list to save the largest words, the old one does not matter
            largest_words = [word]
            # saves the length of the largest word
            largest_length = len(word)

        # checks if word has the same length as the current largest word
        elif len(word) == largest_length:
            # checks if word exists in the list of largest word
            if word in largest_words:
                # if exists, the word is not added to the list
                continue
            # if word is not in the list, it's added to that list
            largest_words.append(word)

    # check if two or more words were found
    if len(largest_words) > 1:
        # raise an exception, several results is not supported
        raise Exception("More than 1 result was found")
    return largest_words[0]


def reverse_word(word):
    """ Reverse a word
    :param word: str, word to reverse
    :return: str, the reversed word
    """
    # reverses the word
    return word[::-1]
