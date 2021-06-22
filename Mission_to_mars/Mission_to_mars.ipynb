{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "import pymongo\n",
    "from splinter import Browser\n",
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import pandas as pd\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 91.0.4472\n",
      "Get LATEST driver version for 91.0.4472\n",
      "Driver [C:\\Users\\kndrs\\.wdm\\drivers\\chromedriver\\win32\\91.0.4472.101\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of page to be scraped\n",
    "url = 'https://redplanetscience.com'\n",
    "browser.visit(url)\n",
    "html=browser.html\n",
    "soup=bs(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Media Get a Close-Up of NASA's Mars 2020 Rover\n",
      "_____________\n",
      "The clean room at NASA's Jet Propulsion Laboratory was open to the media to see NASA's next Mars explorer before it leaves for Florida in preparation for a summertime launch.\n"
     ]
    }
   ],
   "source": [
    "news_title = soup.find('div', class_='content_title').text\n",
    "news_p = soup.find('div', class_='article_teaser_body').text\n",
    "\n",
    "print(news_title)\n",
    "print('_____________')\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Space Images "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "url=\"https://spaceimages-mars.com/\"\n",
    "browser.visit(url)\n",
    "html=browser.html\n",
    "soup=bs(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://spaceimages-mars.com/image/mars/Proctor Crater Dunes 7.jpg\n"
     ]
    }
   ],
   "source": [
    "#find main image\n",
    "image_path = soup.find_all('img')[3][\"src\"]\n",
    "featured_image_url = url + image_path\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Mars Facts "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                         0                1                2\n",
       " 0  Mars - Earth Comparison             Mars            Earth\n",
       " 1                Diameter:         6,779 km        12,742 km\n",
       " 2                    Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 3                   Moons:                2                1\n",
       " 4       Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 5          Length of Year:   687 Earth days      365.24 days\n",
       " 6             Temperature:     -87 to -5 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:          2 ( Phobos & Deimos )\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# URL \n",
    "url = \"https://galaxyfacts-mars.com/\"\n",
    "tables=pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Description</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Mars            Earth\n",
       "Description                                              \n",
       "Mars - Earth Comparison             Mars            Earth\n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km\n",
       "Length of Year:           687 Earth days      365.24 days\n",
       "Temperature:                -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_fact=pd.DataFrame(tables[0])\n",
    "mars_fact.columns = ['Description','Mars','Earth']\n",
    "mars_fact.set_index(\"Description\",inplace=True)\n",
    "mars_fact"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th>Description</th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Mars - Earth Comparison</th>\\n      <td>Mars</td>\\n      <td>Earth</td>\\n    </tr>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg</td>\\n      <td>5.97 × 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n      <td>-88 to 58°C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fact_table=mars_fact.to_html()\n",
    "fact_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<table border=\"1\" class=\"dataframe\">\n",
      "  <thead>\n",
      "    <tr style=\"text-align: right;\">\n",
      "      <th></th>\n",
      "      <th>Mars</th>\n",
      "      <th>Earth</th>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Description</th>\n",
      "      <th></th>\n",
      "      <th></th>\n",
      "    </tr>\n",
      "  </thead>\n",
      "  <tbody>\n",
      "    <tr>\n",
      "      <th>Mars - Earth Comparison</th>\n",
      "      <td>Mars</td>\n",
      "      <td>Earth</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Diameter:</th>\n",
      "      <td>6,779 km</td>\n",
      "      <td>12,742 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Mass:</th>\n",
      "      <td>6.39 × 10^23 kg</td>\n",
      "      <td>5.97 × 10^24 kg</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Moons:</th>\n",
      "      <td>2</td>\n",
      "      <td>1</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Distance from Sun:</th>\n",
      "      <td>227,943,824 km</td>\n",
      "      <td>149,598,262 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Length of Year:</th>\n",
      "      <td>687 Earth days</td>\n",
      "      <td>365.24 days</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Temperature:</th>\n",
      "      <td>-87 to -5 °C</td>\n",
      "      <td>-88 to 58°C</td>\n",
      "    </tr>\n",
      "  </tbody>\n",
      "</table>\n"
     ]
    }
   ],
   "source": [
    "fact_table.replace('\\n','')\n",
    "print(fact_table)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "url=\"https://marshemispheres.com/\"\n",
    "browser.visit(url)\n",
    "html=browser.html\n",
    "soup=bs(html,'html.parser')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# Extract hemispheres item elements\n",
    "mars_hems=soup.find('div',class_='collapsible results')\n",
    "mars_item=mars_hems.find_all('div',class_='item')\n",
    "hemisphere_image_urls=[]\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------------------------------------------------\n",
      "Cerberus Hemisphere Enhanced\n",
      "images/full.jpg\n",
      "--------------------------------------------------\n",
      "Schiaparelli Hemisphere Enhanced\n",
      "images/schiaparelli_enhanced-full.jpg\n",
      "--------------------------------------------------\n",
      "Syrtis Major Hemisphere Enhanced\n",
      "images/syrtis_major_enhanced-full.jpg\n",
      "--------------------------------------------------\n",
      "Valles Marineris Hemisphere Enhanced\n",
      "images/valles_marineris_enhanced-full.jpg\n"
     ]
    }
   ],
   "source": [
    "# Loop through each hemisphere item\n",
    "for item in mars_item:\n",
    "    # Error handling\n",
    "    try:\n",
    "        # Extract title\n",
    "        hem=item.find('div',class_='description')\n",
    "        title=hem.h3.text\n",
    "        # Extract image url\n",
    "        hem_url=hem.a['href']\n",
    "        browser.visit(url+hem_url)\n",
    "        html=browser.html\n",
    "        soup=bs(html,'html.parser')\n",
    "        image_src=soup.find('li').a['href']\n",
    "        if (title and image_src):\n",
    "            # Print results\n",
    "            print('-'*50)\n",
    "            print(title)\n",
    "            print(image_src)\n",
    "        # Create dictionary for title and url\n",
    "        hem_dict={\n",
    "            'title':title,\n",
    "            'image_url':image_src\n",
    "        }\n",
    "        hemisphere_image_urls.append(hem_dict)\n",
    "    except Exception as e:\n",
    "        print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced', 'image_url': 'images/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'image_url': 'images/schiaparelli_enhanced-full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'image_url': 'images/syrtis_major_enhanced-full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'image_url': 'images/valles_marineris_enhanced-full.jpg'}]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "browser.quit()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData]",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
