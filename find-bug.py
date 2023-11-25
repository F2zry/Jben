import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_broken_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a')
            
            broken_links = []
            
            for link in links:
                href = link.get('href')
                if href:
                    full_url = urljoin(url, href)
                    link_response = requests.head(full_url)
                    if link_response.status_code >= 400:
                        broken_links.append((full_url, link_response.status_code))
            
            return broken_links
        
        else:
            print(f"Gagal lu anj {url}. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Akses Eror anj {url}: {e}")

# Example usage:
website_url = input ('Masukin Target Anj : ')
broken_links = find_broken_links(website_url)

if broken_links:
    print("Bug ditemukan:")
    for link, status_code in broken_links:
        print(f"URL: {link} - Status Code: {status_code}")
else:
    print("Ga ada Bug di Website nya TOLOL")