import sys
from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    corpus = open(file_path).read()


    return corpus


def make_chains(input_text):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    words = input_text.split()
    chains = {}
    
        # tuple_length = (raw_input("Enter tuple length: "))
       
    for i in range(len(words)-2):
        my_tuple = words[i], words[i+1]
        new_value = words[i+2]

            # my_tuple = word1, word2, word3, and so on until tuple  num of words is reached
            #  # my_tuple = words[i], words[i + 1]

        # my_tuple = ()
        # for i in range(int(tuple_length)):
        #     my_tuple = my_tuple + words[i]

        if my_tuple not in chains:
            chains[(my_tuple)] = [new_value]
        else:
            chains[my_tuple].append(new_value)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    random_text = ""
    key = choice(chains.keys())
    random_text = random_text + key[0] + " " + key[1]
    
    while key in chains:
        value = choice(chains[key])
        random_text = random_text + " " + value
        key = key[1], value
        
    twitter_text = random_text[:140]
    # for text in twitter_text:
    #     if 
    #         twitter_text = twitter_text + random_text

    print twitter_text

    # return random_text   

    

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
other_random_text = make_text(chains)

# print other_random_text
