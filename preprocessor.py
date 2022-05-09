import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
from nltk.stem import WordNetLemmatizer
import emoji

nltk.download('wordnet')

# Defining dictionary containing all emojis with their meanings.
emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad', 
          ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
          ':-@': 'shocked', ':@': 'shocked',':-$': 'confused', ':\\': 'annoyed', 
          ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
          '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
          '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink', 
          ';-)': 'wink', 'O:-)': 'angel','O*-)': 'angel','(:-D': 'gossip', '=^.^=': 'cat'}
    
def removeURL(tweet, repstr = 'URL'):
    urlPattern1 = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
    urlPattern2 = r'\b(?!(\D\S*|[12][0-9]{3})\b)\S+\b'
    #txt = re.sub(r'\b(?!(\D\S*|[12][0-9]{3})\b)\S+\b', '', txt)
    #return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())
    tweet = re.sub(urlPattern1,repstr,tweet)
    #tweet = re.sub(urlPattern1,'',tweet)
    tweet = re.sub(urlPattern2,repstr,tweet)
    return tweet

def removeEMOJI(tweet):
    for emoji in emojis.keys():
        tweet = tweet.replace(emoji, "EMOJI" + emojis[emoji])
    return tweet

def removeUSER(tweet, repstr = 'USER'):
    userPattern = '@[^\s]+'
    tweet = re.sub(userPattern, repstr, tweet)
    return tweet

def removeSequencePattern(tweet):
    sequencePattern   = r"(.)\1\1+"
    seqReplacePattern = r"\1\1"
    tweet = re.sub(sequencePattern, seqReplacePattern, tweet)
    return tweet

def removeALPHA(tweet):
    alphaPattern = "[^a-zA-Z0-9]"
    tweet = re.sub(alphaPattern, " ", tweet)
    return tweet

def preprocess(textdata, remove_emoji = False):
    processedText = []
    
    # Create Lemmatizer and Stemmer.
    wordLemm = WordNetLemmatizer()
    
    for tweet in textdata:
        tweet = tweet.lower()
        
        # Replace all URls with 'URL'
        tweet = removeURL(tweet)
        # Replace all emojis.
        if remove_emoji:
            tweet = removeEMOJI(tweet)
        # Replace @USERNAME to 'USER'.
        tweet = removeUSER(tweet)

        # Replace all non alphabets.
        tweet = removeALPHA(tweet)

        # Replace 3 or more consecutive letters by 2 letter.
        tweet = removeSequencePattern(tweet)

        tweetwords = ''
        for word in tweet.split():
            # Checking if the word is a stopword.
            #if word not in stopwordlist:
            if len(word)>1:
                # Lemmatizing the word.
                word = wordLemm.lemmatize(word)
                tweetwords += (word+' ')    
        processedText.append(tweetwords)
    return processedText


def preprocess_VADER(textdata):
    processedText = []
    
    for tweet in textdata:
        #tweet = tweet.lower()
        
        # Replace all URls with 'URL'
        tweet = removeURL(tweet, repstr = '')
        # Replace @USERNAME to 'USER'.
        tweet = removeUSER(tweet, repstr = '')        
        processedText.append(tweet)
    return processedText

def preprocessSingleTweet(tweet):
    # Replace all URls with 'URL'
    tweet = removeURL(tweet, repstr = '')
    # Replace @USERNAME to 'USER'.
    tweet = removeUSER(tweet, repstr = '')
    return tweet