import json
import requests
import os 
from dotenv import load_dotenv
load_dotenv()
import re
import base64
import pandas as pd
import src.operaciones as op

#Con esta funcion vemos cual es la ultima pull request en ese momento.
x = op.get_gh_v3('/repos/ironhack-datalabs/datamad0820/pulls',query_params=({"per_page":100}))
z = x[0]['number']

#Iteramos por todas las PullRequest hechas hasta el momento. 
data = [op.getpull(i) for i in range(1,541)]

#Creamos el Json y lo guardamos en Output. 
jsonfile = json.dumps(data)
jsonfile = pd.DataFrame(data)
jsonfile.to_json('output/jsonfile.json',orient="records")

#Con este archivo, luego hay que meterlo en MongoDBCompass con el siguiente comando en la terminal desde la carpeta output. 
#<"mongoimport -d RankingProyect -c student --jsonArray jsonfile.json">