#!/usr/bin/env python
# coding: utf-8

# ### f(x) = x^3 - 6x^2 + 4x + 12
# 
# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# ##### Определяем корни:

# In[2]:


np.roots([1, -6, 4, 12])


# ##### Строим график:

# In[3]:


z = list(range(-10, 10))
fz = [x ** 3 - 6 * x ** 2 + 4 * x + 12 for x in z]


# In[4]:


plt.axes(fc = 'lightyellow')
plt.plot(z, fz)
plt.show()


# ##### Вычисляем вершину:

# In[5]:


y = [1, -6, 4, 12]
np.polyder(y)


# In[6]:


np.roots(np.polyder([1, -6, 4, 12]))


# In[7]:


minimum = np.roots(np.polyder([1, -6, 4, 12]))[0]
maximum = np.roots(np.polyder([1, -6, 4, 12]))[1]
minimum, maximum


# In[8]:


y_min = np.polyval([1, -6, 4, 12], minimum)
y_min


# In[9]:


y_max = np.polyval([1, -6, 4, 12], maximum)
y_max


# In[10]:


print(f'Точка максимума: {maximum, y_max}')
print(f'Точка минимума: {minimum, y_min}')


# ##### Находим интервалы, на которых функция возрастает и убывает:

# In[11]:


print(f'Функция возрастает на: [-∞; {maximum, y_max}] & [{minimum, y_min}; +∞]')
print(f'Функция убывает на: [{maximum, y_max}; {minimum, y_min}]')


# ##### Определяем промежутки, на которых f > 0 и f < 0:

# In[12]:


root1, root2, root3 = np.roots([1, -6, 4, 12])


# In[13]:


print(f'f > 0: [-∞; {round(root3, 2)}] & [{round(root2, 2)}; {round(root1, 2)}]')
print(f'f < 0: [{round(root3, 2)}; {round(root2, 2)}] & [{round(root1, 2)}; +∞]')

