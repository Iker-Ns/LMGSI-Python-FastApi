### Imports ################################################## 
import os   #per neteja la pantalla
from json import load #per carregar el fitxer json

#Variables ###################################################

#Nom del fitxer on desar/carregar dades
nom_fitxer = "alumnes.json" 

### menu() ###################################################
#   Aquesta funció mostra el menú d'opcions per pantalla. 
#   
#   Retorna (str): l'opció escollida per l'usuari
##############################################################
def menu():
    #Netejem la pantalla
    os.system('cls')            
    
    #Mostrem les diferents opcions
    print("Gestió alumnes")
    print("-------------------------------")
    print("1. Mostrar alumnes")
    print("2. Afegir alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")
    
    print("\n5. Desar a fitxer")
    print("6. Llegir fitxer")

    print("\n0. Sortir\n\n\n")
    print(">", end=" ")

    #i retornem l'opció escollida per l'usuari
    return input()



### Programa ################################################

alumnes = []

#Funcio per mostrar tots el alumnes
def mostra_alumnes():
    if len(alumnes) == 0:
        print("No hi ha alumnes, es probable que no hagis llegit el fitxer primer")
        return

    for alumne in alumnes:
        mostra_alumne(alumne["id"])
    
#Funcio per mostrar un alumne#
def mostra_alumne(id:int):
    if len(alumnes) == 0:
        print("No hi ha alumnes, es probable que no hagis llegit el fitxer primer")
        return

    for alumne in alumnes:
        if alumne["id"] == id:
            break # Si trobem l'alumne, sortim del bucle
        
    ## Si no hem trobat l'alumne, mostrem un missatge d'error
    if alumne["id"] != id:
        print("Alumne no trobat")
        return
    
    print(f"""
Id: {alumne["id"]}
Nom: {alumne["nom"]},
Cognom: {alumne["cognom"]},
Email: {alumne["email"]},
Curs: {alumne["curs"]},
Data: {alumne["data"]["dia"]}/{alumne["data"]["mes"]}/{alumne["data"]["any"]},
Feina: {"Si" if alumne["feina"] else "No"}""")

#Funcio per afegir un alumne
def add_alumne(nom, cognom, email, curs, dia, mes, any, feina):
    alumnes.append({
        "id": get_next_id(),
        "nom": nom,
        "cognom": cognom,
        "email": email,
        "curs": curs,
        "data": {
            "dia": dia,
            "mes": mes,
            "any": any
        },
        "feina": feina
    })
    print("Alumne afegit")

#Funcio per esborrar un alumne
def delete_alumne(id:int):
    if len(alumnes) == 0:
        print("No hi ha alumnes, es probable que no hagis llegit el fitxer primer")
        return

    #Comprovem si l'alumne existeix
    for alumne in alumnes:
        if alumne["id"] == id:
            alumnes.remove(alumne)
            print("Alumne esborrat")
            return
    print("Alumne no trobat")

#Funcio per obtenir el següent id disponible per afegir un alumne.
def get_next_id():
    if len(alumnes) == 0:
        return 1
    higher = 1
    for alumne in alumnes:
        if alumne["id"] > higher:
            higher = alumne["id"]
    return higher + 1

#Fins a l'infinit (i més enllà)
while True:
    
    #Executem una opció funció del que hagi escollit l'usuari
    match menu():

        # Mostrar alumnes ##################################
        case "1":
            os.system('cls')
            print("Mostrar alumnes")
            print("-------------------------------")
            

            #Introduiu el vostre codi per mostrar alumnes aquí
            mostra_alumnes()

            input()
    
        # Afegir alumne ##################################
        case "2":
            os.system('cls')
            print("Afegir alumne")
            print("-------------------------------")
            
            #Introduiu el vostre codi per afegir un alumne aquí
            add_alumne(
                nom=input("Nom: "),
                cognom=input("Cognom: "),
                email=input("Email: "),
                curs=input("Curs: "),
                dia=input("Dia: "),
                mes=input("Mes: "),
                any=input("Any: "),
                feina=input("Feina (Si/No): ").lower() == "si"
            )
                
            input()
    
        # Veure alumne ##################################
        case "3":
            os.system('cls')
            print("Veure alumne")
            print("-------------------------------")
            
            #Introduiu el vostre codi per veure un alumne aquí

            # Demanem l'id de l'alumne a l'usuari
            # Comprovem que l'id sigui un número enter
            id = input("Id de l'alumne: ")
            try:
                id = int(id)
            except:
                # Si no és un número enter, mostrem un missatge d'error
                # i tornem a demanar l'id
                print("Id incorrecte")
                input()
                continue
            mostra_alumne(id)

            input()

        # Esborrar alumne ##################################
        case "4":
            os.system('cls')
            print("Esborrar alumne")
            print("-------------------------------")
          
            #Introduiu el vostre codi per esborrar un alumne aquí

            # Demanem l'id de l'alumne a l'usuari
            # Comprovem que l'id sigui un número enter
            id = input("Id de l'alumne: ")
            try:
                id = int(id)
            except:
                # Si no és un número enter, mostrem un missatge d'error
                # i tornem a demanar l'id
                print("Id incorrecte")
                input()
                continue
            delete_alumne(id)

            input()

        # Desar a fitxer ##################################
        case "5":
            os.system('cls')
            print("Desar a fitxer")
            print("-------------------------------")

            #Introduiu el vostre codi per desar a fitxer aquí

            # Guardem el fitxer
            with open(nom_fitxer, "w") as f:
                f.write(alumnes)
            
            input()

        # Llegir fitxer ##################################
        case "6":    
            os.system('cls')
            print("Llegir fitxer")
            print("-------------------------------")

            #Introduiu el vostre codi per llegir de fitxer aquí

            # Demanem el nom del fitxer a l'usuari
            # Si no s'introdueix cap nom, es fa servir el fitxer per defecte (alumnes.json)
            with open(nom_fitxer, "r") as f:
                alumnes = load(f)
            print("Alumnes carregats")

            input()

      

        # Sortir ##################################
        case "0":
            os.system('cls')
            print("Adeu!")

            #Trenquem el bucle infinit
            break

        #Qualsevol altra cosa #####################   
        case _:
            print("\nOpció incorrecta\a")            
            input()
