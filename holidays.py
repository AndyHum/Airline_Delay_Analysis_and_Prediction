
# coding: utf-8

# In[1]:

import pandas as pd
df = pd.read_csv('BosData3.csv')
df


# In[2]:

df['date']=pd.to_datetime((df.Year*10000+df.Month*100+df.DayOfMonth).apply(str),format='%Y%m%d')


# In[3]:

df


# In[4]:

holidays = ['2004-1-1','2008-1-1','2007-1-1','2006-1-1','2005-1-1','2004-12-31',
            '2005-12-31','2006-12-31','2007-12-31','2008-12-31','2008-5-26',
            '2007-5-28','2006-5-29','2005-5-30','2004-5-31','2004-7-4','2005-7-4',
            '2006-7-4','2007-7-4','2008-7-4','2008-11-27','2007-11-22','2006-11-23'
            ,'2005-11-24','2004-11-25','2004-12-25','2005-12-25','2006-12-25',
            '2007-12-25','2008-12-25','2004-12-24','2005-12-24','2006-12-24','2007-12-24'
           ,'2008-12-24','2008-9-1','2007-9-3','2006-9-4','2005-9-5','2004-9-6',
           '2008-3-23','2007-4-8','2006-4-16','2005-3-27','2004-4-11']


# In[5]:

holidays


# In[7]:

from datetime import date
holidaylist =[]
for x in holidays:
    a = date(int(x.split('-')[0]),int(x.split('-')[1]),int(x.split('-')[2]))
    holidaylist.append(a)
holidaylist


# In[11]:

from datetime import date
timelen = []
for x in df['date']:
    i = 10000
    for y in holidaylist:
        if abs((x.date() - y).days) < i:
            i = abs((x.date() - y).days)
    timelen.append(i)
len(timelen)


# In[12]:

df['DaysToHoliday'] = timelen


# In[14]:

df


# In[19]:

df.to_csv('BosData6.csv')


# In[18]:

del df['Unnamed: 0']


# In[ ]:



