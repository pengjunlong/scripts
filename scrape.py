import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()

def save_text(text, filename):
    with open(filename, 'w') as file:
        file.write(text)

def generate_url():
    today = datetime.today()
    return f"https://v2rayshare.githubrowcontent.com/{today.year}/{today.month:02d}/{today.strftime('%Y%m%d')}.txt"

if __name__ == "__main__":
    url = generate_url()
    text = fetch_text(url)
    save_text(text, "v2rayshare.txt")
