
def pull_information_from_File(file_):
    
    global_information = []

    for first_line in file_:
        global_information.append(first_line.split())
    
    return global_information
    


def filtering(state_year, information, enter_year):
    

    index_year = 0
    if len(state_year[1:]) >= 1:
        
        for i in state_year:
            if i == enter_year:
                index_year =  state_year.index(i)
                print(index_year)
    return 0




def main():
    file_ = open("population.txt", "r")
    file_information = pull_information_from_File(file_)

    enter_year = input("Enter Year: ")
    print(file_information[0])
    state_year = filtering(file_information[0], file_information[1:], enter_year)

   


main()

