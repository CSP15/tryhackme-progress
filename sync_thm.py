import requests
from bs4 import BeautifulSoup

USERNAME = 'ampsy'
URL = f'https://tryhackme.com/p/{USERNAME}'

def fetch_completed_rooms():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    rooms = soup.find_all('div', class_='room-completed-name')
    return [room.text.strip() for room in rooms]

def save_to_markdown(rooms):
    with open('tryhackme_rooms.md', 'w', encoding='utf-8') as f:
        f.write(f'# TryHackMe Rooms Completed by {USERNAME}\n\n')
        for room in rooms:
            f.write(f'- {room}\n')

if __name__ == '__main__':
    completed_rooms = fetch_completed_rooms()
    save_to_markdown(completed_rooms)
