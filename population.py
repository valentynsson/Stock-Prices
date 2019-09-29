
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
                continue
            else:
                second_line[0] = second_line[0] + " " + second_line[1]
                second_line.remove(second_line[1])
                
    return global_information
    
def searching_in_list(index_, list_):
    
    special_year = []
    for i in list_:
        special_year.append(int(i[index_]))
    
    max_num = max(special_year)
    min_num = min(special_year)


    tuple_list = []
    for check_name in list_:
        if check_name[index_] == str(max_num):
            max_list = [check_name[0], max_num]
            tuple_list.append(max_list)

        if check_name[index_] == str(min_num):
            min_list = [check_name[0], min_num]
            tuple_list.append(min_list)
            
    
    return tuple_list


def filtering(information, enter_year):                        
         
    get_first_line = []
    for first_list in information:
        get_first_line.append(first_list)
    
        break

    if len(get_first_line[0]) >= 2 and enter_year in get_first_line[0]:
        
        try: 
            the_index_position = get_first_line[0].index(enter_year)
            information.remove(information[0])

            final_result = searching_in_list(the_index_position, information)
                        
            max_tuple = ()
            min_tuple = ()
            if final_result[0][1] < final_result[1][1]:
                min_tuple = (final_result[0][1], final_result[0][0])
                
            if final_result[1][1] < final_result[0][1]:
                min_tuple = (final_result[1][1], final_result[1][0])

            if final_result[0][1] > final_result[1][1]:
                max_tuple = (final_result[0][1], final_result[0][0])
            
            if final_result[1][1] > final_result[0][1]:
                max_tuple = (final_result[1][1], final_result[1][0])
            
        except:
            print("The Year do not exist")
        return min_tuple, max_tuple
    
    else:
        print("Invalid year!")
        return 0




def main():
    
  #  try:
        enter_file = input("Enter filename: ")
        file_ = open(enter_file, "r")
        file_information = pull_information_from_File(file_)
        
        
        enter_year = input("Enter Year: ")
        state_year = filtering(file_information, enter_year)
        print("Minimum: ", state_year[0])
        print("Maximum: ", state_year[1])

 #   except:
#        print("Filename {} not found!".format(enter_file))
        
main()
