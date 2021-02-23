#!/usr/bin/env python
# coding: utf-8

# In[25]:


import re
import cv2 as cv
import os
import numpy as np


# In[50]:


array_of_red_train = []
array_of_green_train = []
array_of_blue_train = []
array_of_transparency_train = []
def read_train_data(path):
    for filename in os.listdir(r"./"+path):
        if filename [-3:]=='tif':
            image = cv.imread (path + "/" + filename, cv.IMREAD_UNCHANGED)
            b, g, r, alpha = cv.split(image)
            array_of_red_train.append(r)
            array_of_blue_train.append(b)
            array_of_green_train.append(g)
            array_of_transparency_train.append(alpha)
read_train_data ('train_data')

array_of_red_test = []
array_of_green_test = []
array_of_blue_test = []
array_of_transparency_test = []
def read_test_data(path):
    for filename in os.listdir(r"./"+path):
        if filename [-3:]=='tif':
            image = cv.imread (path + "/" + filename, cv.IMREAD_UNCHANGED)
            b, g, r, alpha = cv.split(image)
            array_of_red_test.append(r)
            array_of_blue_test.append(b)
            array_of_green_test.append(g)
            array_of_transparency_test.append(alpha)
read_test_data ('test_data')




# In[43]:


def info(dataset):
    mean = [np.mean(item) for item in dataset]  #逐图片平均
    mean_total = np.mean(mean)
    std_total = np.std(mean)
    return mean_total, std_total



# In[42]:


'''
后期可匹配val600和train3000
train_list = []
train_file = open("train3000.txt", "r")
for line in train_file.readlines():                          
    tem = line.strip()
    a, b = re.split ('[ ]',tem)
    train_list.append (a)
    train_list.append (b)
array_of_green_train = []
for filename in train_list:
    image = cv.imread ('train_data' + "/" + filename)
    b, g, r = cv.split(image)
    array_of_green_train.append(g)

val_list = []
val_file = open("val600.txt", "r")
for line in val_file.readlines():                          
    tem = line.strip()
    a, b = re.split ('[ ]',tem)
    val_list.append (a)
    val_list.append (b)
array_of_green_val = []
for filename in val_list:
    image = cv.imread ('train_data' + "/" + filename)
    b, g, r = cv.split(image)
    array_of_green_val.append(g)
'''


# In[61]:





# In[46]:


print('training set: \n  mean and std of red channel are {} ,\n of blue channle are {} ,\n of green channel are {}, \n of transparency channel are {}'.format(info(array_of_red_train),info(array_of_blue_train),info(array_of_green_train),info(array_of_transparency_train)))


# In[51]:


print('test set: n\  mean and std of red channel are {} ,\n of blue channle are {} ,\n of green channel are {}, \n of transparency channel are {}'.format(info(array_of_red_test),info(array_of_blue_test),info(array_of_green_test),info(array_of_transparency_test)))


# In[20]:





# In[81]:





# In[82]:





# In[84]:





# In[38]:





# In[31]:





# In[40]:





# In[ ]:




