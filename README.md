# Real Estate REST API
Welcome to the Real-Estate-API, my final project for the IT325 Web Services course this semester! This RESTful API has been developed using Python Flask and is aimed at facilitating the sharing of Tunisian real estate data in a secure manner. Its primary function is to return property details to those who wish to rent or buy a property but are clueless about the Tunisian public real estate system.

## Technologies Used
To develop this API, I utilized a range of technologies, including:

* Python Flask: A lightweight web framework that makes it easy to build web applications in Python.
* SQLite: A popular relational database management system that was used to store the resources.
* JWT token authentication: A security protocol that ensures only authorized users can access the API.
* Insomnia: An API client that was used to test the efficiency of the project.
* VSCode: A popular code editor that was used to write the code for this project.
* Git-Version Control: A version control system that was used to manage the project's source code and track changes over time.

## Installation
1. Clone this repository
2. Install the required packages by running ```pip install -r requirements.txt```
3. Run the app with ```python app.py```
4. The API will be running at http://localhost:5000

## Features
The Real-Estate-API is equipped with a wide range of features, including all CRUD (Create, Read, Update, and Delete) operations. Additionally, it has been secured with JWT token authentication to ensure that only authorized users can access the API.

## Testing
Multiple Insomnia snippets have been provided in the insomnia directory to test the API endpoints. Simply import the desired snippet into Insomnia and execute the requests.

## Security
The API endpoints are secured with JWT token authentication. The authenticate function in user.py checks the user credentials and returns a JWT token upon successful authentication. The identity function in security.py takes the JWT token and returns the user information if the token is valid.

## Docker
This project includes a Dockerfile for easy deployment. To build a Docker image, run the following command:

```
docker build -t store-inventory-api .
```
Then, to run the Docker container:
```
docker run -p 5000:5000 store-inventory-api
```

## Conclusion
In conclusion, the Real-Estate-API is a powerful tool that makes it easy to manage Tunisian real estate data securely. With its wide range of features, including CRUD operations and JWT token authentication, it is an excellent solution for anyone looking to rent or buy property in Tunisia. So, give it a try and see how it can make your life easier!
