
def main():
    apple_weight = float(input('apple weight: '))
    money_given = float(input('money input: '))
    MONEY_PER_WEIGHT = 21

    calculating_apple_money = total(apple_weight,MONEY_PER_WEIGHT)
    returning_money = returning(calculating_apple_money, money_given)
    if returning_money == -1:
        print('not enough cash')
    else:
        print('money given for customer: ' + str(returning_money))

    a = count_money(returning_money)


def total(apple_weight,MONEY_PER_WEIGHT):
    return apple_weight * MONEY_PER_WEIGHT


def returning(calculating_apple_money, money_given):
    if money_given < calculating_apple_money:
        return -1
    return money_given - calculating_apple_money

def count_money(a):
#500,200,100,50,20,10,1
    count_500 = int(a / 500)
    a = a - 500* count_500
    a = int(a)
    if  count_500 != 0:
        print('500K: '+ str(int(count_500)))
    count_200 = int(a / 200)
    a = a - 200* count_200
    if  count_200 != 0:
        print('200K: ' + str(int(count_200)))
    count_100 = int(a / 100)
    a = a - 100 * count_100
    if  count_100 != 0:
        print('100K: ' + str(int(count_100)))
    count_50 = int(a / 50)
    a = a - 50 * count_50
    if  count_50 != 0:
        print('50K: ' + str(int(count_50)))
    count_20 = int(a / 20)
    a = a - 20 * count_20
    print('20K: ' + str(int(count_20)))
    count_10 = int(a / 10)
    a = a - 10 * count_10
    print('10K: ' + str(int(count_10)))
    count_5 = int(a / 5)
    a = a - 5 * count_5
    print('5K: ' + str(int(count_5)))
    count_1 = int(a / 1)
    a = a - 1* count_1
    print('1K: ' + str(int(count_1)))
    return a

main()