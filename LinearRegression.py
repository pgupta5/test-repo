
import pandas as pd

dataset1 = pd.read_csv(r'C:\Users\Pg\Downloads\file.csv',header=0)

#condZambia = dataset1['Education - Pupil-teacher ratio in primary education (headcount basis)']=='Zambia'
dataset2014to2018 = dataset1[['1970','1985','1995','2008','2014','2015','2016','2017','2018']]
#dataset2014to2018 = dataset2014to2018[condZambia]
#dataset2014to2018.groupby('Education - Pupil-teacher ratio in primary education (headcount basis)').count()
dataset2014to2018=dataset2014to2018.fillna(dataset2014to2018.median())

X = dataset2014to2018.iloc[:, :-1].values
y = dataset2014to2018.iloc[:, dataset2014to2018.shape[1]-1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection  import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                    test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

regressor.score(X_test,y_test)