from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_home(request: Request, db: Session = Depends(get_db)):
    profiles = crud.get_profiles(db)
    return templates.TemplateResponse("index.html", {"request": request, "profiles": profiles})

@app.post("/profiles/add")
def add_profile(profile_name: str = Form(...), description: str = Form(""), db: Session = Depends(get_db)):
    crud.create_profile(db, schemas.ProfileCreate(profile_name=profile_name, description=description))
    return RedirectResponse("/", status_code=303)