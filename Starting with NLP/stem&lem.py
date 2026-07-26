# stemming and lematization 
from nltk.stem import PorterStemmer # extreme to remove suffix 

ps = PorterStemmer()
words = ["running" , "runs" , "runied "  ]
steam_words= [ps.stem(word)for word in words] 
# print(steam_words)

from nltk.stem import LancasterStemmer #more extreme to remove suffix 
ps = LancasterStemmer()
words = ["Walking" , "Walked" , "walk" , "easily"]
stem_word = [ps.stem(word) for word in words]
# print(stem_word) 

from nltk.stem import SnowballStemmer # it not too much extrme aur agressive 
ps = SnowballStemmer("english")
words = ["Walking" , "Walked" , "walk" , "easily"]
stem_words = [ps.stem(word) for word in words] 
# print(stem_word) 

# Regex based stemmer 
from nltk.stem import RegexpStemmer

rg = RegexpStemmer('ing$| ily$ | nner&' , min=4) 
words = ["Walking" , "Walked" , "walk" , "easily"]
stem_words = [ps.stem(word) for word in words] 
# print(stem_word) 

# lemmatizer 
from nltk.stem import WordNetLemmatizer 

Lematizzer = WordNetLemmatizer() 

text = "People are running in the fileds" 

docs = Lematizzer(text) 

for doc in docs :
    print(doc) 
