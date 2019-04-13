import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt

# ******
# mining
# *****
mnist = input_data.read_data_sets('./mnist/data/', one_hot=True)

# ******
# modeling
# *****


X = tf.placeholder(tf.float32, [None, n_step, 784])
Y = tf.placeholder(tf.float32, [None, 10])
keep_prob=tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_normal([784,256],stddev=0.01))
L1=tf.nn.relu(tf.matmul(X,w1))
L1=tf.nn.dropout(L1,keep_prob)











































