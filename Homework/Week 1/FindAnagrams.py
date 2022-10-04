from WordCompare import word_compare # imports the word_compare function from WordCompare

def find_anagrams(word_list):
    anagramList = "" # empty string we're going to use
    
    for word in word_list: # Loops through each word in the word list
        anagramList += str(word) + ": " # Add word to anagram list
        tempList = [] # Temporary list which gets reset on every new word

        for i in range(0, len(word_list)): # Goes through each word using list index
            if word != word_list[i]: # Words can't be anagrams to themselves
                if word_compare(word, word_list[i]) == "Anagram":
                    tempList.append(word_list[i]) # Adds anagrams to list
        
        anagramList += str(tempList) + "\n" # Adds list of anagrams to the string
    return anagramList.rstrip()

words = ["act", "cat", "tac", "map", "pam", "amp", "hello", "mickey", "mouse", "clown", "cse2050", "america"]
expected_result = "act: ['cat', 'tac']\ncat: ['act', 'tac']\ntac: ['act', 'cat']\nmap: ['pam', 'amp']\npam: ['map', 'amp']\namp: ['map', 'pam']\nhello: []\nmickey: []\nmouse: []\nclown: []\ncse2050: []\namerica: []" # Expected result
assert find_anagrams(words) == expected_result # Test case