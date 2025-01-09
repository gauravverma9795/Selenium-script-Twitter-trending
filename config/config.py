from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

class Config:
    TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
    TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
    PROXYMESH_USERNAME = os.getenv("PROXYMESH_USERNAME")
    PROXYMESH_PASSWORD = os.getenv("PROXYMESH_PASSWORD")
    MONGO_URI = os.getenv("MONGO_URI")
