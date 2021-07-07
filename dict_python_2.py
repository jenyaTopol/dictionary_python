def doesKeyExist(d, k):
    '''
    checks if key exists in dictionary
    :param d: dictionary
    :param k: key
    :return: True if k exist in d
    '''
    # return k in d.keys() -- shorter
    if k in d.keys():
        return True
    else:
        return False


def tryAddValue(d, k, v):
    # add k+v into d only if they not exist already
    if doesKeyExist(d, k) == False:
        d[k] = v


def printDictionary(d):
    '''
    nice print of the d dictionary
    :param d: dictionary
    :return: None
    '''
    for k, v in d.items():
        print(f'Dictionary key : {k} = {v}')


def present_menu():
    print('Hello:')
    print('1. get city population by key')
    print('2. add city and population')
    print('3. remove city from dictionary')
    print('4. print dictionary')
    print('5. exit')
    print('please select 1-5')


def get_user_option():
    while True:
        user_opt = input("your choice:")
        if user_opt in ["1", "2", "3", "4", "5"]:
            return int(user_opt)


def print_value_from_key():
    key = input("please enter city name:")
    key = key.upper()  # extra
    if doesKeyExist(popMap, key):  # == True
        print(f'{key} = {popMap[key]}')
    else:
        print(f'city {key} not found')


def add_to_dict():
    while True:
        key = input("please enter new city name:")
        key = key.upper()  # extra
        if doesKeyExist(popMap, key):
            print('city already exist. try again.')
        else:
            break
    citizen_number = int(input("please enter numebr of citizens"))
    popMap[key] = citizen_number


def remove_from_dictionary():
    while True:
        key = input("please enter new city name:")
        key = key.upper()  # extra
        if doesKeyExist(popMap, key):
            break
        else:
            print('city NOT exist. try again.')
    del popMap[key]


popMap = {'TEL AVIV': 443939, 'LONDON': 8825000, 'PARIS': 0, 'TOKYO': 13929286}

while True:
    present_menu()
    user_choice = get_user_option()
    if user_choice == 5:
        break
    if user_choice == 1:
        print_value_from_key()
    elif user_choice == 2:
        add_to_dict()
    elif user_choice == 3:
        remove_from_dictionary()
    else:
        print(popMap)

print('Goodbye')

# help(doesKeyExist)
# help(dict)
