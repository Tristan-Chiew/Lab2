print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

def get_user_input():
    lists = input("enter float")
    float_list = lists.split(",")
    Nout = []
    for i in float_list:
       Nout.append(float(float_list[i]))
    return Nout
def find_min_max():
    print("find max min function")
    return

if __name__ == "__main__":
    main()

def display_main_menu():
    variable = input("Enter some numbers seperated by commas (e.g 5,67,32)")

def calc_average():
    print("calc_average")


def sort_temperature():
    print("sort temp function")
    return

def calc_median_temperature():
    print("find median temp")
    return

def calc_average_temperature():
    temps = input("Enter all the temps seperated by a comma")
    sum,no = 0,0
    for int in temps:
        sum += int
        no += 1
    return sum/no

def calc_min_max_temperature():
    nos = input("Enter all the temps seperated by a comma")
    return max(nos),min(nos)



