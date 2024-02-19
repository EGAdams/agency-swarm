import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urljoin

class WebNavigationAgent:
    def __init__(self, search_engine_url='https://www.google.com/search'):
        self.search_engine_url = search_engine_url

    def perform_search(self, query):
        """Performs a web search for the query and returns the top result URL in a clickable format."""
        try:
            response = requests.get(f"{self.search_engine_url}?q={query}", headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Find all search result links
                search_results = soup.find_all('a', href=True)
                top_result = None
                for result in search_results:
                    if 'url?q=' in result['href'] and 'webcache' not in result['href']:
                        # Extract and decode the URL
                        raw_url = result['href'].split('url?q=')[1].split('&sa=U')[0]
                        decoded_url = unquote(raw_url)
                        # Ensure the URL is complete
                        top_result = urljoin(self.search_engine_url, decoded_url)
                        break
                return top_result
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None
