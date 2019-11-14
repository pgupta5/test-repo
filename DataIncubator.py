# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from scipy import stats

dataset = pd.read_csv(r'C:\Users\Pg\Downloads\Arrest_Data_from_2010_to_Present.csv',header = 0)
dataset.columns=['Report_ID', 'Arrest_Date', 'Time', 'Area_ID', 'Area_Name',
                        'Reporting_District', 'Age', 'Sex_Code', 'Descent_Code',
                        'Charge_Group_Code', 'Charge_Group_Description', 'Arrest_Type_Code',
                        'Charge', 'Charge_Description', 'Address', 'Cross_Street', 'Location']

dataset['Arrest_Date'] = dataset['Arrest_Date'].str[-4:]

'''
How many bookings of arrestees were made in 2018?
'''
datasetYear2018 = dataset.loc[dataset['Arrest_Date'] == '2018']
print(datasetYear2018.shape)

'''What is the 95% quantile of the age of the arrestee in 2018? 
Only consider the following charge groups for your analysis'''

group1 = (dataset['Charge Group Description'] == 'Vehicle Theft')
group2 = (dataset['Charge Group Description'] == 'Robbery')
group3 = (dataset['Charge Group Description'] == 'Burglary')
group4 = (dataset['Charge Group Description'] == 'Receive Stolen Property')

datasetYearGroup = datasetYear2018.loc[group1 | group2 | group3 | group4]

datasetYearGroup.Age.quantile(0.95)

'''
There are differences between the average age of an arrestee for the various 
charge groups. Are these differences statistically significant? For this 
question, calculate the Z-score of the average age for each charge group. 
Report the largest absolute value among the calculated Z-scores.
1. Only consider data for 2018
2. Do not consider "Pre-Delinquency" and "Non-Criminal Detention" as these 
charge groups are reserved for minors
3.Exclude any arrests where the charge group description is not known
'''

datasetYear2018.groupby('Area_ID')['Report_ID'].count()
datasetYear2018Filter = datasetYear2018[datasetYear2018.Charge_Group_Description != 'Pre-Delinquency']
datasetYear2018Filter = datasetYear2018Filter[datasetYear2018Filter.Charge_Group_Description != 'Non-Criminal Detention']
datasetYear2018Filter = datasetYear2018Filter[datasetYear2018Filter.Charge_Group_Description != '']
Zscores = stats.zscore(datasetYear2018Filter.groupby('Charge_Group_Code')['Age'].mean())
maximumZ = np.amax(Zscores)

'''
Felony arrest incidents have been dropping over the years. 
Using a trend line (linear estimation) for the data from 2010 and 
2018 (inclusive), what is the projected number of felony arrests in 2019? 
Round to the nearest integer. Note, the data set includes arrests for 
misdemeanor, felonies, etc.
'''
dataset2010B2018 = dataset.loc[(dataset['Arrest_Date'] <= '2018') & (dataset['Arrest_Date'] >= '2010')]
dataset2010B2018Fel = dataset2010B2018[dataset2010B2018.Arrest_Type_Code == 'F']
YearFel = dataset2010B2018Fel.groupby('Arrest_Date')['Report_ID'].count()
X = np.arange(2010,2019,1).reshape(-1,1)
y = YearFel
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X,y)
regressor.score(X,y)
y_pred = regressor.predict(np.arange(2019,2020,1).reshape(-1,1))

'''
How many arrest incidents occurred within 2 km from the Bradbury Building in 2018? 
Use (34.050536, -118.247861) for the coordinates of the Bradbury Building . 
For simplicity, please use the spherical Earth projected to a plane equation for 
calculating distances. Use the radius of the Earth as 6371 km. Note, some arrest 
records are missing location data and the location is listed as (0, 0). 
These records should not factor in your calculation.
'''
import math
datasetYear2018LocNNull = datasetYear2018[datasetYear2018['Location'] != '(0.0, 0.0)']
destination = list(datasetYear2018LocNNull['Location'])
coorSplit = []
final = []
dist2=[]
originX = 34.050536
originY = -118.247861

for x in destination:
    x = x[1:-1]
    coorSplit.append(list(map(float, x.split(','))))

for x in coorSplit:
    dist2.append(math.sqrt((math.radians(x[0]-(originX)))**2 + (math.radians(x[1]-(originY)))**2))
for x in dist2:
    if x <= .002:
        final.append(x)

'''
How many arrest incidents were made per kilometer on Pico Boulevard during 2018? 
For this question, we will need to estimate the length of Pico Boulevard, which 
mostly stretches from east to west. To estimate the length of Pico Boulevard:
1. Consider all location data which the listed address mentions "Pico".
2. Remove outliers by filtering out locations where either the latitude or 
longitude is 2 standard deviations beyond the mean of the subset of identified 
points.
3. To estimate the length, calculate the distance from the most western and 
eastern coordinate points. Use the spherical Earth projected to a plane 
equation for calculating distances.
Once you have estimated the length of Pico Boulevard, you can proceed to report 
the number of arrest incidents per kilometer on Pico Boulevard in 2018.
'''
import numpy as np
import math
finalList=[]
coorSplit =[]
dataset2018Pico = datasetYear2018[datasetYear2018.Address.str.contains('PICO')]
for x in list(dataset2018Pico['Location']):
    x = x[1:-1]
    coorSplit.append(list(map(float, x.split(','))))

mean = np.mean(coorSplit, axis=0)
sd = np.std(coorSplit, axis=0)
for x in coorSplit:
    if x[0] > mean[0] - 2 * sd[0]:
        if x[1] > mean[1] - 2 * sd[1]:
            finalList.append(x)
    if x[0] > mean[0] + 2 * sd[0]:
        if x[1] > mean[1] + 2 * sd[1]:
            finalList.append(x)         
        
for i in range(1,len(finalList)):
    if (finalList[i][0] > finalList[i-1][0]):
        a1 = finalList[i][0]
        b1 = finalList[i][1]
    
for i in range(1,len(finalList)):
    if (finalList[i][1] > finalList[i-1][1]):
        a2 = finalList[i][0]
        b2 = finalList[i][1]

finalDistance = math.sqrt((a1-a2)**2 + (b1-b2)**2)
finalDistance =(math.sqrt((math.radians(a1-(a2)))**2 + (math.radians(b1-(b2)))**2))
print(len(finalList)/(finalDistance*1000))

'''
Some types of arrest incidents in certain areas occur at a highly 
disproportionate rate compared to their frequency city-wide. For example, 
let's say that the rate of larceny arrests (charge group code 6) is 1% in 
Devonshire (area ID 17). This rate may appear low but what if larceny arrests 
constitute 0.1 % city-wide? The ratio between these two probabilities is 10 and 
we can say that larceny occurs unusually often in Devonshire (Note, these 
numbers were made up for illustration purposes). Calculate this ratio for all 
charge group code and area ID pairs. You can view this ratio as the ratio of 
the conditional probability of an arrest incident of a charge group code given 
that it occurred in an area ID to the unconditional probability of the arrest 
incident of a charge group. Report the average of the top 5 of the calculated 
ratio.
1. Consider all records prior to January 1, 2019.
2. Some arrest incidents don't have a charge group code. These records should 
not be considered in your analysis.
3. Arrest incidents for charge group code 99 should not be considered in your 
analysis.
'''
datasetYearUpto2019 = dataset.loc[dataset['Arrest_Date'] < '2019']
datasetYearUpto2019N = datasetYearUpto2019.dropna(axis=0, subset=['Charge_Group_Code'])
datasetYearUpto2019N = datasetYearUpto2019N[datasetYearUpto2019N['Charge_Group_Code'] != 99]
ArrestPerChargeArea = datasetYearUpto2019N.groupby(['Charge_Group_Code','Area_ID'])['Report_ID'].count()/datasetYearUpto2019N.groupby(['Charge_Group_Code'])['Report_ID'].count()
print(ArrestPerChargeArea)
print(ArrestPerChargeArea.nlargest().mean())
