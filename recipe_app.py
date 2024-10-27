# Import necessary packages
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database credentials
username = 'your_username'  
password = 'your_password' 
hostname = 'localhost'      
database_name = 'recipe'  

# Create an engine object
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{hostname}/{database_name}')

# Create a Session class
Session = sessionmaker(bind=engine)

# Initialize the session object
session = Session()

# Now you can use the session object to interact with the database
