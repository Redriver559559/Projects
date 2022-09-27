#just messing around with sklearns training models (very cool)

import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
from skimage import io
from sklearn.model_selection import train_test_split
from sklearn import datasets
faces = sk.datasets.fetch_olivetti_faces
from sklearn.metrics import f1_score
from sklearn.neighbors import KNeighborsClassifier
digits = sk.datasets.load_digits()

plt.style.use("ggplot")

digit_images = digits.images
target_names = digits.target

#shape of image is an 8x8 2D array




X_train, X_test, y_train, y_test = train_test_split(digits.images, digits.target, test_size=0.33, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)
X_train_samples, x, y = X_train.shape
X_train_data = X_train.reshape((X_train_samples, x*y))
knn.fit(X_train_data, y_train)

def predict_data(test_data):
  samples, x, y = test_data.shape
  data = test_data.reshape((samples, x*y))
  y_prediction = knn.predict(data)
  return y_prediction

y_prediction = predict_data(X_test)

scores = f1_score(y_test, y_prediction, average='weighted')
print(scores)
print(f'{scores*100:.2f}% correct out of {len(X_test)} samples')


from skimage import io

#please provide an image that is 8x8 pixels
#use white on black
image_path = ''
image = io.imread(image_path, as_gray=True)*10

plt.matshow(image)
image = np.reshape(image, (1, image.shape[0], image.shape[1]))
#shape of image is an 8x8 2D array
plt.gray()
plt.show()
y_prediction = predict_data(image)
print(f'Prediction: {y_prediction}')
