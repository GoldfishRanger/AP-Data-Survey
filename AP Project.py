import sqlib
con = sqlib.create_db_connection("127.0.0.1","alischer","alischer1","in_class_demo")

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

    if rowone == "grade":
        for x in grades:
            search_var = (f"""select {rowtwo} from annie_ap where {rowone}='{x}';""")
            search_read = sqlib.read_query(con,search_var)
            print(search_read)
    elif rowone == "pet":
        for x in pets:
            search_var = (f"""select {rowtwo} from annie_ap where {rowone}='{x}';""")
            search_read = sqlib.read_query(con,search_var)
            print(search_read)
    elif rowone == "sib":
        for x in sibs:
            search_var = (f"""select {rowtwo} from annie_ap where {rowone}='{x}';""")
            search_read = sqlib.read_query(con,search_var)
            print(search_read)
    elif rowone == "ice":
        for x in ices:
            search_var = (f"""select {rowtwo} from annie_ap where {rowone}='{x}';""")
            search_read = sqlib.read_query(con,search_var)
            print(search_read)
    
    # figure out how to do below, and like display it afterwards
    # the first option of rowone compared to each option in rowtwo

    # if rowone == "grade":
    #     fifth = 0
    #     sixth = 0
    #     seventh = 0
    #     eighth = 0
    #     ninth = 0
    #     tenth = 0
    #     eleventh = 0
    #     twelfth = 0
    #     for x in search_read_one:
    #         if x[0] == "5th":
    #             fifth += 1
    #         elif x[0] == "6th":
    #             sixth += 1
    #         elif x[0] == "7th":
    #             seventh += 1
    #         elif x[0] == "8th":
    #             eighth +=1
    #         elif x[0] == "9th":
    #             ninth += 1
    #         elif x[0] == "10th":
    #             tenth += 1
    #         elif x[0] == "11th":
    #             eleventh += 1
    #         elif x[0] == "12th":
    #             twelfth += 1
    #     rowone_list = [fifth,sixth,seventh,eighth,ninth,tenth,eleventh,twelfth]
    # elif rowone == "pet":
    #     dog = 0
    #     cat = 0
    #     fish = 0
    #     reptile = 0
    #     for x in search_read_one:
    #         if x[0] == "dog":
    #             dog += 1
    #         elif x[0] == "cat":
    #             cat += 1
    #         elif x[0] == "fish":
    #             fish += 1
    #         elif x[0] == "reptile":
    #             reptile += 1
    #     rowone_list = [dog,cat,fish,reptile]
    # elif rowone == "sib":
    #     zero = 0
    #     one = 0
    #     two = 0
    #     three = 0
    #     four = 0
    #     for x in search_read_one:
    #         if x[0] == 0:
    #             zero += 1
    #         elif x[0] == 1:
    #             one += 1
    #         elif x[0] == 2:
    #             two += 1
    #         elif x[0] == 3:
    #             three +=1 
    #         elif x[0] == 4:
    #             four += 1
    #     rowone_list = [zero,one,two,three,four]
    # elif rowone == "ice":
    #     cho = 0
    #     van = 0
    #     straw = 0
    #     mint = 0
    #     for x in search_read_one:
    #         if x[0] == "chocolate":
    #             cho += 1
    #         elif x[0] == "vanilla":
    #             van += 1
    #         elif x[0] == "strawberry":
    #             straw += 1
    #         elif x[0] == "mint":
    #             mint += 1
    #     rowone_list = [cho,van,straw,mint]

    # if rowtwo == "grade":
    #     fifth = 0
    #     sixth = 0
    #     seventh = 0
    #     eighth = 0
    #     ninth = 0
    #     tenth = 0
    #     eleventh = 0
    #     twelfth = 0
    #     for x in search_read_two:
    #         if x[0] == "5th":
    #             fifth += 1
    #         elif x[0] == "6th":
    #             sixth += 1
    #         elif x[0] == "7th":
    #             seventh += 1
    #         elif x[0] == "8th":
    #             eighth +=1
    #         elif x[0] == "9th":
    #             ninth += 1
    #         elif x[0] == "10th":
    #             tenth += 1
    #         elif x[0] == "11th":
    #             eleventh += 1
    #         elif x[0] == "12th":
    #             twelfth += 1
    #     rowtwo_list = [fifth,sixth,seventh,eighth,ninth,tenth,eleventh,twelfth]
    # elif rowtwo == "pet":
    #     dog = 0
    #     cat = 0
    #     fish = 0
    #     reptile = 0
    #     for x in search_read_two:
    #         if x[0] == "dog":
    #             dog += 1
    #         elif x[0] == "cat":
    #             cat += 1
    #         elif x[0] == "fish":
    #             fish += 1
    #         elif x[0] == "reptile":
    #             reptile += 1
    #     rowtwo_list = [dog,cat,fish,reptile]
    # elif rowtwo == "sib":
    #     zero = 0
    #     one = 0
    #     two = 0
    #     three = 0
    #     four = 0
    #     for x in search_read_two:
    #         if x[0] == 0:
    #             zero += 1
    #         elif x[0] == 1:
    #             one += 1
    #         elif x[0] == 2:
    #             two += 1
    #         elif x[0] == 3:
    #             three +=1 
    #         elif x[0] == 4:
    #             four += 1
    #     rowtwo_list = [zero,one,two,three,four]
    # elif rowtwo == "ice":
    #     cho = 0
    #     van = 0
    #     straw = 0
    #     mint = 0
    #     for x in search_read_two:
    #         if x[0] == "chocolate":
    #             cho += 1
    #         elif x[0] == "vanilla":
    #             van += 1
    #         elif x[0] == "strawberry":
    #             straw += 1
    #         elif x[0] == "mint":
    #             mint += 1
    #     rowtwo_list = [cho,van,straw,mint]

    # number = 0
    # for x in rowone_list:
    #     number += x
    # print(number)

    # make sure its just two, get data, display good

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
    # make sure its just one, get data, display good

# End of graph_data func
# ITS OK TO LOOK UP HOW TF TO DO THIS
print("This code uses randomly generated data.")
print("-----------------------------------------------------------------------------------------------------------------------------------")
print("""There are 3 ways in which you can choose to display the data:
1: Written Data
2: Compare Data
3: Graph Data""")
      
choice = int(input("Enter the coresponding number of the method you would like to use: "))

# try:
if choice == 1:
    basic_data()
elif choice == 2:
    compare_data()
elif choice == 3:
    graph_data()
else:
    print("something went wrong")
# except:
#     print("something went wrong")