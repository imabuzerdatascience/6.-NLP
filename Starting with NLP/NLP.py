# sentences tokeniztion 

# from nltk.tokenize import sent_tokenize 
# import spacy  
# from nltk.tokenize import word_tokenize 

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
# text = "hello" 

# toekns = list(text)
# # print(toekns) 

# text2 = "artificial" 

# tokens2 = list(text2) 
# print(tokens2)



# subword token nizer 
from transformers import AutoTokenizer 
tokenizer = AutoTokenizer.from_pretrained(
     "bert-base-uncased"
) 

text = "I am playing football" 

token = tokenizer.tokenize(text) 
# print(token) 


from transformers import AutoTokenizer

tokennizers = AutoTokenizer.from_pretrained(
    "bert-base-uncased"

)

text2 = "I love tokenization" 
tokens2 = tokennizers.tokenize(text2) 

# print(tokens2)

# subword tokenization with id 
from transformers import AutoTokenizer 

tokenizers_1 = AutoTokenizer.from_pretrained(
    "bert-base-uncased"
)

text_3 = "I love my Nepal" 

tokens_word = tokenizers_1.tokenize(text_3)
token_ids = tokenizers_1.convert_tokens_to_ids(tokens_word) 

# print(f"Token_words : {tokens_word}")
# print(f"Token_id : {token_ids}")  

# subword tokenization compare common and rare word 

from transformers import AutoTokenizer

tokenizers = AutoTokenizer.from_pretrained(
    "bert-base-uncased"
) 

words = [
    "play",
    "playing",
    "unbelievable",
    "hyperparameterization",
    "electroencephalography"
]

 

for word in words:
    tokens = tokenizer.tokenize(word)
print(f"{word:30} -> {tokens}")