import tensorflow as tf
import numpy as np

xy = np.loadtxt('iris_training.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

print(x_data.shape, y_data.shape)

nb_classes = 3   

X = tf.placeholder(tf.float32, [None, 4])
Y = tf.placeholder(tf.int32, [None, 1])   
Y_one_hot = tf.one_hot(Y, nb_classes)

print("one_hot", Y_one_hot)
Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes])
print("reshape", Y_one_hot)

W = tf.Variable(tf.random_normal([4, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# softmax = exp(logits) / reduce_sum(exp(logits), dim)
logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)

cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits,
                                                 labels=Y_one_hot)
cost = tf.reduce_mean(cost_i)
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Launch graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(2000):
        sess.run(train, feed_dict={X: x_data, Y: y_data})
        if step % 100 == 0:
            loss = sess.run(cost, feed_dict={X: x_data, Y: y_data})
            print("Step: {:5}\tCost: {:.3f}".format(step, loss))

    print(sess.run(accuracy,feed_dict={X: x_data, Y: y_data}))
    
#     print("\n=====  prediction =====")   
#     pred = sess.run(tf.argmax(hypothesis,1), feed_dict={X: x_data})
#     # y_data: (N,1) = flatten => (N, ) matches pred.shape
#     for p, y in zip(pred, y_data.flatten()):
#         print("[{}] Prediction: {} True Y: {}".format(p == int(y), p, int(y)))

 
