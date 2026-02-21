from .models import Student
from .database import SessionLocal


def response(data,msg):
    return {"msg":msg,"data":data}


def Create(data):

    db = SessionLocal()

    student = Student(
        Name=data.Name,
        Email=data.Email,
        Age=data.Age
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return response({
        "id":student.id,
        "Name":student.Name,
        "Email":student.Email,
        "Age":student.Age
    },"Add Done")


def List():

    db = SessionLocal()

    students = db.query(Student).all()

    return response([
        {
            "id":s.id,
            "Name":s.Name,
            "Email":s.Email,
            "Age":s.Age
        }
        for s in students
    ],"Get Data")
