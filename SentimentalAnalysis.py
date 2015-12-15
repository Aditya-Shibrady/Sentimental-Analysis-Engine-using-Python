#!/usr/bin/env python

import nltk, random, csv, sys
from nltk.corpus import names
from nltk.tokenize import word_tokenize
from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger
from textblob import TextBlob

def selectTweets(row):
    tweetWords = []
    words = row[0].split()
    for i in words:
        i = i.lower()
        i = i.strip('@#\'"?,.!')
        tweetWords.append(i)
    row[0] = tweetWords

    if counter <= 11600:
        trainTweets.append(row)
    else:
        testTweets.append(row)
def evaluate_features(feature_select):
    posFeatures = []
    negFeatures = []
    #breaks up the sentences into lists of individual words (as selected by the input mechanism) and appends 'pos' or 'neg' after each list
    with open('rt-polarity.pos', 'r') as posSentences:
        for i in posSentences:
            posWords = re.findall(r"[\w']+|[.,!?;]", i.rstrip())
            posWords = [feature_select(posWords), 'positive']
            posFeatures.append(posWords)
    with open('rt-polarity.neg', 'r') as negSentences:
        for i in negSentences:
            negWords = re.findall(r"[\w']+|[.,!?;]", i.rstrip())
            negWords = [feature_select(negWords), 'negative']
            negFeatures.append(negWords)

    trainFeatures = posFeatures + negFeatures
    #trains a Naive Bayes Classifier
   
def make_full_dict(words):
    return dict([(word, True) for word in words])

trainTweets = []
testTweets = []
trainFeatures = []

print "Tweet Sentiment Analyzer"
print "*" * 30


filename =  "dataset.csv"   
            
            #Open file
with open(filename, 'rb') as csvfile: 
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
                
                #Print succes message
    print "> File opened successfully!"
                
    counter = 0
    for row in reader:
        selectTweets(row)
        counter += 1
                    
    print "> Wait a sec for the results..."
                    
    cl = NaiveBayesClassifier(trainTweets)
                
             
    print "> add another data set"
    cl.update(trainFeatures)  
    print "> finish combination"
    cl.show_informative_features(10)


    outputPos=open('positiveTweet.txt','a')
    outputNeg=open('negativeTweet.txt','a')
    dataset = str(raw_input("> Please enter a filename contains tweets: ")) 
    with open(dataset) as f:
         out = f.readlines()   
         for lines in out:
            tweetWords = []
            words = lines.split()
            for i in words:
                i = i.lower()
                i = i.strip('@#\'"?,.!')
                tweetWords.append(i)
                tweet = ' '.join(tweetWords)
            if(cl.classify(tweet)=="positive"):
                outputPos.write(lines)
            else:
                outputNeg.write(lines)                           
                  
                
        
