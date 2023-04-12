import sqlib
con = sqlib.create_db_connection("127.0.0.1","alischer","alischer1","in_class_demo")
import numpy as np
import matplotlib.pyplot as plt

# Writes out data from each category
def basic_data():
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("""Questions posed to the students are under 4 main categories:
1: Grade
2: Pets
3: Siblings
4: Icecream""")
    print("-----------------------------------------------------------------------------------------------------------------------------------")

    cats = input("Please enter the coresponding number to the category you would like to learn more about: ")
    print("-----------------------------------------------------------------------------------------------------------------------------------")

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
        return(f"""
Out of all {number} students
{fifth} are in 5th grade
{sixth} are in 6th
{seventh} are in 7th grade
{eighth} are in 8th grade
{ninth} are in 9th grade
{tenth} are in 10th grade
{eleventh} are in 11th grade
and {twelfth} are in 12th
""")
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
        return(f"""
Out of all {number} students
{dog} own dogs
{cat} own cats
{fish} own fish
and {reptile} own reptiles
""")
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
        return(f"""
Out of all {number} students
{zero} have no siblings
{one} have one sibling
{two} have two siblings
{three} have three siblings
{four} have four siblings
""")
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
        return(f"""
Out of all {number} students
{cho} like chocolate ice cream
{van} like vanilla ice cream
{straw} like strawberry ice cream
{mint} like mint ice cream
""")

   
        print("I'm sorry but that was not an option")

# To compare data from two different categories
def compare_data():
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("""Questions posed to the students are under 4 main categories:
1: Grade
2: Pets
3: Siblings
4: Icecream""")
    print("-----------------------------------------------------------------------------------------------------------------------------------")

    cats = input("Please enter the coresponding numbers of the 2 catagories you would like to compare separated by a space: ")
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    cats = list(map(int,cats.strip().split()))
    catone = cats[0]
    cattwo = cats[1]
    rowone = ""
    rowtwo = ""
# To figure out what category is Row One
    if catone == 1:
        rowone = "grade"
    elif catone == 2:
        rowone = "pet"
    elif catone == 3:
        rowone = "sib"
    elif catone == 4:
        rowone = "ice"
# To figure out what category is Row Two
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

# The Functions that are doing the comparing
# Grade Comparing Func
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

-----------------------------------------------------------------------------------------------------------------------------------
""")
# Pet Comparing Func
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

-----------------------------------------------------------------------------------------------------------------------------------
""")
# Sibling Comparing Func
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

-----------------------------------------------------------------------------------------------------------------------------------
""")
# Ice Cream Comparing Func
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

-----------------------------------------------------------------------------------------------------------------------------------
""")

# Calls Comparsion Functions for Grade Specific Data
    if rowone == "grade":
        for x in grades:
            search_var = (f"""select {rowtwo} from annie_ap where {rowone}='{x}';""")
            search_read = sqlib.read_query(con,search_var)
            list_thing.append(search_read)
        
        if rowtwo == "grade":
                print("You inputted the number for grade twice. Comparison only works if the two things you're comparing are different.")
        
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

# Calls Comparsion Functions for Pet Specific Data
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
                print("You inputted the number for grade twice. Comparison only works if the two things you're comparing are different.")

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

# Calls Comparsion Functions for Sibling Specific Data
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
                print("You inputted the number for grade twice. Comparison only works if the two things you're comparing are different.")

        elif rowtwo == "ice":
            sib_set = 0
            for x in list_thing:
                ice_comp(f"Of all the students with {sibs[sib_set]} sibling(s):")
                sib_set +=1

# Calls Comparsion Functions for Ice Cream Specific Data
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
                print("You inputted the number for grade twice. Comparison only works if the two things you're comparing are different.")

# To Graph data in a bar graph
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
        label = ["5th","6th","7th","8th","9th","10th","11th","12th"]
    # Graph creation code taken from website below
    # https://www.python-graph-gallery.com/barplot/
        y_pos = np.arange(len(label))
        plt.bar(y_pos,info)
        plt.xticks(y_pos,label)
        plt.savefig("Grade_Graph.png")
        print("The PNG of the graph should be with your files.")
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
        label = ["Dog","Cat","Fish","Reptile"]
    # Graph creation code taken from website below
    # https://www.python-graph-gallery.com/barplot/
        y_pos = np.arange(len(label))
        plt.bar(y_pos,info)
        plt.xticks(y_pos,label)
        plt.savefig("Pet_Graph.png")
        print("The PNG of the graph should be with your files.")
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
        label = ["Zero","One","Two","Three","Four"]
    # Graph creation code taken from website below
    # https://www.python-graph-gallery.com/barplot/
        y_pos = np.arange(len(label))
        plt.bar(y_pos,info)
        plt.xticks(y_pos,label)
        plt.savefig("Sibling_Graph.png")
        print("The PNG of the graph should be with your files.")
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
        label = ["Chocolate","Vanilla","Strawberry","Mint"]
    # Graph creation code taken from website below
    # https://www.python-graph-gallery.com/barplot/
        y_pos = np.arange(len(label))
        plt.bar(y_pos,info)
        plt.xticks(y_pos,label)
        plt.savefig("Icecream_Graph.png")
        print("The PNG of the graph should be with your files.")
# End of graph_data func

print("This code uses randomly generated data.")
print("-----------------------------------------------------------------------------------------------------------------------------------")
print("""There are 3 ways in which you can choose to display the data:
1: Written Data
2: Compare Data
3: Graph Data""")

choice = input("Enter the coresponding number of the method you would like to use: ")

try:
    if choice == "1":
        print(basic_data())
    elif choice == "2":
        compare_data()
    elif choice == "3":
        graph_data()
    else:
        print("I'm sorry but that was not an option")
except:
    print("I'm sorry but that was not an option")