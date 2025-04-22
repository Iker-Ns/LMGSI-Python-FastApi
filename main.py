from fastapi import FastAPI #Per crear l'API
from json import loads #Per carregar el fitxer JSON

app = FastAPI() #Creem una instància de FastAPI

alumnes = [{}] #Initialitzar alumnes com una llista buida

# Carreguem el fitxer JSON al iniciar l'aplicació
with open("alumnes.json", "r") as f:
    alumnes = loads(f.read())

# Definim les rutes de l'API

#Si es "/", es mostra "Institut TIC de Barcelona"
@app.get("/")
def get_root():
    return "Institut TIC de Barcelona"

#Funció per obtenir la cuntitat d'alumnes de la llista d'alumnes
@app.get("/alumnes", response_model=int)
def get_alumnes():
    return {"result": len(alumnes)}

#Funció per obtenir un alumne de la llista d'alumnes per id
@app.get("/id/numero", response_class=dict)
def get_alumne_with_id(id:int):
    for i in alumnes:
        if i["id"] == id:
            return i
    return {"result": "Not found"}

#Funció per esbrinar un alumne de la llista d'alumnes
@app.delete("/del/numero", response_model=dict)
def del_alumne(id:int):
    for i in range(len(alumnes)):
        if alumnes[i]["id"] == id:
            alumnes.pop(i)
            return {"result": "Deleted"}
    return {"result": "Not found"}

#Funció per afegir un alumne a la llista d'alumnes
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

#Funció per obtenir el següent id disponible per afegir un alumne.
def get_higher_id():
    higher = 0
    for i in alumnes:
        if i["id"] > higher:
            higher = i["id"]
    return higher
