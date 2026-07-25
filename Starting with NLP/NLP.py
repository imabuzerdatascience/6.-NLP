# sentences tokeniztion 

from nltk.tokenize import sent_tokenize 

sentences = '''
Hello my name is abuzer khan , and i live in biratnagar six . I am datascientisst 
and I work hard to fnd a job 

''' 

sent = sent_tokenize(sentences) 
print(sent)