import sqlib
con = sqlib.create_db_connection("127.0.0.1","alischer","alischer1","in_class_demo")

# Gets All Possible Answers From Catagory(ies) and Gives How Many People Chose What
def basic_data():
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("""Questions posed to the students are under 4 main categories:
1: Grade
2: Pets
3: Siblings
4: Icecream""")
    print("-----------------------------------------------------------------------------------------------------------------------------------")

    cats = input("Please enter the coresponding number to the category you would like to learn more about separated by a space: ")
    cats = list(map(int,cats.strip().split()))
    if len(cats) == 1:
        print("that is too many")
    # make sure its just one, get data, display good

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

print("This code uses randomly generated data.")
print("-----------------------------------------------------------------------------------------------------------------------------------")
print("""There are 3 ways in which you can choose to display the data:
1: Written Data
2: Compare Data
3: Graph Data""")
      
choice = int(input("Enter the coresponding number of the method you would like to use: "))

try:
    if choice == 1:
        basic_data()
    elif choice == 2:
        compare_data()
    elif choice == 3:
        graph_data()
    else:
        print("that was not an option")
except:
    print("that was not an option")