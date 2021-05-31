import os
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv

from model import Entity, Contact, get_model_data

load_dotenv()

BASE_URL = 'https://api.ati.su/v1.0/firms/'

headers = {
    'Authorization': os.getenv('AUTH_KEY')
}

app = FastAPI()


@app.get('/firm/{ati_id}')
def get_firm(ati_id):
    """
    Getting brief data company by ati_id
    :param ati_id: id getting by company ATI
    :return: JSON object with data company and data affiliated company
    """
    return get_model_data(Entity, BASE_URL, ati_id, headers)


@app.get('/contacts/{ati_id}')
def get_contacts(ati_id):
    """
     Getting all contacts company by ati_id
    :param ati_id:
    :return: JSON list with contacts company
    """
    return get_model_data(Contact, BASE_URL, ati_id, headers)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port='8000')
