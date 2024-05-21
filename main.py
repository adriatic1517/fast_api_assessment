from fastapi.staticfiles import StaticFiles
from typing import Annotated
from fastapi import FastAPI, Form, File, UploadFile
#from mail import send_mail

app = FastAPI()

@app.post("/login")
async def login(firstname: Annotated[str, Form()], 
                lastname: Annotated[str, Form()], 
                email: Annotated[str, Form()], 
                cv: UploadFile):
    
    #Write file to read as attachment when sending mail
    cv_bytes = await cv.read()
    write_file(cv_bytes)

    return {"firstname": firstname, 
            "lastname": lastname,
            "email": email,
            "file_size": cv.filename, 
            "bytes": str(cv_bytes)}


app.mount("/", StaticFiles(directory="static",html = True), name="static")


def write_file(bytes):
    with open('resume', 'wb') as binary_file:
        binary_file.write(bytes)