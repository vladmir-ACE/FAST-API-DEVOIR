from pydantic import BaseModel
from datetime import date

class Categorie(BaseModel):
    id:int 
    intituler:str
    description:str

class Proprietaire(BaseModel):
    id:int 
    nom:str
    prenom:str
    telephone:str
    email:str


class Engein(BaseModel):
    id:int 
    imatriculation:str
    cotation:int
    majoration:int

class Facture(BaseModel):
    id:int 
    montant_Total:int
    date:date

class Tranche(BaseModel):
    id:int 
    libeller:str
    montant:int
    date:date


    
    