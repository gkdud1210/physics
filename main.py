from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------
# FRONTEND
# -----------------
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")

# -----------------
# AUTH (simple)
# -----------------
@app.post("/register")
def register(username: str, password: str, role: str, db: Session = Depends(get_db)):
    user = models.User(username=username, password=password, role=role)
    db.add(user)
    db.commit()
    return {"message": "User created"}

@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(username=username, password=password).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login success", "user_id": user.id, "role": user.role}

# -----------------
# PROBLEMS
# -----------------
@app.post("/problems")
def create_problem(problem: dict, db: Session = Depends(get_db)):
    p = models.Problem(**problem)
    db.add(p)
    db.commit()
    return {"message": "Problem created"}

@app.get("/problems")
def get_problems(db: Session = Depends(get_db)):
    return db.query(models.Problem).all()

# -----------------
# ASSIGNMENTS
# -----------------
@app.post("/assignments")
def create_assignment(data: dict, db: Session = Depends(get_db)):
    a = models.Assignment(title_ko=data["title_ko"], title_en=data["title_en"], due_date=data["due_date"])
    db.add(a)
    db.commit()

    for pid in data["problem_ids"]:
        ap = models.AssignmentProblem(assignment_id=a.id, problem_id=pid)
        db.add(ap)
    db.commit()

    return {"message": "Assignment created"}

@app.get("/assignments/{id}")
def get_assignment(id: int, db: Session = Depends(get_db)):
    return db.query(models.Assignment).filter_by(id=id).first()

# -----------------
# SUBMIT
# -----------------
@app.post("/submit")
def submit(data: dict, db: Session = Depends(get_db)):
    problem = db.query(models.Problem).filter_by(id=data["problem_id"]).first()
    is_correct = problem.correct_answer == data["answer"]

    s = models.Submission(
        student_id=data["student_id"],
        assignment_id=data["assignment_id"],
        problem_id=data["problem_id"],
        student_answer=data["answer"],
        is_correct=is_correct
    )
    db.add(s)
    db.commit()

    return {"correct": is_correct}

# -----------------
# WRONG ANSWERS
# -----------------
@app.get("/wrong-answers/{student_id}")
def wrong_answers(student_id: int, db: Session = Depends(get_db)):
    subs = db.query(models.Submission).filter_by(student_id=student_id, is_correct=False).all()

    result = []
    for s in subs:
        p = db.query(models.Problem).filter_by(id=s.problem_id).first()
        result.append({
            "question_ko": p.question_text_ko,
            "question_en": p.question_text_en,
            "your_answer": s.student_answer,
            "correct_answer": p.correct_answer,
            "explanation_ko": p.explanation_ko,
            "explanation_en": p.explanation_en
        })
    return result
