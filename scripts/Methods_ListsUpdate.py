## Method 1: map()

# In[1]:


# Create a list of casualties from battles
battleDeaths = [482, 93, 392, 920, 813, 199, 374, 237, 244]


# In[2]:


# Create a function that updates all battle deaths by adding 100
def updated(x): return x + 100


# In[3]:


# Create a list that applies updated() to all elements of battleDeaths
list(map(updated, battleDeaths))


# ## Method 2: for x in y

# In[4]:


# Create a list of deaths
casualties = [482, 93, 392, 920, 813, 199, 374, 237, 244]


# In[5]:


# Create a variable where we will put the updated casualty numbers
casualtiesUpdated = []


# In[6]:


# Create a function that for each item in casualties, adds 10
for x in casualties:
    casualtiesUpdated.append(x + 100)


# In[7]:


# View casualties variables
casualtiesUpdated


# ## Method 3: lambda functions

# In[8]:


# Map the lambda function x() over casualties
list(map((lambda x: x + 100), casualties))

