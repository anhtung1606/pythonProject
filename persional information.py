def answer(prompt):
    while True:
        a = input(prompt).strip().lower()
        if a == 'yes':
            return True
        elif a == 'no':
            return False
        else:
            continue
def calculate_age(year_born):
    current_year = 2024
    a = current_year - int(year_born)
    return a
def convert(meter):
    feet = meter * 3.2808
    feet = round(feet, 2)
    return feet

def comparison_height(gender,height_feet,viet_nam):
    if gender == True:
        if height_feet >= 6.0:
            print('you are', end=' ')
            for i in range(5):
                print('very', end=' ')
            print('tall as a man ')

        elif height_feet > 5.8:
            print('you are tall')
        else:
            print('hơi lùn nha bro')
    else:
        if height_feet > 6:
            print('miss grand international')
        elif height_feet > 5.5:
            print('bé này cao vậy trời')
        else:
            print('cute girl')
    if viet_nam == True:
        print('we are đồng hương')
    else:
        print('tây à ')
    return(gender,height_feet,viet_nam)
def print_something(name,year_old,height_feet):
    print('---------')
    print('chao xìn ' + name)
    print('you are: ' + str(year_old) + ' year old')
    print('your height (feet): ' + str(height_feet))
def main():
    name = input('what your name: ')
    born = input('what year were you born: ')
    height_meter = float(input('your height (meter): '))
    gender = answer('Are you a male(yes/no) ')
    viet_nam = answer('you are VietNamese ??: ')
    year_old = calculate_age(born)
    height_feet = convert(height_meter)
    print_something(name, year_old, height_feet)
    comparison_height(gender,height_feet,viet_nam)


main()





































