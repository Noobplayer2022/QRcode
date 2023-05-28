#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[1]:


import pyqrcode

s1 = input("enter your web:")

url = pyqrcode.create(s1)

url.svg("QRcode.svg", scale = 8)




# In[ ]:




