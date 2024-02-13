#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 

df = pd.read_csv('SP500_data_main.csv')


# In[4]:


print(df.tail(5))


# In[5]:


# practice for a specific path 

#df_xlsx = pd.read_excel('data_csv.csv')


# In[6]:


dfNA = pd.read_csv('SP500_data_main.csv')


# In[7]:


dfNA.head(5)


# In[8]:


dfNA.dropna()


# In[9]:


print(df.columns)


# In[10]:


print(df['Date'])


# In[11]:


print(df['Real_Price'])


# In[12]:


print(df['Consumer_Price_Index'][0:5])


# In[13]:


print(df[['Date','Dividend','SP500', 'Consumer_Price_Index']][0:5])


# In[14]:


print(df[['Date','Dividend','SP500']][0:3])


# In[15]:


df.head(7)


# In[16]:


df.tail(3)


# In[17]:


print(df.iloc[0:2])


# In[ ]:


for index, row in df.iterrows():
    print(index,row)


# In[ ]:


for index, row in df.iterrows():
    print(index,row['Date'])


# In[ ]:


df.loc[df['SP500'] >= 1000]


# In[53]:


df.loc[df['Dividend'] >= 40]


# In[54]:


df.loc[df['PE10'] >= 27]


# In[55]:


#stat numbers and metrics
df.describe()


# In[56]:


# you can add more arguments in sp500 ['Date', 'SP500'], ascending=False
df.sort_values('SP500', ascending=False)


# In[57]:


df['Total'] = df['Dividend'] + df['Real_Dividend']


# In[58]:


df.head(5)


# In[59]:


#you can remove columns 

df = df.drop(columns=['Total'])


# In[60]:


df.head(5)


# In[61]:


df['Total'] = df['Dividend'] + df['Real_Dividend']


# In[33]:


#df = df.[['SP500','Dividend','Earnings']]
#change the columns and you can save it later as another CSV 
# df.to_csv('modified_SP500')
#df.to_excel('mod_SP_500')


# In[62]:


#Collect data for specific years | OR sign  YOU DON'T NEED TO RUN THIS SECTION
new_data = df.loc[(df['Date'] >= '1920-12') & (df['Date'] <= '1935-12')] 

#new_data.to_csv('~/Desktop/filter.csv') YOU CAN RESET NAME.reset_index()


# In[30]:


#df.groupby(['Date']).mean() YOU CAN ADD HEAD OR TAILS 


# In[7]:


#START OF THE GRAPHS WITH THE SECTION MATPLOT


# In[63]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[1]:


plt.title("Data for 1920 to 1935",fontweight='bold')

plt.figure(figsize=(20, 10))


plt.plot(new_data.Date, new_data.Dividend, label='Dividend')
plt.plot(new_data.Date, new_data.Earnings, label='Earnings',color='red', linestyle='dashed')#dotted
#plt.plot(new_data.Date, new_data.SP500, label='SP500')

plt.xticks(new_data.Date[::36])
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()
#plt.savefig('Sample.png') POSSILE NO VIEW

#LARGE AMOUNT OF DATA 


# In[57]:


#VIDEO WAS FOR 22 MIN ONLY FOR TREND LINES


# In[10]:


#Collect data for specific years | OR sign  YOU DON'T NEED TO RUN THIS SECTION
current_data = df.loc[(df['Date'] >= '2000-12') & (df['Date'] <= '2015-12')] 


# In[70]:


plt.title("Data for 2000 to 2015",fontweight='bold')

plt.figure(figsize=(20, 10))


plt.plot(current_data.Date, current_data.Dividend, label='Dividend')
plt.plot(current_data.Date, current_data.loc['Consumer Price Index'], label='Earnings',color='red', linestyle='dashed')#dotted
#plt.plot(new_data.Date, new_data.SP500, label='SP500')

plt.xticks(current_data.Date[::36]) #60 for similar results
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()
#plt.savefig('Sample.png') POSSILE NO VIEW

#LARGE AMOUNT OF DATA 


# In[2]:


plt.title("Data for 1920 to 1935 CPI",fontweight='bold')

plt.figure(figsize=(20, 10))


plt.plot(new_data.Date, new_data.Dividend, label='Dividend')
plt.plot(new_data.Date, new_data.Consumer_Price_Index, label='Consumer Price Index',color='red', linestyle='dashed')#dotted
#plt.plot(new_data.Date, new_data.SP500, label='SP500')

plt.xticks(new_data.Date[::36]) #60 for similar results
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()
#plt.savefig('Sample.png') POSSILE NO VIEW

#LARGE AMOUNT OF DATA 


# In[ ]:




