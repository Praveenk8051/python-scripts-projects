# ### Import the modules

# Import required modules
import requests
from bs4 import BeautifulSoup


# ### Scrap the html and turn into a beautiful soup object

# Create a variable with the url
url = 'http://chrisralbon.com'

# Use requests to get the contents
r = requests.get(url)

# Get the text of the contents
html_content = r.text

# Convert the html content into a beautiful soup object
soup = BeautifulSoup(html_content, 'lxml')


# ### Select the website's title

# View the title tag of the soup object
print(soup.title)


# ### Website title tag's string

# View the string within the title tag
print(soup.title.string)


# ### First paragraph tag

# view the paragraph tag of the soup
print(soup.p)


# ### The parent of the title tag
print(soup.title.parent.name)


print(soup.find_all('a')[0:5])


# ### The string inside the first paragraph tag
print(soup.p.string)

print(soup.find_all('h2')[0:5])
print(soup.find_all('a')[0:5])

