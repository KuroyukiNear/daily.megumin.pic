import os
import json
import requests

def load_image_data():
    try:
        with open("image_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_image_data(image_data):
    with open("image_data.json", "w") as file:
        json.dump(image_data, file, indent=4)

def get_next_filename(image_data):
    return f"Day_{len(image_data)}.jpg"

def check_exists(img_url, image_data):
    if img_url in image_data:
        print("Image exists.")
    else:
        print("Downloading...")
        # Download the image
        image_response = requests.get(img_url)
        if image_response.status_code == 200:
            filename = get_next_filename(image_data)
            # Save the image in the 'img' directory
            filepath = os.path.join("img", filename)
            with open(filepath, "wb") as image_file:
                image_file.write(image_response.content)
            print(f"Image downloaded successfully as {filename}.")
            # Store the image URL and filename in the image_data dictionary
            image_data[img_url] = filename
            save_image_data(image_data)
        else:
            print(f"Failed to download image. Status code: {image_response.status_code}")

def fetch_img_url():
    api_url = "https://api.waifu.pics/sfw/megumin"
    print("Fetching new JSON data...")
    response = requests.get(api_url)
    json_data = response.json()
    print(json_data)
    img_url = json_data["url"]  # Access the URL using the key "url"
    print(img_url)
    image_data = load_image_data()
    check_exists(img_url, image_data)

if __name__ == "__main__":
    while True:
        fetch_img_url()
