from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)



# load pima indians dataset
dataset = numpy.loadtxt("Boston.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:5]
Y = dataset[:,5]


# create model
model = Sequential()
model.add(Dense(12, input_dim=5, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile model
model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X, Y, epochs=300, batch_size=200,verbose=1)

# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))