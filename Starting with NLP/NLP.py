# sentences tokeniztion 

from nltk.tokenize import sent_tokenize 
import spacy  
from nltk.tokenize import word_tokenize 

# sentences = '''
# Hello my name is abuzer khan , and i live in biratnagar six . I am datascientisst 
# and I work hard to fnd a job 

# ''' 

# sent = sent_tokenize(sentences) 
# print(sent) 


# print("--------------------------------------------------------------------")

# # another one 
# text = '''
# I am learning NLP.
# I am learning Machine Learning!
# Are you learning AI?
# Yes, I am.

# ''' 

# token = sent_tokenize(text) 

# #using for loop to print 
# for tokens in token : 
#     print(tokens)

# #direct print 
# print(token) 



# word tokenizer 
# text = '''
# Hello , She is my sister and she is came from Austrila.
# ''' 
# words_token = word_tokenize(text)  


# print(words_token) 

# character toeknization 
text = "hello" 

toekns = list(text)
# print(toekns) 

text2 = "artificial" 

tokens2 = list(text2) 
print(tokens2)