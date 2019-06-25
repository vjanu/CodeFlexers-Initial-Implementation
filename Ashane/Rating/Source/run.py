from flask import jsonify,Flask
import re
from nltk.stem import PorterStemmer
from train import dataset,feature_set,no_of_items,words

ps = PorterStemmer()

# To calculate the basic probability of a word for a category
def calc_prob(word,category):
	if word not in feature_set or word not in dataset[category]:
		return 0

	return float(dataset[category][word])/no_of_items[category]

# Weighted probability of a word for a category
def weighted_prob(word,category):
	# basic probability of a word - calculated by calc_prob
	basic_prob=calc_prob(word,category)

	# total_no_of_appearances - in all the categories
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
		if ' ' in i:
			i=i.split(' ')
			for j in i:
				if j not in data:
					data.append(j.lower())
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
	for i in dataset.keys():
		# Category Probability
		# Number of items in category/total number of items
		cat_prob=float(no_of_items[i])/sum(no_of_items.values())
		# p(test data | category)
		test_prob1=test_prob(test,i)
		results[i]=test_prob1*cat_prob     
	return results  
    
app = Flask(__name__)

@app.route("/sentiment/<string:sentence>")
def main(sentence):
   
    #TODO:Enter the word which has to be tested
    text = sentence

    #Replace the unbiased words
    for word in words:
        text=text.replace(word,' ')
    result = naive_bayes(text)

    print (text)
    print (result)
    inverse = [(value, key) for key, value in result.items()]
    resultRating = max(inverse)[1]
    minVal = min(inverse)[0]
    maxVal = max(inverse)[0]
    # print (min(inverse)[0])
    if(minVal==maxVal):
        print ("Rating cannot be predicted")
        sentimentType="Rating cannot be predicted"
        resultRating = 3
    elif ((resultRating == '1') or (resultRating == '2')):
        sentimentType="negative"
        print ("negative")
    elif (resultRating == '3'):
        sentimentType="neutral"
        print ("neutral")
    else:
        sentimentType="positive"
        print ("positive")
    print (resultRating)
    
    data =[{'InputSentiment' : sentence ,'ResultRating' : resultRating,'Type':sentimentType}]
    
    return jsonify(data), 200
    #return jsonify(
   #     InputSentiment = sentence,
  #      ResultRating = resultRating,
   #     Type = sentimentType
  #  )    
    
app.run(debug=False,host="0.0.0.0",port=8090)
#if (__name__ == __main__):
#    app.run(debug=true,host="0.0.0.0",port=8090)    
