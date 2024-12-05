import requests
from bs4 import BeautifulSoup
import re

def get_links():
    # Step 1: Fetch the webpage content
    url_root = 'https://wol.jw.org/';
    #https://wol.jw.org/am/wol/d/r93/lp-am/101993001

    url_awakes = url_root + 'am/wol/lv/r93/lp-am/0/8015'    

    response = requests.get(url_awakes)

    # Check if the request was successful
    if response.status_code == 200:
        # Step 2: Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Step 3: Extract specific data
        # Example: Extracting all the headings (h1 tags)
        #headings = soup.find_all('h1')  # Find all <h1> tags
        #headings = soup.find_all('ul')  # Find all <h1> tags

        # Print each heading
        #for heading in headings:
        #    print(heading.text)

        # Example: Extracting links (anchor tags)
        links = soup.find_all('a')  # Find all <a> tags

        # Print each link's href attribute
        for link in links:
            href = link.get('href')
            if '/lp-am/0/' in href:
                article_url = url_root + href
                article_response = requests.get(article_url)

                # Check if the request was successful
                if article_response.status_code == 200:
                    article_soup = BeautifulSoup(response.text, 'html.parser')
                    article_links = article_soup.find_all('a')  # Find all <a> tags
                    for article_link in article_links:
                        article_href = article_link.get('href')
                        if '/lp-am/0/' in article_href:
                            print(article_href)
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

def scrape_amharic_text():
    url = 'https://wol.jw.org/am/wol/d/r93/lp-am/101993001'
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Step 2: Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        #exclude_classes = ['noticeText', 'noticeText noMarkerNotice']  # List of classes to exclude
        #p_tags = soup.find_all('p', class_=lambda x: x and not any(cls in exclude_classes for cls in x))        
        p_tags = soup.find_all('p')

        # Step 4: Loop through all the <p> tags and print the text content
        for tag in p_tags:
            #print(tag.get_text())
            tag_text = tag.get_text()
            sentences = split_into_sentences(tag_text)

            for sentence in sentences:
                print('sentence',sentence) 

def split_into_sentences(paragraph):
    delimiter = "\u1362"
    sentences = paragraph.split(delimiter)
        #"([!?።])")
    #sentences = re.split(delimiter, paragraph)
    return sentences

          
            
def main():
    database = r"C:\myapps\grafana-helper\src\data\blackbody.db"

    # create a database connection
    #get_links()
    scrape_amharic_text()

if __name__ == '__main__':
    main()       