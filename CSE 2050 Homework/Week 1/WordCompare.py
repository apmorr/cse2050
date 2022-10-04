import string
from unittest import skip


def word_compare(val1, val2 = "steal"):
    if (isinstance(val1, str) and (isinstance(val2, str))): # Checks if both variables are strings
        if (sorted(val1) == sorted(val2)): # Rearranges strings
            return "Anagram"
        else: return (val1, val2)
    else: return "Those aren't strings!"


# Test cases
assert word_compare(22, "test") == "Those aren't strings!" # Non-string input
assert word_compare("test string", "string") == ("test string", "string") # Different string length
assert word_compare("rat", "tar") == "Anagram" # Anagram case
assert word_compare("dog", "cat") == ("dog", "cat") # Same length, but not anagrams
assert word_compare("teals") == "Anagram" # Testing default value for second parameter
