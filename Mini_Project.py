#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd 

df = pd.read_csv('data_csv.csv')


# In[43]:


print(df.tail(5))


# In[57]:


#stat numbers and metrics
df.describe()


# In[45]:


#Collect data for specific years | OR sign  YOU DON'T NEED TO RUN THIS SECTION
new_data = df.loc[(df['Date'] >= '1920-12') & (df['Date'] <= '1935-12')] 


# In[46]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[47]:


plt.title("Dividend Data for 1920 to 1935",fontweight='bold')

plt.figure(figsize=(20, 10))


plt.plot(new_data.Date, new_data.Dividend, label='Dividend')
plt.plot(new_data.Date, new_data.Earnings, label='Earnings',color='red', linestyle='dashed') #dotted


plt.xticks(new_data.Date[::36])
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()



# In[48]:


plt.title("CPI Data for 1920 to 1935",fontweight='bold')

plt.figure(figsize=(20, 10))


plt.plot(new_data.Date, new_data['Consumer Price Index'], label='CPI')



plt.xticks(new_data.Date[::36]) #60 for similar results
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()



# In[49]:


#Collect data for specific years | OR sign  YOU DON'T NEED TO RUN THIS SECTION
current_data = df.loc[(df['Date'] >= '2000-12') & (df['Date'] <= '2015-12')] 


# In[50]:


plt.title("Dividend Data for 2000 to 2015",fontweight='bold')

plt.figure(figsize=(20, 10))


plt.plot(current_data.Date, current_data.Dividend, label='Dividend')
plt.plot(current_data.Date, current_data.Earnings, label='Earnings',color='red', linestyle='dashed')#dotted


plt.xticks(current_data.Date[::36]) #60 for similar results
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()



# In[51]:


plt.title("CPI Data for 2000 to 2015",fontweight='bold')

plt.figure(figsize=(20, 10))


plt.plot(current_data.Date, current_data['Real Earnings'], label='Real Earnings')
plt.plot(current_data.Date, current_data['Consumer Price Index'], label='CPI',color='red', linestyle='dashed')#dotted


plt.xticks(current_data.Date[::36]) #60 for similar results
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()



# In[60]:


plt.title("S&P 500 Data for 2000 to 2015",fontweight='bold')

plt.figure(figsize=(20, 10))



plt.plot(current_data.Date, current_data['SP500'], label='SP500',color='red', linestyle='dashed')#dotted
#plt.plot(current_data.Date, current_data['Consumer Price Index'], label='CPI')


plt.xticks(current_data.Date[::36]) #60 for similar results
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()



# In[53]:


plt.title("CPI Data for 2000 to 2015",fontweight='bold')

plt.figure(figsize=(20, 10))


plt.plot(current_data.Date, current_data['Consumer Price Index'], label='CPI')


plt.xticks(current_data.Date[::36]) #60 for similar results
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()



# In[54]:


plt.title("CPI Data for 1920 to 1935",fontweight='bold')

plt.figure(figsize=(20, 10))


plt.plot(new_data.Date, new_data['Consumer Price Index'], label='CPI')


plt.xticks(new_data.Date[::36]) #60 for similar results
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()



# In[58]:


plt.title("S&P 500 Data for 1920 to 1935",fontweight='bold')

plt.figure(figsize=(20, 10))



plt.plot(new_data.Date, new_data['SP500'], label='SP500',color='red', linestyle='dashed')#dotted
plt.plot(new_data.Date, new_data['Consumer Price Index'], label='CPI')


plt.xticks(new_data.Date[::36]) #60 for similar results
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()



# # END OF THE CODE 

# In[ ]:




