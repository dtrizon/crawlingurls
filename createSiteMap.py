import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Function to crawl a URL
def crawl_url(url, visited_urls):
    try:
        # Send an HTTP GET request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Process the page here, e.g., print page title
            page_title = soup.title.string
            print(f"Title: {page_title} - {url}")

            # Add this URL to the list of visited URLs
            visited_urls.add(url)
            # Find and follow links on the page
            for link in soup.find_all('a', href=True):
                
                # Construct the absolute URL from the relative link
                next_url = urljoin(url, link['href'])
                # Check if the URL belongs to the same domain
                if urlparse(next_url).netloc == urlparse(url).netloc:
                    # Check if we haven't visited this URL before
                    if next_url not in visited_urls:
                        # Recursively crawl the next URL
                        crawl_url(next_url, visited_urls)
        else:
            print(f"Failed to retrieve URL: {url}")
    except Exception as e:
        print(f"An error occurred while crawling URL {url}: {str(e)}")

# Starting URL to crawl
start_url = "https://.com"

# Set to keep track of visited URLs
visited_urls = set()

# Start crawling
crawl_url(start_url, visited_urls)
print(visited_urls)
print(len(visited_urls))

f = open("urlText.txt", "a")
for item in visited_urls:
  f.write(item + "\n")
