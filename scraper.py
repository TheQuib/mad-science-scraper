from bs4 import BeautifulSoup
import requests, yaml

def load_config():
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config

def scrape_madScience(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def save_version(version):
    with open('latestVersion', 'w') as file:
        file.write(version)

def send_webhook(url, version, date, title, body):
    webhook_url = url
    data = {
        "content": f"\n---------\n\nUpdates to mad science have been released.\n\nVersion: {version}\nDate: {date}\nTitle: {title}\n\n{body}\n\n"
    }
    requests.post(webhook_url, json=data)

if __name__ == "__main__":
    load_config()

    webhook_url = load_config()['webhook_url']
    url = load_config()['scrape_url']
    soup = scrape_madScience(url)
    latestUpdate = soup.find_all('div', class_='entry')

    version = latestUpdate[0].find('span', class_='version-badge').text
    date = latestUpdate[0].find('span', class_='entry-date').text
    title = latestUpdate[0].find('div', class_='entry-title').text.replace('LATEST', '').strip()
    body = latestUpdate[0].find('div', class_='change-group').text.strip()


    if version == open('latestVersion', 'r').read():
        print("No new version found.")
    else:       
        print("New version found!")
        print(f"Version: {version}\nDate: {date}\nTitle: {title}")
        send_webhook(webhook_url, version, date, title, body)

    save_version(version)