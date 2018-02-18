import matplotlib.pyplot as plt 

x = [1,2,3]
y = [1,2,3]

plt.plot(x, y, linewidth=4.0)
plt.show()

line,=plt.plot(x, y, '-')
line.set_antialiased(False)
plt.show()

x1 = [1,2,3,4]
y1 = [8,2,3,10]
x2 = [2,7,8,9]
y2 = [6,10,3,1]
lines = plt.plot(x1, y1, x2, y2)
# use keyword args
plt.setp(lines, color='r', linewidth=2.0)
# or MATLAB style string value pairs
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
plt.show()
