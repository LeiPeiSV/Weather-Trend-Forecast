#!/usr/bin/env python
# coding: utf-8

# # Explore Weather Trends

# In this project, we will be exploring the weather trend in San Jose and compare it to the global trend. We used NumPy, Pandas, and Matplotlib to implement the analysis and visualization. 

# ## Data Analysis

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


# import the san jose weather data
san_jose = pd.read_csv('/Users/Lei/Downloads/San_Jose_Data.csv')
san_jose.head()


# In[8]:


# import the global weather data
global_data = pd.read_csv('/Users/Lei/Downloads/Global_Data.csv')
global_data.head()


# **Calculate Moving Average Temperature**
# 
# Used _.rolling().mean()_ to calculate the moving average. The plot is drawn using matplotlibs. The x/y axis, graph title, legends, and the units are also included in the graph.

# **Identify the Optimal Window Size**
# 
# Used for loop to subplot 6 graphs with window size ranging from 3 to 8 (inclusive). The results shows that the larger the window size, the smoother lines achieved. Thus we selected 8 as the final result image.

# In[33]:


plt.figure(figsize=(20, 10))

for i, moving_size in enumerate([3,4,5,6,7,8]):
    plt.subplot(2, 3, i+1)
    plt.plot(global_data['year'], global_data['avg_temp'].rolling(moving_size).mean())
    plt.plot(san_jose['year'], san_jose['avg_temp'].rolling(moving_size).mean())
    plt.grid()
    plt.title(str(moving_size))


# In[11]:


moving_size = 8

plt.figure(figsize=(10, 8))
plt.plot(global_data['year'], global_data['avg_temp'].rolling(moving_size).mean())
plt.plot(san_jose['year'], san_jose['avg_temp'].rolling(moving_size).mean())

plt.grid()
plt.xlabel('Year')
plt.ylabel('Moving Average Temperature(°C)')
plt.title('8-years moving average temperature comparison, Global Vs San Jose')
plt.legend(['Global Temperature(°C)', 'San Jose Temperature(°C)']);


# ## Observation

# - San Jose is much hotter than the global average temperature. The temperature of San Jose is ranging between 14°C to 15°C in the time period of 1850 till 2020. Whereas the global is much warmer, ranging from 8°C to 10°C during the same period of time.
# 
# 
# - The global temperature shows a clear trend that before 1850, the average difference seems to be 2 °C consistently between 7°C to 9°C. After 1850, it increased slightly (1 °C). From that time till now, the global temperature shows a clear increasing from 8°C to 10°C.
# 
# 
# - Due to the lack of data, we can’t view the temperature at San Jose before 1850. It seems that the temperature in San Jose is ranging from 14°C to 14.5°C in the period of 1850 to 1930. However, it slightly increased by 0.5°C as shown along the orange line.
# 
# 
# - After 1950, there is a clear trend in San Jose that the temperature is increasing faster by 1°C. That trend aligns with the development of Silicon Valley starting from 1950 when the big companies began to boom, and people are relocating for more job opportunities in the San Jose Area. It is clear that the average temperature has passed 15°C recently since 2000.
# 
# 
# - The global trend shows global warming starting from the late 1800s, which could result from increasing human activities and carbon emission after the first industrial revolution. The average temperature has increased nearly 2°C and it’s getting faster after 1970s, where the slope is much steeper.
# 
# 
# - In general, we can safely state that global warming is TRUE. And according to the data we analyzed, it is primarily related to human activity as well as industrial sector development. Both trends further confirmed that statement.
