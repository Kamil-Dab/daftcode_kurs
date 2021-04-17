from fastapi import FastAPI, Request, Response

from pydantic import BaseModel

from typing import Dict

app = FastAPI()

app.id_patient = 0

app.patients = dict()

#Zad1

@app.get('/')
def hello_world():
	return {"message": "Hello World during the coronavirus pandemic!"}

#Zad2 / 1.2

@app.api_route('/method', methods = ['GET','POST','PUT','DELETE','OPTIONS'])
def name_method(request: Request):
	return{"method": request.method}


#@app.get('/method')
#def mathod_name_get():
#	return {"method": "GET"}

#@app.post('/method')
#def mathod_name_post():
#	return {"method": "POST"}

#@app.put('/method')
#def mathod_name_put():
#	return {"method": "PUT"}

#@app.delete('/method')
#def mathod_name_delete():
#	return {"method": "DELETE"}

#Zad3 /1.4

class NamePatientRq(BaseModel):
    name: str
    surename: str


class NamePatientResp(BaseModel):
    id: int
    patient: Dict


@app.post('/patient', response_model=NamePatientResp)
def name_patient(request: NamePatientRq):
	app.id_patient += 1
	app.patients[app.id_patient] = request.dict()
	return NamePatientResp(id = app.id_patient, patient=request.dict())

#Zad4 / 1.5

@app.get('/patient/{number_pat}')
def number_patients(number_pat: int):
	if number_pat in app.patients:
		return app.patients[number_pat]
	else:
		return Response(status_code=204)
