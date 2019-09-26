

def pull_information_from_File(file_):
    
    header = []
    global_information = []

    for first_line in file_:
        global_information.append(first_line.split())
    print(header)
    
    


file_ = open("population.txt", "r")
pull_information_from_File(file_)










print(header)













#
# enterName = input("Please enter the year: ")


