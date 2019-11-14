
import pandas as pd

dataset1 = pd.read_csv(r'C:\Users\Pg\Downloads\file.csv',header=0)
dataset1.columns
dataset1.head(5)
dataset1.tail(5)
dataset1.shape   #250, 101


'''
https://nces.ed.gov/fastfacts/display.asp?id=28
During the 1970s and early 1980s, public school enrollment decreased while the 
number of teachers generally increased. For public schools, the number of pupils 
per teacher—that is, the pupil/teacher ratio—declined from 22.3 in 1970 to 17.9 
in 1985. After enrollment started increasing in 1985, the public school 
pupil/teacher ratio continued to decline, reaching 17.2 in 1989. After a period 
of relative stability from the late 1980s through the mid-1990s, the ratio 
declined from 17.3 in 1995 to 15.3 in 2008. After 2008, the public school 
pupil/teacher ratio increased, reaching 16.0 in 2015. In comparison, the 
private school pupil/teacher ratio was 11.9 in 2015. The average class size in 
2011–12 was 21.2 pupils for public elementary schools and 26.8 pupils for 
public secondary schools. 
'''
condZambia = dataset1['Education - Pupil-teacher ratio in primary education (headcount basis)']=='Zambia'
dataset2014to2018 = dataset1[['Education - Pupil-teacher ratio in primary education (headcount basis)'
                              ,'1970','1985','1995','2008','2014','2015','2016','2017','2018']]
dataset2014to2018 = dataset2014to2018[condZambia]
#dataset2014to2018.groupby('Education - Pupil-teacher ratio in primary education (headcount basis)').count()

import numpy as np
import matplotlib.pyplot as pt
X = dataset2014to2018['Education - Pupil-teacher ratio in primary education (headcount basis)']
y = dataset2014to2018['2014'].values
y2 = dataset2014to2018['2015'].values
y3 = dataset2014to2018['2016'].values
y4 = dataset2014to2018['2017'].values
y5 = dataset2014to2018['2018'].values
y6 = dataset2014to2018['1970'].values
y7 = dataset2014to2018['1985'].values
y8 = dataset2014to2018['2008'].values
y9 = dataset2014to2018['1995'].values

array1 = np.array(['1970','1985','1995','2008','2014','2015','2016','2017','2018'])
array2 = np.array([y6[0],y7[0],y9[0],y8[0],y[0],y2[0],y3[0],y4[0],y5[0]])

condArgentina = dataset1['Education - Pupil-teacher ratio in primary education (headcount basis)']=='Argentina'
dataset2014to2018 = dataset1[['Education - Pupil-teacher ratio in primary education (headcount basis)'
                              ,'1970','1985','1995','2008','2014','2015','2016','2017','2018']]
dataset2014to2018 = dataset2014to2018[condArgentina]
#dataset2014to2018.groupby('Education - Pupil-teacher ratio in primary education (headcount basis)').count()

X = dataset2014to2018['Education - Pupil-teacher ratio in primary education (headcount basis)']
y = dataset2014to2018['2014'].values
y2 = dataset2014to2018['2015'].values
y3 = dataset2014to2018['2016'].values
y4 = dataset2014to2018['2017'].values
y5 = dataset2014to2018['2018'].values
y6 = dataset2014to2018['1970'].values
y7 = dataset2014to2018['1985'].values
y8 = dataset2014to2018['2008'].values
y9 = dataset2014to2018['1995'].values

array3 = np.array(['1970','1985','1995','2008','2014','2015','2016','2017','2018'])
array4 = np.array([y6[0],y7[0],y9[0],y8[0],y[0],y2[0],y3[0],y4[0],y5[0]])

pt.plot(array1,array2)
pt.plot(array3,array4)
pt.title('Pupil-teacher ratio in primary education in Zambia and Argentina')
pt.xlabel('Year')
pt.ylabel('Pupil-teacher ratio')
pt.show()

'''
It shows that the above claim for the pattern does not match for the country of
Zambia and Argentina
'''

dataset1 = pd.read_csv(r'C:\Users\Pg\Downloads\file.csv',header=0)
dataset2014to2018 = dataset1[['Education - Pupil-teacher ratio in primary education (headcount basis)'
                              ,'1970','1985','1995','2008','2014','2015','2016','2017','2018']]
X = dataset2014to2018['Education - Pupil-teacher ratio in primary education (headcount basis)']
y = dataset2014to2018['2014'].dropna()
y = np.mean(y)
y2 = dataset2014to2018['2015'].dropna()
y2 = np.mean(y2)
y3 = dataset2014to2018['2016'].dropna()
y3 = np.mean(y3)
y4 = dataset2014to2018['2017'].dropna()
y4 = np.mean(y4)
y5 = dataset2014to2018['2018'].dropna()
y5 = np.mean(y5)
y7 = dataset2014to2018['1985'].dropna()
y7 = np.mean(y7)
y8 = dataset2014to2018['2008'].dropna()
y8 = np.mean(y8)
y9 = dataset2014to2018['1995'].dropna()
y9 = np.mean(y9)
array1 = np.array(['1985','1995','2008','2014','2015','2016','2017','2018'])
array2 = np.array([y7,y9,y8,y,y2,y3,y4,y5])

pt.plot(array1,array2)
pt.title('Average Pupil-teacher ratio across countries')
pt.xlabel('Year')
pt.ylabel('Pupil-teacher ratio')

'''
This graph support the above claim that ratio has declined until 2008
and increased until 2015
'''

