from fastapi import FastAPI
import time

app = FastAPI()

request_limit=100
time_limit = 60


client_id = {}


@app.get("/")
def hello():
    return {"message":"hello"}

@app.post("/check")
def client_id_authenticate(client:str):
    
    
   
    

    if(client not in client_id):
        count = 1
        windowStart = time.time()
        client_id[client]={
              "count":count,
              "window":windowStart
        }
       
      
       

        
        return {"message":"id authenticated and request allowed",
                "current_count":1}
    else:
        currentTime = time.time()

        elasped = currentTime - client_id[client]["window"]

        if(elasped>=time_limit):
                client_id[client]["window"] = time.time()
                client_id[client]["count"] = 1
        elif(client_id[client]["count"]<request_limit):
                 client_id[client]["count"] += 1
        else:
                return{"message":"429 too many requests"}
        
             
        
                
                
                
        
        
                
        return {"message":"request allowed",
                "current_count":client_id[client]["count"]}



    

