#!/usr/bin/env python
# coding: utf-8

# In[35]:


def letter_count() :
    text = input("Please enter your sentences : ")
    new_dict = {}
    for i in text :
        new_dict.update({i : text.count(i) })
    print(new_dict)
letter_count()

