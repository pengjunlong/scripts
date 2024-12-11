import requests
import base64
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    try:
        text = base64.b64decode(text).decode('utf-8')
    except Exception:
        print("base64 decode failed")
    if not text.endswith('\n'):
        text += '\n'
    return text

def save_text(text, filename):
    with open(filename, 'w') as file:
        file.write(text)

def generate_v2rayshare_url():
    today = datetime.today()
    return f"https://v2rayshare.githubrowcontent.com/{today.year}/{today.month:02d}/{today.strftime('%Y%m%d')}.txt"


def v2rayshare():
    url = generate_v2rayshare_url()
    text = fetch_text(url)
    return text


def aiboboxx():
    url = "https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2"
    text = fetch_text(url)
    return text


def ermaozi():
    url = "https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/v2ray.txt"
    text = fetch_text(url)
    return text


if __name__ == "__main__":
    text = ""
    text += v2rayshare()
    text += aiboboxx()
    text += ermaozi()
    text = text.rstrip('\n')
    text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    save_text(text, "v2ray.txt")




