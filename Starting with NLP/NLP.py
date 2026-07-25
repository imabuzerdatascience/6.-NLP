# sentences tokeniztion 

from nltk.tokenize import sent_tokenize 
import spacy 
sentences = '''
Hello my name is abuzer khan , and i live in biratnagar six . I am datascientisst 
and I work hard to fnd a job 

''' 

sent = sent_tokenize(sentences) 
print(sent) 


print("--------------------------------------------------------------------")

# another one 
text = '''
I am learning NLP.
I am learning Machine Learning!
Are you learning AI?
Yes, I am.

''' 

token = sent_tokenize(text) 

#using for loop to print 
for tokens in token : 
    print(tokens)

#direct print 
print(token) 


# playing with spacy  
