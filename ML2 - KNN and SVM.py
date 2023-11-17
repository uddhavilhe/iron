import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split


df = pd.read_csv("C:/Users/UDDHAV ILHE/Desktop/emails.csv")

print(df)

from sklearn.preprocessing import scale
X= df.iloc[:,1:3001]

Y = df.iloc[:,-1].values

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.20)
X_train.shape

from sklearn.neighbors import KNeighborsClassifier

model_knn = KNeighborsClassifier(n_neighbors=5)
model_knn.fit(X_train, y_train)

y_pred = model_knn.predict(X_test)

print("Prediction",y_pred)

from sklearn import metrics
print("KNN accuracy = ",metrics.accuracy_score(y_test,y_pred))

meanAbErr = metrics.mean_absolute_error(y_test, y_pred)
meanSqErr = metrics.mean_squared_error(y_test, y_pred)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
print('R squared: {:.2f}'.format(model_knn.score(X,Y)*100))
print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)

from sklearn.svm import SVC

model_svc = SVC(C = 1)

model_svc.fit(X_train, y_train)

y_pred_svc = model_svc.predict(X_test)

print("Prediction",y_pred_svc)

print("SVM accuracy = ",metrics.accuracy_score(y_test,y_pred_svc))

meanAbErr = metrics.mean_absolute_error(y_test, y_pred_svc)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_svc)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_svc))
print('R squared: {:.2f}'.format(model_svc.score(X,Y)*100))
print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)