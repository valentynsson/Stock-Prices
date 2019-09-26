

def pull_information_from_File(file_):
    
    header = []
    global_information = []

    for first_line in file_:
        global_information.append(first_line.split())
    
    header.append(global_information[0])
    global_information.pop(0)
    
    return header, global_information
    


file_ = open("population.txt", "r")
file_information = pull_information_from_File(file_)
print(file_information[0])






















#
# enterName = input("Please enter the year: ")


