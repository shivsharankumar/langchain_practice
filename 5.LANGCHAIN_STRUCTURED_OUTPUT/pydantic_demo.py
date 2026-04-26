from pydantic import BaseModel, Field,EmailStr
from typing import Optional
class Student(BaseModel):
    name:str ='shiv'#default value
#optional field
    age:Optional[int]
    #email type
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5,description="Grade Point Average of student")#validation for cgpa between 0 and 10
# new_student={"name":"John Doe"}
# new_student={'age': 25}
#type coercing
# new_student={'age': '25'}
new_student={'age': '25','email': 'john.doe@example.com','cgpa': 8.5}

Student=Student(**new_student)
print(Student)
dict_student=dict(Student)
print(dict_student)
student_json=Student.model_dump_json()
print(student_json)