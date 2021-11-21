""" Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string.
If there are two or more words that are the same length, return the first word from the string with that length. 
 Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

example - input = "fun123!! world"
          output = "fun123"
 """
import re

def LongestWord(sen):
  # code goes here
  largest = ""
  temp = ""
  for letter in sen:
    if not re.search("[a-zA-Z0-9]", letter):
      #print('enter')
      largest = larger(largest,temp)
      temp = ""
    else:
      #print(letter)
      temp+=letter
    largest = larger(largest,temp)
  return largest

def larger(word1,word2):
  if len(word1) >= len(word2):
    return word1
  else:
    return word2

# keep this function call here 
print(LongestWord(input()))