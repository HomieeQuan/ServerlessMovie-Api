from flask import Flask, jsonify, request
from azure.cosmos import CosmosClient
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

# Set up Cosmos DB client
url = os.getenv('COSMOS_URI')
key = os.getenv('COSMOS_KEY')
client = CosmosClient(url, credential=key)
database_name = os.getenv('COSMOS_DATABASE')
container_name = os.getenv('COSMOS_CONTAINER')

database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Movie API. Use /movies for all movies or /movies/<year> for movies by year."

@app.route('/movies', methods=['GET'])
def get_movies():
    query = "SELECT * FROM c"
    movies = list(container.query_items(query=query, enable_cross_partition_query=True))
    
    # Ensure each movie has a cover_image URL
    for movie in movies:
        if 'cover_image' not in movie:
            movie['cover_image'] = "No cover image available"
    
    return jsonify(movies)

@app.route('/movies/<int:year>', methods=['GET'])
def get_movies_by_year(year):
    query = f"SELECT * FROM c WHERE c.year = {year}"
    movies = list(container.query_items(query=query, enable_cross_partition_query=True))
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True)
