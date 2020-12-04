#Usage: python predict-multiclass.py
#https://github.com/tatsuyah/CNN-Image-Classifier

import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import tensorflow as tf

img_width, img_height = 150, 150
model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)



        

def predict(file):
  x = load_img(file, target_size=(img_width,img_height))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  global graph
  graph = tf.get_default_graph()
  with graph.as_default():
      array = model.predict(x)
      result = array[0]
      answer = np.argmax(result)
  if answer == 0:
    print("Label: Dog")
  elif answer == 1:
    print("Label: Person")
  #elif answer == 2:
    #print("Label: Dog-Person")

  return answer

dog_t = 0
dog_f= 0
person_t = 0
person_f = 0


for i, ret in enumerate(os.walk('./test-data/dog')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
  
    result = predict(ret[0] + '/' + filename)
    if result == 0:
      dog_t += 1
    else:
      dog_f += 1

for i, ret in enumerate(os.walk('./test-data/person')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    
    result = predict(ret[0] + '/' + filename)
    if result == 1:
      person_t += 1
    else:
      person_f += 1



"""
Check metrics
"""
print("True Dog: ", dog_t)
print("False Dog: ", dog_f)
print("True Person: ", person_t)
print("False Person: ", person_f)

