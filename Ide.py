# cook your dish here
import tensorflow as tf
from tensorflow import keras
import numpy as np
fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
              
 train_images = train_images / 255.0

test_images = test_images / 255.0
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10)
test_acc = model.evaluate(test_images,  test_labels, verbose=2)
test_acc = test_acc[1]*100

# storing accuracy
import os
os.system("sudo touch /task3/accuracy.txt")
os.system("echo {} > /task3/accuracy.txt".format(text_acc))

# saving the model to send to the clien