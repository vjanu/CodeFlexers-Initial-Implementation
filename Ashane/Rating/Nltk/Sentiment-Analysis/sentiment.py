### REFER - https://www.nltk.org/_modules/nltk/classify/naivebayes.html , https://www.nltk.org/book/ch06.html

import nltk
import re
import csv

neg=open("negative.csv",encoding="utf8")
pos=open("positive.csv",encoding="utf8")
reader = csv.reader(neg, delimiter='+')
reader1 = csv.reader(pos, delimiter='+')
pos_tweets=[]
neg_tweets=[]

for row in reader1:
    pos_tweets.append(row)
# pos_tweets = [('I love this car', '5'),
#               ('This view is amazing', '5'),
#               ('I feel great this morning', '3'),
#               ('I am so excited about the concert', '4'),
#               ('He is my best friend', '3')]

#print(pos_tweets)
for row in reader:
    neg_tweets.append(row)
# neg_tweets = [('I do not like this car', '1'),
#               ('This view is horrible', '1'),
#               ('I feel tired this morning', '2'),
#               ('I am not looking forward to the concert', '1'),
#               ('He is my enemy', '2')]
#print(neg_tweets)

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    tweets.append((words_filtered, sentiment))
    #print(tweets)
test_tweets = [
    (['feel', 'happy', 'this', 'morning'], 'positive'),
    (['larry', 'friend'], 'positive'),
    (['not', 'like', 'that', 'man'], 'negative'),
    (['house', 'not', 'great'], 'negative'),
    (['your', 'song', 'annoying'], 'negative')]

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)    
    #print (wordlist)
    word_features = wordlist.keys()
    #print (word_features)    
    return word_features


def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words


#print nltk.FreqDist(get_words_in_tweets(tweets))
#print (get_word_features(get_words_in_tweets(tweets)))
word_features = get_word_features(get_words_in_tweets(tweets))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

tweet = 'Driver sucks'
print (classifier.classify(extract_features(tweet.split())))
