from pymongo.mongo_client import MongoClient
import urllib.parse

username = "ap5032890"
password = urllib.parse.quote_plus("Abhijit@1892")  # Replace with your actual password

uri = f"mongodb+srv://{username}:{password}@cluster0.dhkncma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
