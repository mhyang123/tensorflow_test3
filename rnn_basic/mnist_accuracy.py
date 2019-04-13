'''

import  tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#****
#mining
#****
mnist=input_data.read_data_sets('./mnist/data/',one_hot=True)

#--------------
#MODELING
#-----------------
#옵션
learing_rate=0.01
total_epoch=30#총 회전수
batch_size=128#한번에 입력받는 갯수

n_input =28#가로 픽셀
n_step =28#세로 픽셀
n_hidden=128
n_class=10#10단계

X=tf.placeholder(tf.float32,[None,n_step,n_input])
Y=tf.placeholder(tf.float32,[None,n_class])
W=tf.Variable(tf.random_normal(n_hidden,n_class))
b=tf.variable(tf.random_normal(n_class))

cell=tf.nn.raw_rnn_cell.BasicLSTMCell(n_hidden)
outputs,states=tf.nn.dynamic_rnn(cell,X,dtype=tf.float32)
outputs=tf.transpose(outputs,[1,0,2])
model=tf.matmul(outputs,W)+B
cost=tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits_v2(lgits=model,labels=Y))
optimizer=tf.train.AdadeltaOptimizer(learing_rate).minimize(cost)
#---
#learing
#-----------
sess=tf.Session()
sess.run(tf.global_variables_initializer())
total_batch=int(mnist.train.num_examples/batch_size)
for epoch in range(total_batch):
    total_cost=0
    for i in rang(total_batch):
        batch_xs,batch_ys=mnist.train.next_batch(batch_size0)
        batch_xs=batch_xs.reshape(batch_size,n_step,n_input)
        _, cost_val = sess.run([optimizer, cost],
                               {X: batch_xs, Y: batch_ys})
        total_cost += cost_val
    print('Epoch: ', '%04d' % (epoch + 1),
          'Avg. cost =',
          '{:.3f}'.format(total_cost / total_batch))
    print('최적화 완료')

#***
#test
#****
is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
test_batch_size = len(mnist.test.images)
test_xs = mnist.test.images.reshape(test_batch_size, n_step, n_input)
test_ys = mnist.test.labels

print('정확도: ', sess.run(accuracy, {X: test_xs, Y: test_ys}))
'''
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# ******
# mining
# *****
mnist = input_data.read_data_sets('./mnist/data/', one_hot=True)
# ******
# modeling
# *****
# 옵션
learning_rate = 0.01
total_epoch = 30 # 총 회전수
batch_size = 128 # 한번에 입력받는 갯수

n_input = 28 # 가로픽셀
n_step = 28 # 세로픽셀
n_hidden = 128
n_class = 10 # 10단계

X = tf.placeholder(tf.float32, [None, n_step, n_input])
Y = tf.placeholder(tf.float32, [None, n_class])
W = tf.Variable(tf.random_normal([n_hidden, n_class]))
b = tf.Variable(tf.random_normal([n_class]))

cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden)
outputs, states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)
outputs = tf.transpose(outputs, [1, 0, 2])
outputs = outputs[-1]
model = tf.matmul(outputs, W) + b
cost = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)
# ******
# learning
# *****
sess = tf.Session()
sess.run(tf.global_variables_initializer())
total_batch = int(mnist.train.num_examples/batch_size)
for epoch in range(total_epoch):
    total_cost = 0
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = batch_xs.reshape(batch_size, n_step, n_input)
        _, cost_val = sess.run([optimizer, cost],
                               {X: batch_xs, Y: batch_ys})
        total_cost += cost_val
    print('Epoch: ', '%04d' % (epoch + 1),
          'Avg. cost =',
          '{:.3f}'.format(total_cost / total_batch))
print('최적화 완료')

# ******
# test
# *****
is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
test_batch_size = len(mnist.test.images)
test_xs = mnist.test.images.reshape(test_batch_size, n_step, n_input)
test_ys = mnist.test.labels

print('정확도: ', sess.run(accuracy, {X: test_xs, Y: test_ys}))

















