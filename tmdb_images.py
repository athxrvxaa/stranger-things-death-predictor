import requests
from pathlib import Path

TMDB_API_KEY = "455971729a43f934cda1237f831321ca"

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"

characters = {
    "Eleven": "Millie Bobby Brown",
    "Max Mayfield": "Sadie Sink",
    "Steve Harrington": "Joe Keery",
    "Dustin Henderson": "Gaten Matarazzo",
    "Jim Hopper": "David Harbour",
    "Mike Wheeler": "Finn Wolfhard",
    "Lucas Sinclair": "Caleb McLaughlin",
    "Will Byers": "Noah Schnapp",
    "Robin Buckley": "Maya Hawke",
    "Nancy Wheeler": "Natalia Dyer",
}

img_dir = Path("images")
img_dir.mkdir(exist_ok=True)

def get_person_id(actor_name):
    url = f"{BASE_URL}/search/person"
    params = {"api_key": TMDB_API_KEY, "query": actor_name}
    r = requests.get(url, params=params)
    r.raise_for_status()
    results = r.json()["results"]
    if not results:
        return None
    return results[0]["id"]

def get_profile_image(person_id):
    url = f"{BASE_URL}/person/{person_id}/images"
    params = {"api_key": TMDB_API_KEY}
    r = requests.get(url, params=params)
    r.raise_for_status()
    profiles = r.json()["profiles"]
    if not profiles:
        return None
    return profiles[0]["file_path"]

for character, actor in characters.items():
    print(f"Downloading {character} ({actor})...")

    person_id = get_person_id(actor)
    if not person_id:
        print(f"❌ Actor not found: {actor}")
        continue

    img_path = get_profile_image(person_id)
    if not img_path:
        print(f"❌ No image for {actor}")
        continue

    img_url = f"{IMAGE_BASE}{img_path}"
    img_data = requests.get(img_url).content

    filename = character.lower().replace(" ", "_") + ".jpg"
    (img_dir / filename).write_bytes(img_data)

    print(f"✅ Saved {filename}")
