#Don't run this script ever!!!

import random
import time

def get_random_number_list():
    random_list = []

    i = 0

    while i < 9999999999999:
        i += 1

        random_number = random.random()
        random_number = i * random_number
        random_number = i * random_number
        random_number = i * random_number
        random_number = i * random_number
        random_number = i * random_number
        random_number = i * random_number
        random_number = i * random_number
        random_number = i * random_number

        if len(random_list) > 0 and i < len(random_list):
            if random_number < 1:
                random_number = random_number * random_list[i] / random_list[i - 1]
            else:
                random_number = random_number * random_list[i] / random_list[i - 1]

        random_list.append(random_number)
    
    return random_list

def destroy(i):
    p = 0
    broken_data = []
    random_list = get_random_number_list()


    while i > 0 or i < 0:
        p += 1
        i += 1

        random_number = i * random.random()
        random_number = i * random_number / random.random() * random.random() / random.random() * random.random() / random.random() / random.random()
        random_number = i * random_number / random.random() * random.random() / random.random() * random.random() / random.random() / random.random()
        random_number = i * random_number / random.random() * random.random() / random.random() * random.random() / random.random() / random.random()
        random_number = i * random_number / random.random() * random.random() / random.random() * random.random() / random.random() / random.random()
        random_number = i * random_number / random.random() * random.random() / random.random() * random.random() / random.random() / random.random()
        random_number = i * random_number / random.random() * random.random() / random.random() * random.random() / random.random() / random.random()
        random_number = i * random_number / random.random() * random.random() / random.random() * random.random() / random.random() / random.random()

        broken_data.append(random_number)

        print(broken_data)
    
    return random_list



def run():
    start_time = time.time()

    first=1000
    second=10000
    third=100000

    result = first * second / third * second / third * second / third * second / third * second / third * second / third * second / third * second / third * second / third * second / third * second / third * second / third * second / third * second / third * second / third * second / third

    try:
        result = destroy(int(result))
    except Exception:
        result = destroy(int(result))

    end_time = time.time()

    time_spent = end_time - start_time

    print(result)
    print("")
    print("Executed in time:", time_spent)


run()
