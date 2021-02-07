import tensorflow as tf
import numpy as np
from tensorflow import keras
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
xx = np.array ([3,4,2,5,4,3], dtype=float) # number of bedrooms
yy = np.array([229000,399000,250000,347500,289000,97000],dtype=float) #price
yy = yy/100000 #price divided by 100000
model.fit(xx, yy, epochs=2000,verbose=0)

#%%

print(model.predict([2])*100000,
      model.predict([3])*100000,
      model.predict([4])*100000,
      model.predict([5])*100000)
