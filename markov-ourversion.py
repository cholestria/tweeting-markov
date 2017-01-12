import twitter
import os
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
 
    return twitter_text

    # return random_text   
def tweet_function(chains):
    """takes chains as input and asks if we want to tweet"""

    api = twitter.Api(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    # print api.VerifyCredentials()

    

    user_input = raw_input("Do you want to tweet? ")

    # while True:

    if user_input == "Y":
        status = api.PostUpdate(make_text(chains))
        print status.text

        # elif user_input == "q":
        #     break

        # else:         
        #     print "I didn't understand"
        #     continue


    

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
other_random_text = make_text(chains)

# print other_random_text
tweet_status = tweet_function(chains)
