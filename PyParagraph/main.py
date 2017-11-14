#import os allows the file to run across systems
import os
import re

#open the file and analyze it

paragraph = open("paragraph_1.txt")
value = paragraph
def word_count(value):
    # Find all non-whitespace patterns.
    list = re.findall("(\S+)", value)
    # Return length of resulting list.
    return len(list)

print (word_count(value))

#approximate sentence count

#Average letter count per word

#average sentence length

