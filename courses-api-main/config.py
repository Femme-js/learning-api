# import variables from .env

import os

class Config:
    ID = os.environ.get('ID')
