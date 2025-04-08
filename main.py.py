from fastapi import FastAPI
from json import loads

app = FastAPI()

alumnes = [{

}]

with open("alumnes.json", "r") as f:
    alumnes = loads(f.read())

@app.get("/")
def get_root():
    return "Institut TIC de Barcelona"

@app.get("/alumnes", response_model=int)
def get_alumnes():
    return len(alumnes)

@app.get("/id/numero", response_class=dict)
def get_alumne_with_id(id:int):
    for i in alumnes:
        if i["id"] == id:
            return i
    return {"result": "Not found"}

@app.delete("/del/numero", response_model=dict)
def del_alumne(id:int):
    for i in range(len(alumnes)):
        if alumnes[i]["id"] == id:
            alumnes.pop(i)
            return {"result": "Deleted"}
    return {"result": "Not found"}

@app.post("/alumne", response_model=dict)
def post_alumne(nom:str, cognom:str, dia:str, mes:str, any:str, email:str, feina:str, curs:str):
    result = {
        "id": get_higher_id()+1,
        "nom": nom,
        "cognom": cognom,
        "data": {
            "dia": dia,
            "mes": mes,
            "any": any
        },
        "email": email,
        "feina": feina,
        "curs": curs
    }
    alumnes.append(result)
    return {"result": "Created"}

def get_higher_id():
    higher = 0
    for i in alumnes:
        if i["id"] > higher:
            higher = i["id"]
    return higher