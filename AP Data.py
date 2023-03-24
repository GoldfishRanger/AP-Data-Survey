import sqlib
con = sqlib.create_db_connection("127.0.0.1","alischer","alischer1","in_class_demo")

import sqlib
import random
data = []

con = sqlib.create_db_connection("127.0.0.1","alischer","alischer1","in_class_demo")

class movement:
    id = None
    grade = None
    pet = None
    sib = None
    ice = None

    def __init__(self, id):
        grade = random.randint(5,12)
        if grade == 5:
            grade = "5th"
        elif grade == 6:
            grade = "6th"
        elif grade == 7:
            grade = "7th"
        elif grade == 8:
            grade = "8th"
        elif grade == 9:
            grade = "9th"
        elif grade == 10:
            grade = "10th"
        elif grade == 11:
            grade = "11th"
        elif grade == 12:
            grade = "12th"
        self.grade = grade
        pet = random.randint(1,4)
        if pet == 1:
            pet = "dog"
        elif pet == 2:
            pet = "cat"
        elif pet == 3:
            pet = "fish"
        elif pet == 4:
            pet = "reptile"
        self.pet = pet
        sib = random.randint(0,4)
        self.sib = sib
        ice = random.randint(1,4)
        if ice == 1:
            ice = "chocolate"
        elif ice == 2:
            ice = "vanilla"
        elif ice == 3:
            ice = "strawberry"
        elif ice == 4:
            ice = "mint"
        self.ice = ice
        self.id = id
    
    def __str__(self):
        self = [self.id, self.grade, self.pet, self.sib, self.ice]

for x in range(1, 101):
    movementx = movement(x)
    move = """insert into annie_ap (id,grade,pet,sib,ice) values ('{id}','{grade}','{pet}','{sib}','{ice}');""".format(id = movementx.id, grade = movementx.grade, pet = movementx.pet, sib = movementx.sib, ice = movementx.ice)
    move_result = sqlib.execute_query(con, move)