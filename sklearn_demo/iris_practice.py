from sklearn.datasets import load_iris
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target
poly = PolynomialFeatures(3).fit_transform(x, y)
print(poly)

X_train, X_test, y_train, y_test = train_test_split(poly, y, test_size=0.3, random_state=4)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

y_predit = knn.predict(X_test)

print(y_test)
print(y_predit)
print(knn.score(X_test, y_test))

k_range = range(1, 31)
k_score = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, x, y, cv=10, scoring='accuracy')
    k_score.append(scores.mean())

plt.plot(k_range,k_score)
plt.show()