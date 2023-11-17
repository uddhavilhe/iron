import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv("C:/Users/UDDHAV ILHE/Desktop/diabetes.csv")
print(data)

data.head()

df = data.isnull().sum()
print(df)

for column in data.columns[1:-3]:
    data[column].replace(0, np.NaN, inplace = True)
    data[column].fillna(round(data[column].mean(skipna=True)), inplace = True)
df1 =  data.head(10)

print(df1)

X = data.iloc[:, :8] #Features
Y = data.iloc[:, 8:] #Predictor

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2,
random_state=0)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn_fit = knn.fit(X_train, Y_train.values.ravel())
knn_pred = knn_fit.predict(X_test)

from sklearn.metrics import confusion_matrix, precision_score, recall_score,f1_score , accuracy_score
print("Confusion Matrix")
print(confusion_matrix(Y_test, knn_pred))
print("Accuracy Score:", accuracy_score(Y_test, knn_pred))
print("Reacal Score:", recall_score(Y_test, knn_pred))

print("F1 Score:", f1_score(Y_test, knn_pred))
print("Precision Score:",precision_score(Y_test, knn_pred))