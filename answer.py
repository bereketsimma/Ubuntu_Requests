import os
import requests
from urllib.parse import urlparse
import sys

def fetch_image():
    url = input("Enter the image URL: ").strip()
    
    if not url:
        print("No URL provided. Exiting.")
        return
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the image: {e}")
        return
    
    os.makedirs("Fetched_Images", exist_ok=True)
    
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    if not filename:
        filename = "image_from_web.jpg"
    
    filepath = os.path.join("Fetched_Images", filename)
    
    try:
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"Image successfully saved to {filepath}")
    except Exception as e:
        print(f"Error saving the image: {e}")

if __name__ == "__main__":
    fetch_image()
