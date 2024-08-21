from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config import *
import uvicorn
from models import AgentModel, WEngineModel
import json

from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/media", StaticFiles(directory = MEDIA_DIR), name = 'media')

import views

origins = ["*"]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)



def main():
	uvicorn.run("main:app", host = host, port = port, reload=True)

if __name__ == "__main__":
	main()

