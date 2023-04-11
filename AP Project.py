import sqlib
con = sqlib.create_db_connection("127.0.0.1","alischer","alischer1","in_class_demo")
import matplotlib.pyplot as plt

# Gets All Possible Answers From Catagory and Gives How Many People Chose What
def basic_data():
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("""Questions posed to the students are under 4 main categories:
1: Grade
2: Pets
3: Siblings
4: Icecream""")
    print("-----------------------------------------------------------------------------------------------------------------------------------")

    cats = input("Please enter the coresponding number to the category you would like to learn more about: ")
# grade
    if cats == "1":
        search_var = """select grade from annie_ap;"""
        search_read = sqlib.read_query(con,search_var)
        fifth = 0
        sixth = 0
        seventh = 0
        eighth = 0
        ninth = 0
        tenth = 0
        eleventh = 0
        twelfth = 0
        for x in search_read:
            if x[0] == "5th":
                fifth += 1
            elif x[0] == "6th":
                sixth += 1
            elif x[0] == "7th":
                seventh += 1
            elif x[0] == "8th":
                eighth +=1
            elif x[0] == "9th":
                ninth += 1
            elif x[0] == "10th":
                tenth += 1
            elif x[0] == "11th":
                eleventh += 1
            elif x[0] == "12th":
                twelfth += 1
        number = fifth+sixth+seventh+eighth+ninth+tenth+eleventh+twelfth
        print(f"""Out of all {number} students
{fifth} are in 5th grade
{sixth} are in 6th
{seventh} are in 7th grade
{eighth} are in 8th grade
{ninth} are in 9th grade
{tenth} are in 10th grade
{eleventh} are in 11th grade
and {twelfth} are in 12th""")
# pet
    if cats == "2":
        search_var = """select pet from annie_ap;"""
        search_read = sqlib.read_query(con,search_var)
        dog = 0
        cat = 0
        fish = 0
        reptile = 0
        for x in search_read:
            if x[0] == "dog":
                dog += 1
            elif x[0] == "cat":
                cat += 1
            elif x[0] == "fish":
                fish += 1
            elif x[0] == "reptile":
                reptile += 1
        number = dog+cat+fish+reptile
        print(f"""Out of all {number} students
{dog} own dogs
{cat} own cats
{fish} own fish
and {reptile} own reptiles""")
# sib  
    if cats == "3":
        search_var = """select sib from annie_ap;"""
        search_read = sqlib.read_query(con,search_var)
        zero = 0
        one = 0
        two = 0
        three = 0
        four = 0
        for x in search_read:
            if x[0] == 0:
                zero += 1
            elif x[0] == 1:
                one += 1
            elif x[0] == 2:
                two += 1
            elif x[0] == 3:
                three +=1 
            elif x[0] == 4:
                four += 1
        number = zero+one+two+three+four
        print(f"""Out of all {number} students
{zero} have no siblings
{one} have one sibling
{two} have two siblings
{three} have three siblings
{four} have four siblings""")
# ice
    if cats == "4":
        search_var = """select ice from annie_ap;"""
        search_read = sqlib.read_query(con,search_var)
        cho = 0
        van = 0
        straw = 0
        mint = 0
        for x in search_read:
            if x[0] == "chocolate":
                cho += 1
            elif x[0] == "vanilla":
                van += 1
            elif x[0] == "strawberry":
                straw += 1
            elif x[0] == "mint":
                mint += 1
        number = cho+van+straw+mint
        print(f"""Out of all {number} students
{cho} like chocolate ice cream
{van} like vanilla ice cream
{straw} like strawberry ice cream
{mint} like mint ice cream""")

# To compare data from different catagories
def compare_data():
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("""Questions posed to the students are under 4 main categories:
1: Grade
2: Pets
3: Siblings
4: Icecream""")
    print("-----------------------------------------------------------------------------------------------------------------------------------")

    cats = input("Please enter the coresponding numbers of the 2 catagories you would like to compare separated by a space: ")
    print("")
    cats = list(map(int,cats.strip().split()))
    catone = cats[0]
    cattwo = cats[1]
    rowone = ""
    rowtwo = ""
    if catone == 1:
        rowone = "grade"
    elif catone == 2:
        rowone = "pet"
    elif catone == 3:
        rowone = "sib"
    elif catone == 4:
        rowone = "ice"
    
    if cattwo == 1:
        rowtwo = "grade"
    elif cattwo == 2:
        rowtwo = "pet"
    elif cattwo == 3:
        rowtwo = "sib"
    elif cattwo == 4:
        rowtwo = "ice"

    grades = ["5th","6th","7th","8th","9th","10th","11th","12th"]
    pets = ["dog","cat","fish","reptile"]
    sibs = ["0","1","2","3","4"]
    ices = ["chocolate","vanilla","strawberry","mint"]
    list_thing = []

# The Code that is doing the comparing
# Have to return stuff
    def grade_comp(intro):
        fifth = 0
        sixth = 0
        seventh = 0
        eighth = 0
        ninth = 0
        tenth = 0
        eleventh = 0
        twelfth = 0
        for y in x:
            if y[0] == "5th":
                fifth += 1
            elif y[0] == "6th":
                sixth += 1
            elif y[0] == "7th":
                seventh += 1
            elif y[0] == "8th":
                eighth +=1
            elif y[0] == "9th":
                ninth += 1
            elif y[0] == "10th":
                tenth += 1
            elif y[0] == "11th":
                eleventh += 1
            elif y[0] == "12th":
                twelfth += 1
        print(f"""{intro}
{fifth} are in 5th grade
{sixth} are in 6th grade
{seventh} are in 7th grade
{eighth} are in 8th grade
{ninth} are in 9th grade
{tenth} are in 10th grade
{eleventh} are in 11th grade
and {twelfth} are in 12th grade
""")

    def pet_comp(intro):
            dog = 0
            cat = 0
            fish = 0
            reptile = 0
            for y in x:
                if y[0] == "dog":
                    dog += 1
                elif y[0] == "cat":
                    cat += 1
                elif y[0] == "fish":
                    fish += 1
                elif y[0] == "reptile":
                    reptile += 1
            print(f"""{intro}
{dog} have a dog
{cat} have a cat
{fish} have a fish
and {reptile} have a reptile
""")

    def sib_comp(intro):
        zero = 0
        one = 0
        two = 0
        three = 0
        four = 0
        for y in x:
            if y[0] == 0:
                zero += 1
            elif y[0] == 1:
                one += 1
            elif y[0] == 2:
                two += 1
            elif y[0] == 3:
                three +=1 
            elif y[0] == 4:
                four += 1
        print(f"""{intro}
{zero} of them have 0 siblings
{one} of them have 1 sibling
{two} of them have 2 siblings
{three} of them have 3 siblings
and {four} of them have 4 siblings
""")

    def ice_comp(intro):
        cho = 0
        van = 0
        straw = 0
        mint = 0
        for x in search_read:
            if x[0] == "chocolate":
                cho += 1
            elif x[0] == "vanilla":
                van += 1
            elif x[0] == "strawberry":
                straw += 1
            elif x[0] == "mint":
                mint += 1
        print(f"""{intro}
{cho} like chocolate ice cream
{van} like vanilla ice cream
{straw} like strawberry ice cream
{mint} like mint ice cream
""")

# Grade
    if rowone == "grade":
        for x in grades:
            search_var = (f"""select {rowtwo} from annie_ap where {rowone}='{x}';""")
            search_read = sqlib.read_query(con,search_var)
            list_thing.append(search_read)
        
        if rowtwo == "grade":
                print("You inputted the number for grade twice. Comparison only works if the two things your comparing are different.")
        
        elif rowtwo == "pet":
            grade_set = 0
            for x in list_thing:
                pet_comp(f"Of all the students in {grades[grade_set]} grade:")
                grade_set +=1
        
        elif rowtwo == "sib":
            grade_set = 0
            for x in list_thing:
                sib_comp(f"Of all the students in {grades[grade_set]} grade:")
                grade_set += 1
        
        elif rowtwo == "ice":
            grade_set = 0
            for x in list_thing:
                ice_comp(f"Of all the students in {grades[grade_set]} grade:")
                grade_set += 1

# Pet
    elif rowone == "pet":
        for x in pets:
            search_var = (f"""select {rowtwo} from annie_ap where {rowone}='{x}';""")
            search_read = sqlib.read_query(con,search_var)
            list_thing.append(search_read)
        
        if rowtwo == "grade":
            pet_set = 0
            for x in list_thing:
                grade_comp(f"Of all the students who have a {pets[pet_set]} as a pet:")
                pet_set +=1

        elif rowtwo == "pet":
                print("You inputted the number for grade twice. Comparison only works if the two things your comparing are different.")

        elif rowtwo == "sib":
            pet_set = 0
            for x in list_thing:
                sib_comp(f"Of all the students who have a {pets[pet_set]} as a pet:")
                pet_set +=1

        elif rowtwo == "ice":
            pet_set = 0
            for x in list_thing:
                ice_comp(f"Of all the students who have a {pets[pet_set]} as a pet:")
                pet_set +=1

# Sib  
    elif rowone == "sib":
        for x in sibs:
            search_var = (f"""select {rowtwo} from annie_ap where {rowone}='{x}';""")
            search_read = sqlib.read_query(con,search_var)
            list_thing.append(search_read)
        
        if rowtwo == "grade":
            sib_set = 0
            for x in list_thing:
                grade_comp(f"Of all the students with {sibs[sib_set]} sibling(s):")
                sib_set +=1
        
        elif rowtwo == "pet":
            sib_set = 0
            for x in list_thing:
                pet_comp(f"Of all the students with {sibs[sib_set]} sibling(s):")
                sib_set +=1
        
        elif rowtwo == "sib":
                print("You inputted the number for grade twice. Comparison only works if the two things your comparing are different.")

        elif rowtwo == "ice":
            sib_set = 0
            for x in list_thing:
                ice_comp(f"Of all the students with {sibs[sib_set]} sibling(s):")
                sib_set +=1

# Ice
    elif rowone == "ice":
        for x in ices:
            search_var = (f"""select {rowtwo} from annie_ap where {rowone}='{x}';""")
            search_read = sqlib.read_query(con,search_var)
            list_thing.append(search_read)
        
        if rowtwo == "grade":
            ice_set = 0
            for x in list_thing:
                grade_comp(f"Of all the students who like {ices[ice_set]} ice cream:")
                ice_set +=1
        
        elif rowtwo == "pet":
            ice_set = 0
            for x in list_thing:
                pet_comp(f"Of all the students who like {ices[ice_set]} ice cream:")
                ice_set +=1

        elif rowtwo == "sib":
            ice_set = 0
            for x in list_thing:
                sib_comp(f"Of all the students who like {ices[ice_set]} ice cream:")
                ice_set +=1

        elif rowtwo == "ice":
                print("You inputted the number for grade twice. Comparison only works if the two things your comparing are different.")

# Graph data
def graph_data():
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("""Questions posed to the students are under 4 main categories:
1: Grade
2: Pets
3: Siblings
4: Icecream""")
    print("-----------------------------------------------------------------------------------------------------------------------------------")

    cats = input("Please enter the coresponding number of the catagory you would like to graph separated by a space: ")
# Grade
    if cats == "1":
        search_var = """select grade from annie_ap;"""
        search_read = sqlib.read_query(con,search_var)
        fifth = 0
        sixth = 0
        seventh = 0
        eighth = 0
        ninth = 0
        tenth = 0
        eleventh = 0
        twelfth = 0
        for x in search_read:
            if x[0] == "5th":
                fifth += 1
            elif x[0] == "6th":
                sixth += 1
            elif x[0] == "7th":
                seventh += 1
            elif x[0] == "8th":
                eighth +=1
            elif x[0] == "9th":
                ninth += 1
            elif x[0] == "10th":
                tenth += 1
            elif x[0] == "11th":
                eleventh += 1
            elif x[0] == "12th":
                twelfth += 1
        info = [fifth, sixth, seventh, eighth, ninth, tenth, eleventh, twelfth]
        plt.pie(info)
        # save or something
# Pet
    elif cats == "2":
        search_var = """select pet from annie_ap;"""
        search_read = sqlib.read_query(con,search_var)
        dog = 0
        cat = 0
        fish = 0
        reptile = 0
        for x in search_read:
            if x[0] == "dog":
                dog += 1
            elif x[0] == "cat":
                cat += 1
            elif x[0] == "fish":
                fish += 1
            elif x[0] == "reptile":
                reptile += 1
        info = [dog, cat, fish, reptile]
        plt.pie(info)
        # save or something
# Sib
    elif cats == "3":
        search_var = """select sib from annie_ap;"""
        search_read = sqlib.read_query(con,search_var)
        zero = 0
        one = 0
        two = 0
        three = 0
        four = 0
        for x in search_read:
            if x[0] == 0:
                zero += 1
            elif x[0] == 1:
                one += 1
            elif x[0] == 2:
                two += 1
            elif x[0] == 3:
                three +=1 
            elif x[0] == 4:
                four += 1
        info = [zero,one,two,three,four]
        plt.pie(info)
        # save or something
# Ice
    elif cats == "4":
        search_var = """select ice from annie_ap;"""
        search_read = sqlib.read_query(con,search_var)
        cho = 0
        van = 0
        straw = 0
        mint = 0
        for x in search_read:
            if x[0] == "chocolate":
                cho += 1
            elif x[0] == "vanilla":
                van += 1
            elif x[0] == "strawberry":
                straw += 1
            elif x[0] == "mint":
                mint += 1
        info = [cho,van,straw,mint]
        plt.pie(info)
        # save or something
# End of graph_data func

print("This code uses randomly generated data.")
print("-----------------------------------------------------------------------------------------------------------------------------------")
print("""There are 3 ways in which you can choose to display the data:
1: Written Data
2: Compare Data
3: Graph Data""")
      
choice = int(input("Enter the coresponding number of the method you would like to use: "))

if choice == 1:
    basic_data()
elif choice == 2:
    compare_data()
elif choice == 3:
    graph_data()
else:
    print("That was not an option.")