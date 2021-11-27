#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

from config.settings import BASE_DIR
# In[6]:


def make_df():
    
    df = pd.read_csv(os.path.join(BASE_DIR, 'static', 'today_number9_6.csv'))
    
    data_list = ['강원', '경기','광주']

    a = data_list[0]
    b = data_list[1]
    c = data_list[2]

    aa = df[df['지역명']==a]
    bb = df[df['지역명']==b]
    cc = df[df['지역명']==c]

    total = aa.append(bb, ignore_index = True)
    total = total.append(cc,ignore_index=True)
    
    return total


# In[9]:


def make_bar_plot(df_name):
    sns.factorplot(x = '지역명', y= '확진자수', data= df_name, kind='bar')
    plt.savefig(os.path.join(BASE_DIR, 'static', 'aa1.png'))




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




