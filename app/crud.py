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


def Get(id):

    db = SessionLocal()

    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        return response(None, "Student not found")

    return response({
        "id": student.id,
        "Name": student.Name,
        "Email": student.Email,
        "Age": student.Age
    }, "Get Student")


def Update(id, data):

    db = SessionLocal()

    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        return response(None, "Student not found")

    student.Name = data.Name
    student.Email = data.Email
    student.Age = data.Age

    db.commit()
    db.refresh(student)

    return response({
        "id": student.id,
        "Name": student.Name,
        "Email": student.Email,
        "Age": student.Age
    }, "Update Done")


def Delete(id):

    db = SessionLocal()

    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        return response(None, "Student not found")

    db.delete(student)
    db.commit()

    return response({"id": id}, "Delete Done")
