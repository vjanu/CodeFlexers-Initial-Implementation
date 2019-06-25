import re
import csv
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()
stop_words = set(stopwords.words('english')) 
#print(stop_words)

#Unbiased words are eliminated
#words=[]
words=['Uber','uber','UBER',' the ',' The ',' are ',' was ',' were ',' she ',' they ',' their ',' her ',' him ',' his ',' and ',' And ']
#words=stop_words

#TODO:Insert the correct file
fh=open("TRAIN_DATASET/total_training_data.csv","r")

# The delimiter in the csv file is '+' instead of comma. This was done to compromise with the commas in the sentence in the sentence of the dataset used.
reader = csv.reader(fh, delimiter='+')

# It is the dictionary that has the data : { label(5/4/3/2/1) : { word : count of number of occurences of the word } }
dataset={}

# It is the dictionary that keeps the count of records that are labeled a label l for each label l
# That is, { label l : No. of records that are labeled l }
no_of_items={}

# This is the dictionary that contains the count of the occurences of word under each label
# That is, { word : { label l : count of the occurence of word with label l } }
feature_set={}

# For each sentence in dataset
# row[1] = rating number(5/4/3/2/1)
# row[0] = relavent sentiment
for row in reader:
	#print("###############")
	#wordstemming = word_tokenize(row[0])
	#for w in wordstemming:
    		#print(ps.stem(w))

	#To replace the unbiased words from the string	
	for word in words:		
		row[0]=row[0].replace(word,' ')
	# Initialize the label in the dictionary if not present already
	no_of_items.setdefault(row[1],0)
	# Increase the count of occurence of label by 1 for every occurence
	no_of_items[row[1]]+=1
	# Initialize the dictionary for a label if not present
	dataset.setdefault(row[1],{})

	# Split the sentence with respect to non-characters, and do not split if apostophe is present
	split_data=re.split('[^a-zA-Z\']',row[0])
	
	# For every word in split data
	for i in split_data:      
        # Removing stop words to a small extent by ignoring words with less length 
		#TODO: when the unnecessary words are removed,accuracy increases
		#if len(i) > 4:
		if len(i) > 2:

			#stemming the words to make common words like drive,driving -> drive
			#print(ps.stem(i))
			i = ps.stem(i)

			# Initialize the word count in dataset
			dataset[row[1]].setdefault(i.lower(),0)
			# Increase the word count on its occurence with label row[1]
			dataset[row[1]][i.lower()]+=1
			# Initialze a dictionary for a newly found word in feature set
			feature_set.setdefault(i.lower(),{})
			# If the label was found for the word, for the first time, initialize corresponding count value for word as key
			feature_set[i.lower()].setdefault(row[1],0)
			# Increment the count for the word in that label 
			feature_set[i.lower()][row[1]]+=1

	



			
