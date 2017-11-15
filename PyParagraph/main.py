#import os allows the file to run across systems
import os
import re
import sys
#open the file and analyze it
file = 'paragraph_1.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)

#approximate word count
output1 = re.findall("\s+", lines)
word_count = "Approximate Word Count: "
print(word_count + str(len(output1)))

#approximate sentence count
output2 = re.findall("[?.!]", lines)
sentence_count = "Approximate Sentence Count: "
print(sentence_count + str(len(output2)))

#Average letter count per word
words = lines.split()
average = sum(len(word) for word in words) / len(words)
average_letter_count = "Average Letter Count: "
print(average_letter_count + str(average))

#average sentence length
sentence = lines.split('.')
average_sentence_count = sum(len(x.split()) for x in sentence) / len(sentence)
average_sentence_length = "Average Sentence Length: "
print(average_sentence_length + str(average_sentence_count))

sys.stdout = open('output.txt','wt')

print(word_count + str(len(output1)))
print(sentence_count + str(len(output2)))
print(average_letter_count + str(average))
print(average_sentence_length + str(average_sentence_count))