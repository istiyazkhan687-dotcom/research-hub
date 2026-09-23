from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

from database import engine, SessionLocal, Base
from models import SurveyModel

# ڈیٹا بیس ٹیبل بنانا
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Research Survey Exchange API",
    description="اکیڈمک ریسرچرز کے لیے سروے شیئرنگ اور مستقل ڈیٹا بیس سسٹم",
    version="1.1.0"
)

# Pydantic Schemas
class SurveyCreate(BaseModel):
    title: str
    researcher_name: str
    target_field: str
    form_link: str
    target_responses: int
    credits_offered: int = 10

class SurveyOut(SurveyCreate):
    id: int
    responses_collected: int
    is_active: bool

    class Config:
        from_attributes = True

# Database Session Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["General"])
def home():
    return {"message": "Academic Research Platform API with SQLite Database is running!"}

# تمام سرویز ڈیٹا بیس سے لانا
@app.get("/surveys", response_model=List[SurveyOut], tags=["Surveys"])
def list_surveys(db: Session = Depends(get_db)):
    return db.query(SurveyModel).all()

# نیا سروے مستقل محفوظ کرنا
@app.post("/surveys", response_model=SurveyOut, tags=["Surveys"])
def create_survey(survey: SurveyCreate, db: Session = Depends(get_db)):
    db_survey = SurveyModel(**survey.model_dump())
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

# مخصوص سروے حاصل کرنا
@app.get("/surveys/{survey_id}", response_model=SurveyOut, tags=["Surveys"])
def get_survey(survey_id: int, db: Session = Depends(get_db)):
    db_survey = db.query(SurveyModel).filter(SurveyModel.id == survey_id).first()
    if not db_survey:
        raise HTTPException(status_code=404, detail="سروے نہیں ملا")
    return db_survey



