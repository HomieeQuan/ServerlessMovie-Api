Capstone Project: Serverless Movies API
This project is a fully-functional Serverless Movies API that utilizes cloud infrastructure to manage and display movie information. By leveraging serverless functions, a NoSQL database, and cloud storage, the API delivers movie data, including cover images, in a highly efficient and scalable manner.

Project Overview
The Serverless Movies API was designed and implemented to handle movie data requests dynamically, using modern cloud technologies to ensure responsiveness and scalability.

Cloud Infrastructure
To build this API, I first set up the necessary cloud infrastructure using an SDK tailored to my cloud provider of choice. The infrastructure consists of:

NoSQL Database: I configured a cloud-based NoSQL database to store detailed movie information, ensuring fast access and scalability.
Cloud Storage: Movie cover images are stored in cloud storage, with each image associated with a specific movie entry in the database.
Serverless Functions: These functions handle the API's logic, processing requests, and returning data without the need for traditional server management.
Data Preparation
To populate the database, I curated a collection of movie data, which includes essential information such as titles, release years, and genres. This data was then uploaded to the NoSQL database. For each movie, a cover image was stored in cloud storage, with a direct URL linking the image to its corresponding movie record.

Serverless Functions
I developed two primary serverless functions to power the API:

GetMovies: This function retrieves a complete list of movies from the database and returns it as a JSON response. Each movie entry includes a URL for its cover image, allowing clients to access the images directly.

GetMoviesByYear: Designed to cater to specific client requests, this function returns a list of movies released in a specified year. The year is passed as a parameter, and the function queries the database to fetch and return the relevant movies.

Conclusion
The Serverless Movies API is now live, providing an efficient and scalable way to access and display movie information. The use of serverless technology and cloud infrastructure ensures that the API can handle varying loads and deliver data quickly, making it a robust solution for movie data retrieval.
