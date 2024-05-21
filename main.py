from fastapi.staticfiles import StaticFiles
from typing import Annotated
from fastapi import FastAPI, Form, File, UploadFile
from mail import send_mail
from database import create_db, add_lead, get_all_leads

app = FastAPI()

create_db()

@app.post("/login")
async def login(firstname: Annotated[str, Form()], 
                lastname: Annotated[str, Form()], 
                email: Annotated[str, Form()], 
                cv: UploadFile):
    
    add_lead(firstname, lastname, email, "PENDING")
    get_all_leads()
    
    #Write file to read as attachment when sending mail
    write_file('resume', await cv.read())

    send_mail('Alma', [email], 'Thanks for your interest!', 'Hi, thanks for signing up.', ['resume'])
    send_mail('Alma', ['emadalma40@gmail.com'], 'New lead' + str(email), 'There is a new lead', ['resume'])

    return {
            "firstname": firstname, 
            "lastname": lastname,
            "email": email
            
            }

@app.get("/leads")
async def leads():
    leads = get_all_leads()
    map = {}
    for i in leads:
        map[i[0]] = {"first_name", i[1], 
                     "last_name", i[2], 
                     "email", i[3]}
        
        
        
    return {
        "leads": map
    }

app.mount("/", StaticFiles(directory="static",html = True), name="static")


def write_file(filename, bytes):
    with open(filename, 'wb') as binary_file:
        binary_file.write(bytes)