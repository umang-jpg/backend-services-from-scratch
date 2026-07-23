from fastapi import FastAPI

app = FastAPI()


client_id = ["abcd1234","efgh5678"]


@app.get("/")
def hello():
    return {"message":"hello"}

@app.post("/check")
def client_id_authenticate(client:str):
    if(client not in client_id):
        client_id.append(client)
        return {"message":"id authenticated"}
    else:
        return {"message":"your id exist already"}
