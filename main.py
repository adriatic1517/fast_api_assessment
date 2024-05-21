from fastapi.staticfiles import StaticFiles
from typing import Annotated
from fastapi import FastAPI, Form, File, UploadFile
from mail import send_mail

app = FastAPI()

@app.post("/login")
async def login(firstname: Annotated[str, Form()], 
                lastname: Annotated[str, Form()], 
                email: Annotated[str, Form()], 
                cv: UploadFile):
    
    #Write file to read as attachment when sending mail
    write_file('resume', await cv.read())

    send_mail('Alma', [email], 'Thanks for your interest!', 'Hi, thanks for signing up.', ['resume'])
    send_mail('Alma', ['emadalma40@gmail.com'], 'New lead' + str(email), 'There is a new lead', ['resume'])

    return {
            "firstname": firstname, 
            "lastname": lastname,
            "email": email
            }


app.mount("/", StaticFiles(directory="static",html = True), name="static")


def write_file(filename, bytes):
    with open(filename, 'wb') as binary_file:
        binary_file.write(bytes)