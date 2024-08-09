import os
from dotenv import load_dotenv
from azure.cosmos import CosmosClient, PartitionKey

# Load environment variables
load_dotenv()

# Get environment variables
URL = os.getenv('COSMOS_URI')
KEY = os.getenv('COSMOS_KEY')
DATABASE_NAME = os.getenv('COSMOS_DATABASE')
CONTAINER_NAME = os.getenv('COSMOS_CONTAINER')

# Print variables for debugging
# print(f"URL: {URL}")
# print(f"KEY: {KEY}")
# print(f"DATABASE_NAME: {DATABASE_NAME}")
# print(f"CONTAINER_NAME: {CONTAINER_NAME}")

# Initialize the Cosmos client
client = CosmosClient(URL, credential=KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

# Example: Query items
query = "SELECT * FROM c"
items = list(container.query_items(query=query, enable_cross_partition_query=True))

for item in items:
    print(item)


def add_movie(movie):
    try:
        container.create_item(body=movie)
        print(f"Added movie: {movie['title']}")
    except Exception as e:
        print(f"Error adding movie {movie['title']}: {str(e)}")
  

movies = [
    {
        "id": "1",
        "title": "Iron Man",
        "year": 2008,
        "director": "Jon Favreau",
        "cover_image": ""
    },
    {
        "id": "2",
        "title": "The Incredible Hulk",
        "year": 2008,
        "director": "Louis Leterrier",
        "cover_image": ""
    },
    {
        "id": "3",
        "title": "Iron Man 2",
        "year": 2010,
        "director": "Jon Favreau",
        "cover_image": ""
    },
    {
        "id": "4",
        "title": "Thor",
        "year": 2011,
        "director": "Kenneth Branagh",
        "cover_image": ""
    },
    {
        "id": "5",
        "title": "Captain America: The First Avenger",
        "year": 2011,
        "director": "Joe Johnston",
        "cover_image": ""
    },
    {
        "id": "6",
        "title": "The Avengers",
        "year": 2012,
        "director": "Joss Whedon",
        "cover_image": ""
    },
    {
        "id": "7",
        "title": "Iron Man 3",
        "year": 2013,
        "director": "Shane Black",
        "cover_image": ""
    },
    {
        "id": "8",
        "title": "Thor: The Dark World",
        "year": 2013,
        "director": "Alan Taylor",
        "cover_image": ""
    },
    {
        "id": "9",
        "title": "Captain America: The Winter Soldier",
        "year": 2014,
        "director": "Anthony Russo, Joe Russo",
        "cover_image": ""
    },
    {
        "id": "10",
        "title": "Guardians of the Galaxy",
        "year": 2014,
        "director": "James Gunn",
        "cover_image": ""
    },
    {
        "id": "11",
        "title": "Avengers: Age of Ultron",
        "year": 2015,
        "director": "Joss Whedon",
        "cover_image": ""
    },
    {
        "id": "12",
        "title": "Ant-Man",
        "year": 2015,
        "director": "Peyton Reed",
        "cover_image": ""
    },
    {
        "id": "13",
        "title": "Captain America: Civil War",
        "year": 2016,
        "director": "Anthony Russo, Joe Russo",
        "cover_image": ""
    },
    {
        "id": "14",
        "title": "Doctor Strange",
        "year": 2016,
        "director": "Scott Derrickson",
        "cover_image": ""
    },
    {
        "id": "15",
        "title": "Guardians of the Galaxy Vol. 2",
        "year": 2017,
        "director": "James Gunn",
        "cover_image": ""
    },
    {
        "id": "16",
        "title": "Spider-Man: Homecoming",
        "year": 2017,
        "director": "Jon Watts",
        "cover_image": ""
    },
    {
        "id": "17",
        "title": "Thor: Ragnarok",
        "year": 2017,
        "director": "Taika Waititi",
        "cover_image": ""
    },
    {
        "id": "18",
        "title": "Black Panther",
        "year": 2018,
        "director": "Ryan Coogler",
        "cover_image": ""
    },
    {
        "id": "19",
        "title": "Avengers: Infinity War",
        "year": 2018,
        "director": "Anthony Russo, Joe Russo",
        "cover_image": ""
    },
    {
        "id": "20",
        "title": "Ant-Man and The Wasp",
        "year": 2018,
        "director": "Peyton Reed",
        "cover_image": ""
    },
    {
        "id": "21",
        "title": "Captain Marvel",
        "year": 2019,
        "director": "Anna Boden, Ryan Fleck",
        "cover_image": ""
    },
    {
        "id": "22",
        "title": "Avengers: Endgame",
        "year": 2019,
        "director": "Anthony Russo, Joe Russo",
        "cover_image": ""
    },
    {
        "id": "23",
        "title": "Spider-Man: Far From Home",
        "year": 2019,
        "director": "Jon Watts",
        "cover_image": ""
    },
    {
        "id": "24",
        "title": "Black Widow",
        "year": 2021,
        "director": "Cate Shortland",
        "cover_image": ""
    },
    {
        "id": "25",
        "title": "Shang-Chi and the Legend of the Ten Rings",
        "year": 2021,
        "director": "Destin Daniel Cretton",
        "cover_image": ""
    },
    {
        "id": "26",
        "title": "Eternals",
        "year": 2021,
        "director": "Chloé Zhao",
        "cover_image": ""
    },
    {
        "id": "27",
        "title": "Spider-Man: No Way Home",
        "year": 2021,
        "director": "Jon Watts",
        "cover_image": ""
    },
    {
        "id": "28",
        "title": "Doctor Strange in the Multiverse of Madness",
        "year": 2022,
        "director": "Sam Raimi",
        "cover_image": ""
    },
    {
        "id": "29",
        "title": "Thor: Love and Thunder",
        "year": 2022,
        "director": "Taika Waititi",
        "cover_image": ""
    }
]

for movie in movies:
    add_movie(movie)

# Query to verify the data was added
query = "SELECT * FROM c"
items = list(container.query_items(query=query, enable_cross_partition_query=True))

print("\nMovies in the database:")
for item in items:
    print(f"{item['title']} ({item['year']})")   