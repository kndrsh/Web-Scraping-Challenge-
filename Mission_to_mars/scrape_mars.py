
from splinter import browser
from bs4 import BeautifulSoup 
import pandas as pd
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver 
    executable_path = {'executable_path': 'chromedriver'}
    return browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    #### URL of page to be scraped - MARS NEWS ####
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
   
    # Create BeautifulSoup object and parse
    soup = BeautifulSoup(html, 'html.parser')
    
    # Collect the latest News Title and Paragraph Text and assign text to variables
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    #### URL of page to be scraped - JPL IMAGES ####
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Find image url for the current Featured Mars Image; assign the url string to a variable
    full_img = soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url = url + full_img

    #### URL of page with tables to be read - MARS FACTS ####
    url = "https://galaxyfacts-mars.com/"
    # Scrape any tabular data from page
    tables = pd.read_html(url)
    
    # Convert the data to a HTML table string
    mars_df = pd.DataFrame(tables[0])
    mars_df.columns = ['Description', 'Mars', 'Earth']
    mars_df.set_index('Description', inplace=True)
    # Generate html table
    mars_table = mars_df.to_html()
    # Clean up table - strip newlines
    mars_table.replace('\n','')

    #### URL of page to be scraped - MARS HEMISPHERES ####
    url = "https://marshemispheres.com/"
    browser.visit(url)
    html = browser.html
    time.sleep(1)
    # Create BeautifulSoup object and parse
    soup = BeautifulSoup(html, 'html.parser')

    # Obtain high resolution images for each of Mar's hemispheres
    # Extract hemispheres item elements
    mars_hems=soup.find('div',class_='collapsible results')
    mars_item=mars_hems.find_all('div',class_='item')
    hemisphere_image_urls=[]
    
    
    for item in mars_item:
    # Error handling
        try:
        # Extract title
            hem=item.find('div',class_='description')
            title=hem.h3.text
        # Extract image url
            hem_url=hem.a['href']
            browser.visit(url+hem_url)
            html=browser.html
            soup=BeautifulSoup(html,'html.parser')
            image_src=soup.find('li').a['href']
            if (title and image_src):
            # Print results
                print('-'*50)
                print(title)
                print(image_src)
        # Create dictionary for title and url
            hem_dict={
            'title':title,
            'image_url':image_src
        }
            hemisphere_image_urls.append(hem_dict)
        except Exception as e:
            print(e)

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_table": mars_table,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    browser.quit()

    # Return results
    return mars_data