
from src.app import app
from src.database import db
from flask import request
from bson.json_util import dumps
from datetime import datetime
import numpy as np

@app.route("/lab/create/<name>")
def create_lab(name):
    new_lab = {
    'Lab': name}
    result = db.student.insert_one(new_lab)
    return {'_id': str(result.inserted_id)}


@app.route("/lab/randomeme/<lab>")
def random_meme(lab):
    result=db.student.aggregate([  
        { "$match":  {"Lab": lab} },
        { "$sample": {"size": 1} }, 
        { "$project" : { "Meme" : 1, "_id": 0}}
      ])
    return dumps(result)

@app.route("/lab/search/<name>")
def searchLab(name):
    opened_pr = db.student.find({"$and":[{"Lab":name},{"State": "open"}]}).count()
    closed_pr = db.student.find({"$and":[{"Lab":name},{"State": "closed"}]}).count()
    grade_time = db.student.find({"Lab":name},{'Creado':1,'Cerrada':1})
    grade_time_list=[]
    for i in grade_time:
        op = datetime.fromisoformat(i['Creado'].replace('Z',''))
        cl = datetime.fromisoformat(i['Cerrada'].replace('Z',''))
        grade_time_list.append((cl-op).total_seconds())

    result={'-El numero de PR abiertas es': opened_pr,
    '-El numero de PR cerradas es': closed_pr,
    '-El porcentaje de PR cerradas con las abiertas es de ': f'{int(closed_pr/(closed_pr+opened_pr)*100)}%',
    f'-El tiempo maximo de correccion en horas de el {name}': (f'{str(round(max(grade_time_list)/3600,2))}h'),
    f'-El tiempo minimo de correccion en horas de el {name}': (f'{str(round(min(grade_time_list)/3600,2))}h'),
    f'-El tiempo medio de correccion en horas de el {name}': (f'{str(round(np.mean(grade_time_list)/3600,2))}h')
    }
    return dumps(result)

def getapi():
    res = requests.get(f"http://localhost:5050/student/all")
    data = res.json() 
    return list(data)

#mongodb+srv://1234:1234@therankingproject.yrlud.mongodb.net/rankingproject
#docker run -p 5050:5050 --env DBURL="mongodb+srv://1234:1234@therankingproject.yrlud.mongodb.net/RankingProyect?retryWrites=true&w=majority" --env PORT=5050 rankingproject
