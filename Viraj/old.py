# K-Means Clustering

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

df = pd.read_csv('users.csv')

#get the userID of the passenger(Frontend fetch)
UID = 179477

#get the index of the row which belongs to particular passenger
index = df[df['UID']== UID].index.values.astype(int)[0]
#print(df.iloc[index]) # print data of the row
#print(df[df['UID']== UID].iloc[:,11]) # print data of the row
#print(df[df['UID']== UID].iloc[:,12]) # print data of the row
#print(df[df['UID']== UID].iloc[:,13]) # print data of the row
#print(df[df['UID']== UID].iloc[:,14]) # print data of the row
#print(df[df['UID']== UID].iloc[:,10]) # print data of the row


#get the properties of the specified user and assign it to variables
isSmoking = df[df['UID']== UID].iloc[:,7].values[0]
isMusicLover = df[df['UID']== UID].iloc[:,8].values[0]
isMotionSickness = df[df['UID']== UID].iloc[:,9].values[0]
isLikeQuietness = df[df['UID']== UID].iloc[:,10].values[0]
isGenderPrefered = df[df['UID']== UID].iloc[:,6].values[0]



#Defining rules for the filteration
#todo add more rules - language spoken?
def rules(smokingFlag, musicFlag, motionFlag, quietnessFlag, genderFlag):
	df.loc[(df['Smoking'] == smokingFlag) & (df['Music_Lover'] == musicFlag) & (df['Motion_Sickness'] == motionFlag) & (df['Gender_Preference'] == genderFlag) 
	& (df['Like_Quietness'] == quietnessFlag)].to_csv('newUsers.csv', index=False);
	
	

#Execute rule based mechanism 
rules(isSmoking, isMusicLover, isMotionSickness, isLikeQuietness, isGenderPrefered);


dataset = pd.read_csv('newUsers.csv')
X = dataset.iloc[:,[3,4]].values # read columns Age-x axis and Profession-y axis

# Using the elbow method to find the optimal number of clusters

from sklearn.cluster import KMeans
wcss =[]
for i in range (1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter =200, n_init = 10, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_) #Within Cluster Sum of Squares

# Plot the graph to visualize the Elbow Method to find the optimal number of cluster  
#plt.plot(range(1,11),wcss)
#plt.title('The Elbow Method')
#plt.xlabel('Number of clusters')
#plt.ylabel('WCSS')
#plt.show()

# Applying KMeans to the dataset with the optimal number of cluster

kmeans=KMeans(n_clusters = 3, init = 'k-means++', max_iter = 200, n_init = 10, random_state = 0)
Y_Kmeans = kmeans.fit_predict(X)
#print(kmeans.cluster_centers_) #cluster center points
#print(kmeans.labels_==1) #cluster center points
# Visualising the clusters

#get clusters and sort them into new file
dataset["Cluster"] = Y_Kmeans
dataset.sort_values(by='Cluster',  inplace=True)
dataset.to_csv('final.csv', index=False)

#specify the cluster where the particular passenger belongs to
n = dataset[dataset['UID']== UID].iloc[:,11].values[0]


#ds = X[np.where(kmeans.labels_== n)] #get particular cluster
#print(ds)
#print(dataset.loc[dataset['Cluster'] == n])

#Initialize lists required
uIDList= list()
filteredList=list()

dataListOfSuitableDrivers = dataset.loc[dataset['Cluster'] == n, ['UID']]
uIDList = dataListOfSuitableDrivers.values.tolist()
# remove reported drivers from the list(uIDList - entries from db)

print(uIDList)

dataListOfSuitableDrivers.to_csv('selectedDrivers.csv', index=False)
#uIDList.append(dataListOfSuitableDrivers.get('UID'))
	
#database call to get reported list for particular UID
#filteredList = uIDList - [1,2,3,4,5]

dataset = pd.DataFrame(filteredList)
dataset.to_csv('selectedDrivers.csv')
#with open("selectedDrivers.csv","w") as f:
 #   wr = csv.writer(f,delimiter="\n")
  #  wr.writerow(uIDList)
	
#for x in uIDList:
	#print(x) #dummy printing the list
	
#print(dataset[kmeans.labels_== n]) # get dataset in each cluster
#print(dataset['UID']== UID) # get true for paticular row
#print(dataset[dataset['UID']== UID].index.values.astype(int)[0]) # get index of row which has UID index



	
plt.scatter(X[Y_Kmeans == 0, 0], X[Y_Kmeans == 0,1],s = 100, c='red', label = 'Cluster 1')

plt.scatter(X[Y_Kmeans == 1, 0], X[Y_Kmeans == 1,1],s = 100, c='blue', label = 'Cluster 2')

plt.scatter(X[Y_Kmeans == 2, 0], X[Y_Kmeans == 2,1],s = 100, c='green', label = 'Cluster 3')


plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s = 300, c = 'yellow', label = 'Centroids')

    
plt.title('Clusters of drivers')
plt.xlabel('Age')
plt.ylabel('Profession')
plt.legend()
plt.show()
