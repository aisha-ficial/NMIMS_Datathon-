import requests
from bs4 import BeautifulSoup

# Function to scrape data from a website
def scrape_website_data(url):
    headers = {
        'User-Agent': 'Your User Agent'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Customize this part based on the structure of the website
        skincare_data = []
        for article in soup.find_all('article'):
            title = article.find('h2').text.strip()
            # Add additional attributes as needed
            url = article.find('a')['href']
            skincare_data.append({'title': title, 'url': url})
        return skincare_data
    else:
        print(f"Failed to fetch data from {url}")
        return []

# Main function
def main():
    websites = [
        {'name': 'wiki skin', 'url': 'https://en.wikipedia.org/wiki/Skin_care'},
        {'name': 'wiki skin natural', 'url': 'https://en.wikipedia.org/wiki/Natural_skin_care'}
        # Add more websites as needed
    ]
    
    for website in websites:
        print(f"Scraping data from {website['name']}...")
        skincare_data = scrape_website_data(website['url'])
        for data in skincare_data:
            print(f"Title: {data['title']}")
            print(f"URL: {data['url']}")
            print()

if __name__ == "__main__":
    main()
