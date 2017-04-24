from keras.models import Sequential
from keras.layers import Dense
import numpy
from keras import optimizers
# fix random seed for reproducibility
numpy.random.seed(7)

# load pima indians dataset
dataset = numpy.loadtxt("BostonData2.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:5]
Y = dataset[:,5]
# create model
model = Sequential()
model.add(Dense(9, init='normal',input_dim=5, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='SGD', metrics=['accuracy'])

# Fit the model
model.fit(X, Y, epochs=100, batch_size=1000,verbose=2)

# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# calculate predictions
predictions = model.predict(X)
print(predictions)



