import random

def guess_random_number ():

    max_value = int(input('最大値を入力してください\n'))
    while True:
        min_value = int(input('最小値を入力してください\n'))
        if max_value > min_value:
            break
        else:
            print('最小値は最大値より小さくする必要があります。もう一度入力してください。')

    random_number = random.randint(min_value, max_value)
    attempt = 0
    max_attempt = 5

    print(f"{min_value}から{max_value}の範囲で数字を当ててください。今の試行回数は{attempt}です。")

    while attempt < max_attempt:
        guess = int(input('数字を入力してください： '))
        attempt += 1

        if guess < random_number:
            print('もっと大きい数かも。')
        elif guess > random_number:
            print('もっと小さいんじゃない？')
        else:
            print(f'正解！{attempt}回目で。')
            break
    else:
        print(f'正解は{random_number}でした。')

guess_random_number()



