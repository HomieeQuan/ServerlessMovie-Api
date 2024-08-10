import os
from dotenv import load_dotenv
from azure.cosmos import CosmosClient, PartitionKey


load_dotenv()

URL = os.getenv('COSMOS_URI')
KEY = os.getenv('COSMOS_KEY')
DATABASE_NAME = os.getenv('COSMOS_DATABASE')
CONTAINER_NAME = os.getenv('COSMOS_CONTAINER')


# Initialize the Cosmos client
client = CosmosClient(URL, credential=KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)


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
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/0/02/Iron_Man_%282008_film%29_poster.jpg"
    },
    {
        "id": "2",
        "title": "The Incredible Hulk",
        "year": 2008,
        "director": "Louis Leterrier",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg"
    },
    {
        "id": "3",
        "title": "Iron Man 2",
        "year": 2010,
        "director": "Jon Favreau",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg"
    },
    {
        "id": "4",
        "title": "Thor",
        "year": 2011,
        "director": "Kenneth Branagh",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg"
    },
    {
        "id": "5",
        "title": "Captain America: The First Avenger",
        "year": 2011,
        "director": "Joe Johnston",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg"
    },
    {
        "id": "6",
        "title": "The Avengers",
        "year": 2012,
        "director": "Joss Whedon",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/8/8a/The_Avengers_%282012_film%29_poster.jpg"
    },
    {
        "id": "7",
        "title": "Iron Man 3",
        "year": 2013,
        "director": "Shane Black",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/1/19/Iron_Man_3_poster.jpg"
    },
    {
        "id": "8",
        "title": "Thor: The Dark World",
        "year": 2013,
        "director": "Alan Taylor",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/7/7f/Thor_The_Dark_World_poster.jpg"
    },
    {
        "id": "9",
        "title": "Captain America: The Winter Soldier",
        "year": 2014,
        "director": "Anthony Russo, Joe Russo",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg"
    },
    {
        "id": "10",
        "title": "Guardians of the Galaxy",
        "year": 2014,
        "director": "James Gunn",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg"
    },
    {
        "id": "11",
        "title": "Avengers: Age of Ultron",
        "year": 2015,
        "director": "Joss Whedon",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/f/ff/Avengers_Age_of_Ultron_poster.jpg"
    },
    {
        "id": "12",
        "title": "Ant-Man",
        "year": 2015,
        "director": "Peyton Reed",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg"
    },
    {
        "id": "13",
        "title": "Captain America: Civil War",
        "year": 2016,
        "director": "Anthony Russo, Joe Russo",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg"
    },
    {
        "id": "14",
        "title": "Doctor Strange",
        "year": 2016,
        "director": "Scott Derrickson",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg"
    },
    {
        "id": "15",
        "title": "Guardians of the Galaxy Vol. 2",
        "year": 2017,
        "director": "James Gunn",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/a/ab/Guardians_of_the_Galaxy_Vol_2_poster.jpg"
    },
    {
        "id": "16",
        "title": "Spider-Man: Homecoming",
        "year": 2017,
        "director": "Jon Watts",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg"
    },
    {
        "id": "17",
        "title": "Thor: Ragnarok",
        "year": 2017,
        "director": "Taika Waititi",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg"
    },
    {
        "id": "18",
        "title": "Black Panther",
        "year": 2018,
        "director": "Ryan Coogler",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg"
    },
    {
        "id": "19",
        "title": "Avengers: Infinity War",
        "year": 2018,
        "director": "Anthony Russo, Joe Russo",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg"
    },
    {
        "id": "20",
        "title": "Ant-Man and The Wasp",
        "year": 2018,
        "director": "Peyton Reed",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/2/2c/Ant-Man_and_the_Wasp_poster.jpg"
    },
    {
        "id": "21",
        "title": "Captain Marvel",
        "year": 2019,
        "director": "Anna Boden, Ryan Fleck",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/8/85/Captain_Marvel_poster.jpg"
    },
    {
        "id": "22",
        "title": "Avengers: Endgame",
        "year": 2019,
        "director": "Anthony Russo, Joe Russo",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg"
    },
    {
        "id": "23",
        "title": "Spider-Man: Far From Home",
        "year": 2019,
        "director": "Jon Watts",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/b/bd/Spider-Man_Far_From_Home_poster.jpg"
    },
    {
        "id": "24",
        "title": "Black Widow",
        "year": 2021,
        "director": "Cate Shortland",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/e/e9/Black_Widow_%282021_film%29_poster.jpg"
    },
    {
        "id": "25",
        "title": "Shang-Chi and the Legend of the Ten Rings",
        "year": 2021,
        "director": "Destin Daniel Cretton",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/7/74/Shang-Chi_and_the_Legend_of_the_Ten_Rings_poster.jpeg"
    },
    {
        "id": "26",
        "title": "Eternals",
        "year": 2021,
        "director": "Chloé Zhao",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/9/9b/Eternals_%28film%29_poster.jpeg"
    },
    {
        "id": "27",
        "title": "Spider-Man: No Way Home",
        "year": 2021,
        "director": "Jon Watts",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/0/00/Spider-Man_No_Way_Home_poster.jpg"
    },
    {
        "id": "28",
        "title": "Doctor Strange in the Multiverse of Madness",
        "year": 2022,
        "director": "Sam Raimi",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/1/17/Doctor_Strange_in_the_Multiverse_of_Madness_poster.jpg"
    },
    {
        "id": "29",
        "title": "Thor: Love and Thunder",
        "year": 2022,
        "director": "Taika Waititi",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/8/88/Thor_Love_and_Thunder_poster.jpeg"
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