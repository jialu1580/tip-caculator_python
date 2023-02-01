#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('welcome to tip calculator')
total_bill = float(input('what was the total bill?\n'))
people = float(input('how many people to split the bill?\n'))
tip = float(input('what percentage tip would you like to give? 10,15,20?'))
money = total_bill / people + total_bill / people * 0.01 * tip
new_money = round(money, 2)
print(f"each person should pay:${new_money}")


# In[ ]:





# In[ ]:




