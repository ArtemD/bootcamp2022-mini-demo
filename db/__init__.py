import sqlalchemy
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv

# Load .env file
load_dotenv(find_dotenv())

import os

engine = sqlalchemy.create_engine(os.environ.get('DATABASE'))
Session = sessionmaker(bind=engine)