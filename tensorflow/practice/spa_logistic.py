import tensorflow as tf
import numpy as np
from sklearn.preprocessing import scale

xy = np.loadtxt('binary.csv',  delimiter=',', dtype='float32')
x_data = xy[:,0:-1]
y_data = xy[:,[-1]]

#x_data = scale(x_data)
x_data[:,1] = (x_data[:,1] - x_data[:,1].mean())/x_data[:,1].std()
print(x_data)
print(y_data) 

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_uniform([4, 1], -1.0, 1.0))

h = tf.matmul(X, W)
hypothesis = tf.div(1., 1. + tf.exp(-h))
#hypothesis = tf.sigmoid(h)
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))


a = tf.Variable(0.1)  # learning rate, alpha
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)  # goal is minimize cost

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(2001):
    sess.run(train, feed_dict={X: x_data, Y: y_data})
    if step % 20 == 0:
        print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run(W))

print('-----------------------------------------')
print(sess.run(hypothesis, feed_dict={X: [[1,-1.8002628,3.61,3.]]}) > 0.5)

correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, {X: x_data, Y: y_data}))


