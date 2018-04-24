
# coding: utf-8

# # seaborn

# In[39]:


import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

import seaborn as sns

x = np.linspace(0, 14, 100)
y1 = np.sin(x)
y2 = 2*np.sin(x+0.5)
y3 = 3*np.sin(x+1.0)
y4 = 4*np.sin(x+1.5)

plt.figure(figsize=(10,6))
plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.show()


# In[40]:


sns.set_style("white")

plt.figure(figsize=(10,6))
plt.plot(x,y1, x,y2, x,y3, x,y4)

sns.despine()

plt.show()


# In[41]:


sns.set_style("dark")

plt.figure(figsize=(10,6))
plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.show()


# In[42]:


sns.set_style("whitegrid")

plt.figure(figsize=(10,6))
plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.show()


# In[43]:


plt.figure(figsize=(10,6))
plt.plot(x,y1, x,y2, x,y3, x,y4)

sns.despine(offset=10)

plt.show()


# In[44]:


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style("whitegrid")
get_ipython().magic('matplotlib inline')


# In[45]:


tips = sns.load_dataset("tips")
tips.head(5)


# In[46]:


sns.set_style("whitegrid")

plt.figure(figsize=(8,6))
sns.boxplot(x=tips["total_bill"])
plt.show()


# In[47]:


plt.figure(figsize=(8,6))
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()


# In[48]:


plt.figure(figsize=(8,6))
sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, palette="Set3")
plt.show()


# In[49]:


plt.figure(figsize=(8,6))
sns.swarmplot(x="day", y="total_bill", data=tips, color=".5")
plt.show()


# In[50]:


plt.figure(figsize=(8,6))
sns.boxplot(x="day", y="total_bill", data=tips)
sns.swarmplot(x="day", y="total_bill", data=tips, color=".25")
plt.show()


# In[51]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')

tips = sns.load_dataset("tips")
tips.head(5)


# In[52]:


sns.set_style("darkgrid")
sns.lmplot(x="total_bill", y="tip", data=tips, size=7)
plt.show()


# In[53]:


sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips, size=7)
plt.show()


# In[54]:


sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips, palette="Set1", size=7)
plt.show()


# In[55]:


uniform_data = np.random.rand(10, 12)
uniform_data


# In[56]:


sns.heatmap(uniform_data)
plt.show()


# In[57]:


sns.heatmap(uniform_data, vmin=0, vmax=1)
plt.show()


# In[58]:


flights = sns.load_dataset("flights")
flights.head(5)


# In[59]:


flights = flights.pivot("month", "year", "passengers")
flights.head(5)


# In[60]:


plt.figure(figsize=(10,8))
sns.heatmap(flights)
plt.show()


# In[61]:


plt.figure(figsize=(10,8))
sns.heatmap(flights, annot=True, fmt="d")
plt.show()


# In[62]:


sns.set(style="ticks")
iris = sns.load_dataset("iris")
iris.head(10)


# In[63]:


sns.pairplot(iris)
plt.show()


# In[64]:


sns.pairplot(iris, hue="species")
plt.show()


# In[65]:


sns.pairplot(iris, vars=["sepal_width", "sepal_length"])
plt.show()


# In[66]:


sns.pairplot(iris, x_vars=["sepal_width", "sepal_length"], 
             y_vars=["petal_width", "petal_length"])
plt.show()


# In[67]:


anscombe = sns.load_dataset("anscombe")
anscombe.head(5)


# In[68]:


sns.set_style("darkgrid")

sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),  ci=None, size=7)
plt.show()


# In[69]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
           ci=None, scatter_kws={"s": 80}, size=7)
plt.show()


# In[70]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           order=1, ci=None, scatter_kws={"s": 80}, size=7)
plt.show()


# In[71]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           order=2, ci=None, scatter_kws={"s": 80}, size=7)
plt.show()


# In[72]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           ci=None, scatter_kws={"s": 80}, size=7)
plt.show()


# In[73]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           robust=True, ci=None, scatter_kws={"s": 80}, size=7)
plt.show()

