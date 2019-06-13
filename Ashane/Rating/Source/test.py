import re
import csv
from nltk.stem import PorterStemmer
from train import dataset,feature_set,no_of_items,words

ps = PorterStemmer()

print ("\n------------no_of_items ==> {rating : number of sentenses in training data with relavent rating}---------------\n")
print (no_of_items)
print ("\n--------------dataset ==>rating:{['word':total number of occurances in given rating]}-----------------\n")
print (dataset)
print ("\n------------feature_set ==> word : {['rating':number of occurances]}---------------\n")
print (feature_set)
print ("\n--------------------------------------\n")

# To calculate the basic probability of a word for a given category
# (total number of occurances of a given word in a given rating category / total number of occurances of given rating category) 
def calc_prob(word,category):
	if word not in feature_set or word not in dataset[category]:
		return 0
	return float(dataset[category][word])/no_of_items[category]

# Weighted probability of a word for a category
def weighted_prob(word,category):
	# basic probability of a word for given category
	# probability of a word given category
	basic_prob=calc_prob(word,category)

	# total_no_of_appearances - in all the categories
	# total sum of all occurances of given word in all rating categories
	if word in feature_set:
		tot=sum(feature_set[word].values())
	else:
		tot=0
		
	# Weighted probability is given by the formula
	# (weight*assumedprobability + total_no_of_appearances*basic_probability)/(total_no_of_appearances+weight)
	# weight by default is taken as 1.0
	# assumed probability is 0.5 here
	weight_prob=((1.0*0.5)+(tot*basic_prob))/(1.0+tot)
	return weight_prob

# To get probability of the test data for the given category
def test_prob(test,category):
	# Split the test data
	split_data=re.split('[^a-zA-Z\']',test)

	data=[]
	for i in split_data:
		#for a sentence with several words seperated by space
		if ' ' in i:
			i=i.split(' ')
			for j in i:
				#add the words to data[] which are not in 'data' array. 
				if j not in data:
					data.append(j.lower())
		#for a sentiment with single word
		elif len(i) > 2 and i not in data:
                    i = ps.stem(i)
                    data.append(i.lower())
	p=1
	for i in data:
		p*=weighted_prob(i,category)
	return p

# Naive Bayes implementation
def naive_bayes(test):
	'''
		p(A|B) = p(B|A) * p(A) / p(B)

		Assume A - Category
			   B - Test data
			   p(A|B) - Category given the Test data

		Here ignoring p(B) in the denominator (Since it remains same for every category)
	'''
	results={}
    
    #for ratings 1/2/3/4/5
	for i in dataset.keys():
		# p(A)
		# Category Probability
		# Number of items in category/total number of items
        # EX: no.of sentences with rating 1 in dataset / total number of sentences in dataset
		cat_prob=float(no_of_items[i])/sum(no_of_items.values())

		# p(B|A)
		# p(test data | category)
		test_prob1=test_prob(test,i)

		# p(B|A) * p(A) 
		results[i]=test_prob1*cat_prob
	return results

print ("---Started testing the accuracy---")

#TODO:Insert the correct file
#To check the accuracy of the exact same data which was trained
fh = open("TEST_DATASET/test_case1.csv","r")

reader = csv.reader(fh, delimiter='+')
correct = 0
incorrect = 0
accuracy = 0
correctPositive = 0
correctNegative = 0
accuracyPositive =0
for row in reader:
    for word in words:
        row[0]=row[0].replace(word,' ')

    text = row[0]
    result = naive_bayes(text)
    inverse = [(value, key) for key, value in result.items()]
    outputRating = max(inverse)[1]

    if(max(inverse)[0] != min(inverse)[0]):
        if (int(outputRating) > 3):
            RatingString = "Positive"
        else:
            RatingString = "Negative"

        if (int(row[1]) > 3):
            DocString = "Positive"
        else:
            DocString = "Negative"

        if (RatingString == DocString):
            correctPositive = correctPositive + 1
        else:
            correctNegative = correctNegative + 1

        if (outputRating == row[1]):
            correct = correct + 1
            print(row)

            #with open('test_case1.csv', mode='a') as employee_file:
             #   employee_writer = csv.writer(employee_file,delimiter='+')
              #  employee_writer.writerow(row)

        else:
            incorrect = incorrect + 1

totalSentiment = correct + incorrect
accuracy = (correct/totalSentiment)*100
print ("\n-----Testing for the exact value-----")
print("No. of correct matches of values   :",correct)
print("No. of incorrect matches of values :",incorrect)
print("                                  ------------------------",)
print("Accuracy of exact matches [%]      :",accuracy)

totalPositivity = correctPositive + correctNegative
accuracyPositive = (correctPositive/totalPositivity)*100
print ("\n---Testing for the positive/negative sentiment identification---")
print("No. of correct matches for sentiment classification   :",correctPositive)
print("No. of incorrect matches for sentiment classification :",correctNegative)
print("                                                     ---------------------",)
print("Accuracy of sentiment classification [%]              :",accuracyPositive)
print ("\n---Testing completed---")
    
    
