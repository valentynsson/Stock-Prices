
def check_if_number(value):
    try: 
        value = int(value)
        return True

    except:
        return False        
    

def pull_information_from_File(file_):
    
    global_information = []

    for first_line in file_:
        global_information.append(first_line.split())
    
    for second_line in global_information:  
        check_num = check_if_number(second_line[1])
        
        if check_num == True:
            print(second_line[1])
        else:
            second_line[0] = second_line[0] + " " + second_line[1]
            print(second_line[0])
    return 0


def filtering(information, enter_year):                        
         
    return 0


def main():
    file_ = open("population.txt", "r")
    file_information = pull_information_from_File(file_)

    '''
    enter_year = input("Enter Year: ")
    state_year = filtering(file_information, enter_year)
    '''


main()

