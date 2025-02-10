def main():
    letter = int(input('how many letter do you want: '))
    num_to_choose = int(input('how many number do you want: '))
    symbol = input('how many symbol do you want: ')

    structure(num_to_choose,letter)

def structure(num_to_choose,letter_to_choose):
    import random
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random_numbers = random.sample(numbers, num_to_choose)
    random_letters = random.sample(letters,letter_to_choose)
    print(f"The random numbers chosen are: {random_numbers}")
    print(f"The random letters chosen are: { random_letters}")
    print(random_numbers + random_letters)



main()


