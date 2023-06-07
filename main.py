from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
 return {"message": "Hello World"}


@app.get("/category/{category}")
async def engeins_par_categorie(category:str): 
    engeins=[]
     
    return engeins


@app.get("/owner/{owner}")
async def engeins_par_proprio(owner:str): 
    engeins=[]
     
    return engeins

@app.get("/bills/{owner}")
async def engeins_par_proprio(owner:str): 
    facture="il s'agit de la facture de :"+owner
     
    return {"message":facture}


