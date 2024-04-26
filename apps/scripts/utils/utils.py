from typing import Any
import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet, stopwords
from nltk.stem import WordNetLemmatizer
from datetime import datetime
import joblib
import os

class lemmaToken():
    """
    class for lemmatize tokenizer.

    This class utilized NLTK's wordnet lemmatizer alongside with the stopwords and POS (parts-of-speech) in english version.

    Attributes:
    wordnetLemma (WordNetLemmatizer) : NLTK's instance of WordNetLemmatizer
    stopWords (set) : set of NLTK's stopwords in english

    method:
    getPos(tags:str) -> str:
        determines the given token POS of a certain words in english

    __call__(sentences:str) -> list:
        output the lemmatized of a sentences based on NLTK's lemmatizer in a list
    """
    def __init__(self) -> None:
        """
        initializing an instances for WordNetLemmatizer and NLTK's stopwords
        """
        self.wordnetLemma = WordNetLemmatizer()
        self.stopWords = set(stopwords.words('english'))
    def getPos(self, tags:str) -> str:
        """
        return the POS of a certain tags
        """
        if tags.startswith('J'):
            return wordnet.ADJ
        elif tags.startswith('V'):
            return wordnet.VERB
        elif tags.startswith('N'):
            return wordnet.NOUN
        elif tags.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN
    def __call__(self, sentences:str) -> list[str]:
        """
        return a list of strings of the lemmatized sentence
        """
        tokens = word_tokenize(sentences)
        wordNtokens = nltk.pos_tag(tokens)
        return [self.wordnetLemma.lemmatize(word, pos=self.getPos(tag)) for word, tag in wordNtokens if word.lower() not in self.stopWords]

# def isValidFiles(filePath:str) -> bool:
#     """
#     returning True if the given file path is a valid files, else Error.
#     """
#     try:
#         with open(filePath):
#             pass
#         return True
#     except FileNotFoundError:
#         raise FileNotFoundError(f'File {filePath} not found!')
#     except PermissionError:
#         raise PermissionError(f'File {filePath} access required!')
    
# def exportNow(objName, pref:str, dir:str) -> Any :
#     """
#     Export an object using joblib.dump to a directory.
#     parameters : 
#     objName (Obj) : any python object and must not be empty
#     pref (str) : prefix name of the exported object 
#     dir (str) : path where the exported object will be
#     output : None
#     """
#     if not os.path.exists(dir):
#         raise FileNotFoundError('directory not found')
#     if pref:
#         timeObj = datetime.now()
#         timesNow = [pref, timeObj.year, timeObj.month, timeObj.day]
#         joblib.dump(objName, os.path.join(dir, '_'.join(timesNow)))
#     else:
#         raise ValueError('pref must not empty!')
