import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

tf.set_random_seed(777) 

xy = np.loadtxt('03train.txt', dtype='float32')
x_data = xy[:,0:-1]
y_data = xy[:,[-1]]

# x_data = [1.,2.,3.]
# y_data = [1.,2.,3.]

w=tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b=tf.Variable(tf.random_uniform([1], -1.0, 1.0))

hypothesis = w * x_data + b

cost = tf.reduce_mean(tf.square(hypothesis - y_data))

a = tf.Variable(0.1)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

W_vals = []
cost_vals = []
B_vals = []

for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        curr_W = sess.run(w)
        curr_cost = sess.run(cost)
        curr_B = sess.run(b)
#         print(step, curr_cost, curr_W, curr_B)
        W_vals.append(curr_W)
        cost_vals.append(curr_cost)
        B_vals.append(curr_B)

# Show the cost function
# plt.plot(W_vals, cost_vals,'ro')
# plt.show()


fig = plt.figure()
ax = fig.gca(projection='3d')
   
# Make data.
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
X = W_vals
Y = B_vals
#X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
Z = np.array([cost_vals])
print(Z) 
# print(X)
# print(Y)
# print(Z)
   
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False, alpha=0.5)

# Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
   
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
   
plt.show()

