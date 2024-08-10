import os
import requests
from io import BytesIO
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions 
from MovieDB import movies, container as db_container
from dotenv import load_dotenv


load_dotenv()

account_name = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
account_key = os.getenv('AZURE_STORAGE_ACCOUNT_KEY')
account_url = os.getenv('AZURE_STORAGE_ACCOUNT_URL')

blob_service_client = BlobServiceClient(account_url=account_url, credential=account_key)
container_client = blob_service_client.get_container_client("images")

def upload_cover_image(movie):
    filename = f"{movie['id']}_{movie['title'].replace(' ', '_')}.jpg"
    response = requests.get(movie['cover_image_url'])
    blob_client = container_client.get_blob_client(filename)
    blob_client.upload_blob(data=BytesIO(response.content), overwrite=True)
    movie['cover_image'] = blob_client.url
    db_container.upsert_item(movie)
    print(f"Uploaded cover image for {movie['title']} and updated database")

def upload_all_cover_images():
    print("Starting to upload cover images...")
    for movie in movies:
        upload_cover_image(movie)
    print(f"\nUpload complete. Total movies processed: {len(movies)}")

if __name__ == "__main__":
    upload_all_cover_images()