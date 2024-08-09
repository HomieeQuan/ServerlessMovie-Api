import os
import requests
from io import BytesIO
from azure.storage.blob import BlobServiceClient
from MovieDB import movies
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Azure Storage account info from environment variables
account_name = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
account_key = os.getenv('AZURE_STORAGE_ACCOUNT_KEY')
account_url = os.getenv('AZURE_STORAGE_ACCOUNT_URL')

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient(account_url=account_url, credential=account_key)

# Name of the container
container_name = "images"
# Get a reference to the container
container_client = blob_service_client.get_container_client(container_name)



def upload_cover_image(movie):
    # Generate a filename for the image
    filename = f"{movie['id']}_{movie['title'].replace(' ', '_')}.jpg"
    
    try:
        # Download the image from the URL
        response = requests.get(movie['cover_image_url'])
        response.raise_for_status()
        
        # Create a BytesIO object from the image content
        image_data = BytesIO(response.content)
        
        # Upload the image to blob storage
        blob_client = container_client.upload_blob(name=filename, data=image_data, overwrite=True)
        
        print(f"Uploaded cover image for {movie['title']}")
        return True
    except Exception as e:
        print(f"Error uploading cover image for {movie['title']}: {str(e)}")
        return False

# Upload cover images for all movies
for movie in movies:
    upload_cover_image(movie)

print("Finished uploading cover images.")