from typing import Type, List
from pydantic import BaseModel, parse_obj_as
import requests
from fastapi import status


class AffiliatedEntity(BaseModel):
    firm_name: str
    inn: str


class Entity(BaseModel):
    full_name: str
    firm_type: str
    address: str
    city: str
    score: str
    inn: str
    affiliated_firms: List[AffiliatedEntity]


class Contact(BaseModel):
    name: str
    phone: str
    mobile_phone: str
    icq: str
    fax: str
    skype_name: str
    email: str


def get_model_data(cls: Type[BaseModel], base_url: str, id_item: str, url_headers: dict = None):
    """
        The function return JSON object from api ati.su

    :param cls: All objects inherited from pydantic BaseModel
    :param base_url: url for request
    :param id_item: id
    :param url_headers: http headers
    :return: JSON object or JSON list with response data
    """

    if cls is Entity:
        url = '{}summary/{}/'.format(base_url, id_item)
    elif cls is Contact:
        url = f'{base_url}{id_item}/contacts/summary/'
    else:
        return {'error': 'URL not founded'}

    response = get_response(url, url_headers)
    if response.status_code == status.HTTP_200_OK:
        resp_json = response.json()
        if isinstance(resp_json, list):
            return parse_obj_as(List[cls], resp_json)
        else:
            return parse_obj_as(cls, resp_json)
    return response.json()


def get_response(url, url_headers: dict = None):
    if not url_headers:
        url_headers = {}
    return requests.get(url, headers=url_headers)
