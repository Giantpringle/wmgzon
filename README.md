# WMGZON Sports & Leisure Platform

## Introduction
Welcome to the WMGZON Sports & Leisure platform, an innovative e-commerce application designed to provide a seamless shopping experience for sports and leisure products. Built with Flask, this platform offers robust functionalities, including product browsing, search, account management, and transaction processing.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Flask
- SQLAlchemy
- Docker (for Docker setup)
- A modern web browser

## Installation
To set up the WMGZON platform on your local machine, follow these steps:

1. **Clone the Repository:**
git clone https://github.com/Giantpringle/wmgzon.git
cd wmgzon
2. **Set Up a Virtual Environment (recommended):**
python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate
3. **Install Dependencies:**
pip install -r requirements.txt

## Configuration
- Copy the `.env.example` file to `.env` and adjust the settings to match your local environment.

## Running the Application
To run the Flask application:
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
Access the application at `http://127.0.0.1:5000/` in your web browser.

## Docker Setup
To run the application using Docker, follow these steps:

1. **Build the Docker Image:**
docker build -t wmgzon .
This command builds a Docker image named `wmgzon` based on your `Dockerfile`.

2. **Run the Docker Container:**
docker run -p 5000:5000 wmgzon
This command runs the container, making the app accessible at `http://localhost:5000`.

## Using the Application
- Create an account or log in.
- Browse the product catalog.
- Utilize the search and filter functionalities.
- Add products to your cart and proceed to checkout.

## Additional Information
For more details on specific functionalities or contributing to the project, refer to the project's Wiki or documentation.

## Contact Information
For support or feedback, contact us at alfie.brough@warwick.ac.uk.

## License
Specify the license under which this project is released.

Thank you for exploring the WMGZON Sports & Leisure platform!
