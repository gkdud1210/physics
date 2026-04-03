from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    role = Column(String)

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True)
    title_ko = Column(String)
    title_en = Column(String)
    concept_ko = Column(String)
    concept_en = Column(String)
    difficulty = Column(String)
    question_text_ko = Column(String)
    question_text_en = Column(String)
    correct_answer = Column(String)
    explanation_ko = Column(String)
    explanation_en = Column(String)

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True)
    title_ko = Column(String)
    title_en = Column(String)
    due_date = Column(String)

class AssignmentProblem(Base):
    __tablename__ = "assignment_problems"
    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer)
    problem_id = Column(Integer)

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    assignment_id = Column(Integer)
    problem_id = Column(Integer)
    student_answer = Column(String)
    is_correct = Column(Boolean)
