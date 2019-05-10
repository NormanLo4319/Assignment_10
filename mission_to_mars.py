# Import Beautiful Soup
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import datetime as dt


# In[55]:


# Set the executable path and initialize the chorme browser
executable_path = {'executable_path':'./chromedriver.exe'}
browser = Browser('chrome', **executable_path)


# In[56]:


# Visit the mars NASA new site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[60]:


html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')

# print(news_soup)

# Slide element includes everything in the <ul class = "item_list">
slide_element = news_soup.select_one('ul.item_list li.slide')

print(slide_element)


# In[61]:


slide_element.find("div", class_="content_title")


# In[63]:


# Use the parent element to find the first a tag and save it as new_title
news_title = slide_element.find('div', class_='content_title').get_text()
news_title


# In[65]:


news_paragraph = slide_element.find('div', class_='article_teaser_body').get_text()
news_paragraph


# In[68]:


# For Mars Images
# Visit URL
executable_path = {'executable_path': './chromedriver.exe'}
browser = Browser('chrome', **executable_path)
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[74]:


# Asking splinter to go to the site hit a button with class name full_image
# <button class="full_image">Full Image</button>
full_image_button = browser.find_by_id('full_image')
full_image_button.click()


# In[75]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_element = browser.find_link_by_partial_text('more info')
more_info_element.click()


# In[76]:


# Parse the results html with beautiful soup
html = browser.html
image_soup = BeautifulSoup(html, 'html.parser')


# In[77]:


img_url = image_soup.select_one('figure.lede a img').get('src')
img_url


# In[78]:


# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url}'
img_url


# In[89]:


# For Mars Weather
executable_path = {'executable_path':'./chromedriver.exe'}
browser = Browser('chrome', **executable_path)
url='https://twitter.com/marswxreport?lang=en'
browser.visit(url)


# In[80]:


html = browser.html
weather_soup = BeautifulSoup(html, 'html.parser')


# In[81]:


# Frist find a tweet with the data name "Mars Weather"
mars_weather_tweet = weather_soup.find('div',
                                      attrs= {
                                          'class':'tweet',
                                          'data-name':'Mars Weather'
                                      })


# In[82]:


# Next search within the tweet for p tag containing the tweet text
mars_weather = mars_weather_tweet.find('p', 'tweet-text').get_text()
mars_weather


# In[90]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[91]:


hemisphere_image_urls = []

# First get a list og all the hemisphers
links = browser.find_by_css('a.product-item h3')
for item in range(len(links)):
    hemisphere = {}
    
# Need to find the element on each loop to avoid a stale element exception
    browser.find_by_css('a.product-item h3')[item].click()
    
# Find the sample image anchor tag and extract the href
    sample_element = browser.find_link_by_text('Sample').first
    hemisphere['img_url'] = sample_element['href']
    
# Get hemisher title
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
# Append hemispher object to list
    hemisphere_image_urls.append(hemisphere)

# Navigate backwards in the web page
    browser.back()


# In[92]:


hemisphere_image_urls


# In[93]:


# Mars Facts
df = pd.read_html('https://space-facts.com/mars/')[0]
# print(df)
df.columns=['description', 'value']
df.set_index('description', inplace=True)
print(df)


# In[ ]:





# In[ ]:





# In[ ]:




