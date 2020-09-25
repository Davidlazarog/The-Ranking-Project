import json
import requests
import os 
from dotenv import load_dotenv
load_dotenv()
import re
import base64
import pandas as pd


def get_gh_v3(endpoint, apiKey=os.getenv("TOKEN"), query_params={}): 
    """
    Get data from github using query parameters and passing a custom apikey header
    """
    baseUrl = "https://api.github.com"
    url = f"{baseUrl}{endpoint}"
    headers = {
        "Authorization": f"Bearer {apiKey}"
    }
    res = requests.get(url, params=query_params, headers=headers)
    print(f"Request data to {res.url} status_code:{res.status_code}")
    
    data = res.json()
    return data

def getcoment(x,apiKey=os.getenv("TOKEN")):
    ''' Funcion segunda api que va en la anterior'''
    headers = {
        "Authorization": f"Bearer {apiKey}"
    }
    coment = requests.get(f'https://api.github.com/repos/ironhack-datalabs/datamad0820/issues/{x}/comments',headers=headers)
    coments = coment.json()
    return coments

 
def segundo(comment):
    ''' #Para sacar el segundo usuario con Regex '''
    try:
        return re.findall('@\w*-?\w+',comment[0]['body'])[0].replace('@','')
    except:
        return None
    
def tercero(comment):
    try:
        return re.findall('@\w*-?\w+',comment[0]['body'])[1].replace('@','')
    except:
        return None
    
def grade(comment):
    '''Para sacar con Regex la informacion de notas necesaria'''
    try:
        z= re.findall(r'grade:.*-',comment[0]['body'])
        z = str(z).split(':')
        z = z[1].split("-")
        return z[0]
    except:
        return None

def instructor(comment):
    '''Para sacar el nombre del instructor'''
    try:
        return comment[0]['user']['login']
    except:
        return None
#Para sacar el meme
def meme(comment):
    try:
        try:
            z = re.findall(r'https:.*jpg|.*png|.*jpeg',comment[0]['body'])
            z = str(z).split('(')
            z = z[1].split("'")
            return z[0]
        except: 
            z = re.findall(r'https:.*jpg|.*png|.*jpeg',comment[0]['body'])
            z = str(z).split('(')
            return z[0]
    except:
        return None
    

def lab(data):
    try:
        return re.findall(r'\[(.*?)\]',data)[0]
    except: return None