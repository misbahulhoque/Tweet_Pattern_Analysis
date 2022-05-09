import pandas as pd
import csv
import io
import nltk
import re
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

nltk.download('wordnet')

def more_stopwords():
    stop_words = ['a', 'about', 'above', 'across', 'after', 'afterwards']
    stop_words += ['again', 'against', 'all', 'almost', 'alone', 'along']
    stop_words += ['already', 'also', 'although', 'always', 'am', 'among']
    stop_words += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'anymore']
    stop_words += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
    stop_words += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
    stop_words += ['because', 'become', 'becomes', 'becoming', 'been']
    stop_words += ['before', 'beforehand', 'behind', 'being', 'below']
    stop_words += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
    stop_words += ['bottom', 'but', 'by', 'call', 'called', 'can', 'cannot', 'cant', "can’t"]
    stop_words += ['cause','co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
    stop_words += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
    stop_words += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
    stop_words += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
    stop_words += ['every', 'everyone', 'everything', 'everywhere', 'except']
    stop_words += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
    stop_words += ['five', 'for', 'former', 'formerly', 'forty', 'found']
    stop_words += ['four', 'from', 'front', 'full', 'further', 'get', 'getting', 'give']
    stop_words += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
    stop_words += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
    stop_words += ['herself', 'him', 'himself', 'his', 'how', 'however']
    stop_words += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
    stop_words += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
    stop_words += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'like','lets','let','made']
    stop_words += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
    stop_words += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
    stop_words += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
    stop_words += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
    stop_words += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
    stop_words += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
    stop_words += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
    stop_words += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
    stop_words += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
    stop_words += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
    stop_words += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
    stop_words += ['some', 'somehow', 'someone', 'something', 'sometime']
    stop_words += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
    stop_words += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
    stop_words += ['then', 'thence', 'there', 'thereafter', 'thereby']
    stop_words += ['therefore', 'therein', 'thereupon', 'these', 'they']
    stop_words += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
    stop_words += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
    stop_words += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
    stop_words += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
    stop_words += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
    stop_words += ['whatever', 'when', 'whence', 'whenever', 'where']
    stop_words += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
    stop_words += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
    stop_words += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
    stop_words += ['within', 'without', 'would', 'yet', 'you', 'your']
    stop_words += ['yours', 'yourself', 'yourselves']
    stop_words += ['ab', 'abt','b/c', 'B', 'b4','cld','da', 'im', "i’m", "i'm", 'woz', 'wtv','amp', '&amp','&amp;', 
    'u', 'yall', 'thats','youre', 'lol', 'ive','didnt', "didnt'", 'isnt','dont',"don’t",'wa','ha','haha','hah',
    'aint', 'hes', 'doesnt', 'wouldnt','whats', 'theres', 'heres', 'w', 'th', 'https','wont', 'yeah', 'theyre','h']
    return stop_words

def getStopwords(filter_words = None, special_filter = False):
    stop_words = set(stopwords.words('english'))
    if special_filter:
        more = more_stopwords()
        for w in more:
            if w not in stop_words:
                stop_words.add(w)
    if filter_words:
        stop_words = stop_words.union(filter_words)
    return stop_words

def removeStopwords(textList, filter_words = None, special_filter = False):
    processedText = []
    stop_words = getStopwords(filter_words, special_filter)
    for text in textList:
        tokens = ' '.join(s for s in text.split() if s not in stop_words)
        processedText.append(tokens)
    return processedText

def csvFileAppend(filename, row):
    csvfile = io.open(filename, 'a', encoding='utf-8', newline="")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(row)
    csvfile.close()

def read_csv2df(filename):
    df = pd.read_csv(filename, encoding='utf-8')
    return df

def covidKeywords():
    words = "covid covid19 covid2019 covid_19 coronavirus virus COVD COVD19 2019nCoV WuhanVirus wuhan SARSCoV2 SARS novelcoronavirus rona therona missrona outbreak pandemic CoronavirusOutbreak CoronavirusPandemic CoronaOutbreak SocialDistancing StayAtHome StayHome quarantine lockdown mask WearAMask"
    keywords = words.split(" ")
    keywords.append("'corona -beer'")
    return keywords

def isCovidRelated(tweet):
    keywords = covidKeywords()
    for key in keywords:
        if re.search(key, tweet, re.IGNORECASE):
            return True
    return False

def existsKeys(doc, keys):      # return None if kesys not exist
    key = keys.pop(0)
    if key in doc:
        return existsKeys(doc[key], keys) if keys else doc[key]
