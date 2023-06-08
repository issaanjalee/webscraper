import requests
from bs4 import BeautifulSoup
import csv
url = input('eg:https://example.com \n Enter url:')
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all('a')
csv_file = 'links.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Link'])
    for link in links:
        writer.writerow([link['href']])
print(f"Links saved to {csv_file} successfully.")
