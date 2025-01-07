import requests
import logging

logging.basicConfig(level=logging.INFO,filename="output.log")

url="https://catfact.ninja/fact"

def get_data():
    response=requests.get(url)
    logging.info(url)
    logging.info(response)
    logging.info(response.status_code)
    logging.info(response.json())
get_data()   