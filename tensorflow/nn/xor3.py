import tensorflow as tf
import numpy as np
tf.set_random_seed(777)   

xy = np.loadtxt('07train.txt')

x_data =  xy[:,0:-1]
y_data = xy[:,[-1]]
print(x_data.shape)
print(y_data.shape)

X = tf.placeholder(tf.float32, [None, 2])
Y = tf.placeholder(tf.float32, [None, 1])

W1 = tf.Variable(tf.random_normal([2, 5]))
W2 = tf.Variable(tf.random_normal([5, 4]))
W3 = tf.Variable(tf.random_normal([4, 1]))
b1 = tf.Variable(tf.random_normal([5]))
b2 = tf.Variable(tf.random_normal([4]))
b3 = tf.Variable(tf.random_normal([1]))

L1 = tf.sigmoid(tf.matmul(X,W1)+b1)
L2 = tf.sigmoid(tf.matmul(L1,W2)+b2)
hypothesis = tf.sigmoid(tf.matmul(L2, W3) + b3)

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) *
                       tf.log(1 - hypothesis))

train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(5000):
        sess.run(train, feed_dict={X: x_data, Y: y_data})
        if step % 100 == 0:
            print(step, sess.run(cost, feed_dict={
                  X: x_data, Y: y_data}), sess.run(W1), sess.run(W2))

    # Accuracy report
    h, c, a = sess.run([hypothesis, predicted, accuracy],
                       feed_dict={X: x_data, Y: y_data})
    print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)

'''
Hypothesis:  [[ 0.5]
 [ 0.5]
 [ 0.5]
 [ 0.5]]
Correct:  [[ 0.]
 [ 0.]
 [ 0.]
 [ 0.]]
Accuracy:  0.5
'''
