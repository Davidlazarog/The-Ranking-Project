from src.app import app
from src.database import db
from flask import request
#from ..helpers.json_response import asJsonResponse
from bson.json_util import dumps

#Crea un nuevo usuario
@app.route("/student/create/<name>")
def create_student(name):
    new_student = {
        "User": name}
    result = db.student.insert_one(new_student)
    return {"_id": str(result.inserted_id)}
 
#Te busca la informacion del usuario que escribas
@app.route("/student/search/<name>")
def list_students(name):
    query = {'User':name}
    result = db.student.find(query)
    return dumps(result)

#Te dice que labs ha hecho cada usuario que le metas
@app.route("/student/labs/<name>")
def list_students_lab(name):
    query = {'User':name}
    project = {'Lab':1}
    result = db.student.find(query, project)
    return dumps(result)
    
#Te enseña todos los estudiantes 
@app.route("/student/all")
def all_students():
    result = db.student.distinct('User')
    return dumps(result)

@app.route("/student/grades/<name>")
def grades_student(name):
    query = {'User':name}
    project = {'Nota':1}
    result = list(db.student.find(query, project)).count()
    return f'La nota media de {name} es de {result}'


'''    
{User:'gontzalm'}
'''