#!/usr/bin/env python
# coding: utf-8

# In[1]:


# project: p4
# submitter-netid: cjohnstone
# partner-netid: none


# In[2]:


num=input("How many tries do you want for each question: ")
num=int(num)
print("\n")


# In[ ]:


def askQuestion(question, answer, hint):
    newnum=num
    print(question)
    while num>0:
        print("\n")
        str1=input("Your answer: ")
        newnum=newnum-1
        str2=str1
        print("\n")
        str2=str2.strip()
        str2=str2.lower()
        if str2 == answer:
            print("Congratulations! You got it right.")
            print("\n")
            return (1)
        elif newnum==1:
            print(hint)
            print("You have this many remaining tries: "+ str(newnum))
        elif newnum==0:
            print("You answered '"+ str1+"'. The correct answer is '"+answer+"'.")
            print("You have this many remaining tries: "+ str(newnum))
            return (0)
        else:
            print("You have this many remaining tries: "+ str(newnum))
            
                

ans1=askQuestion('What is the type of the following? "1.0" + "2.0"\na) int\nb) float\nc) str\nd) bool\ne) NoneType', "c", "Check the textbook")


# In[ ]:


ans2=askQuestion('What is the type of the following? "1" * 2', "str", "notice the quotes!")


# In[ ]:


ans3=askQuestion('What does this expression evaluate to?\nTrue != (3 < 2)', "true", "Calcuate the right side first. Don't forget != means not equal to.")


# In[ ]:


ans=ans1+ans2+ans3
print("You tried 3 questions and got "+str(ans) +" right.")

