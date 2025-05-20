from fastapi import FastAPI #Per crear l'API
from json import load #Per carregar el fitxer JSON

app = FastAPI() #Creem una instància de FastAPI

alumnes = [{}] #Initialitzar alumnes com una llista buida

# Carreguem el fitxer JSON al iniciar l'aplicació
with open("alumnes.json", "r") as f:
    alumnes = load(f)

# Definim les rutes de l'API

#Si es "/", es mostra "Institut TIC de Barcelona"
@app.get("/")
def get_root():
    return "Institut TIC de Barcelona"

#Funció per obtenir la cuntitat d'alumnes de la llista d'alumnes
@app.get("/alumnes", response_model=dict)
def get_alumnes():
    return {"result": len(alumnes)}

#Funció per obtenir un alumne de la llista d'alumnes per id
@app.get("/id/{numero}", response_model=dict)
def get_alumne_with_id(numero:int):
    # Por cada alumno...
    for i in alumnes:
        # Si el id del alumno es igual al numero que han pasado como parametro lo devolvemos.
        if i["id"] == numero:
            return i
    # Si no hemos encontrado al alumno, devolvemos un mensaje de error.
    return {"result": "Not found"}

#Funció per esbrinar un alumne de la llista d'alumnes
@app.delete("/del/{numero}", response_model=dict)
def del_alumne(id:int):
    # Per cada alumne...
    for i in range(len(alumnes)):
        # Si el id del alumno es igual al numero que han pasado como parametro lo borramos.
        if alumnes[i]["id"] == id:
            alumnes.pop(i)
            # Devolvemos un error de que se ha borrado el alumno.
            return {"result": "Deleted"}
    # Si no hemos encontrado al alumno, devolvemos un mensaje de error.
    return {"result": "Not found"}

#Funció per afegir un alumne a la llista d'alumnes
@app.post("/alumne", response_model=dict)
def post_alumne(nom:str, cognom:str, dia:str, mes:str, any:str, email:str, feina:str, curs:str):
    # Guardamos los datos del alumno en un diccionario.
    result = {
        # El id del alumno es el id más alto que hemos encontrado + 1.
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
    # Añadimos el alumno a la lista de alumnos.
    alumnes.append(result)
    # Y devolvemos un mensaje de que se ha creado el alumno.
    return {"result": "Created"}

#Funció per obtenir el següent id disponible per afegir un alumne.
def get_higher_id():
    higher = 0
    # Iteramos por cada alumno y si el id del alumno es mayor que el id más alto que hemos encontrado, lo guardamos.
    for i in alumnes:
        if i["id"] > higher:
            higher = i["id"]
    # Devolvemos el id más alto que hemos encontrado.
    return higher
