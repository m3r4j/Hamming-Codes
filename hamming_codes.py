import random

def cal_valid_moves(skips, result):
    num = skips
    range_1 = 0

    count = 0
    arr = []

    while len(arr) != len(result):
        if count > len(result):
            break
        if count % 2 == 0:
            for i in range(range_1, num):
                arr.append(i)
                range_1 += 2
                num += 2
        count += 1

    return arr


def flip_parity_bits(sequence):
    result = []

    for i in sequence:
        ones = 0
        zeros = 0

        for x in i:
            if '0' in x:
                zeros += 1

            elif '1' in x:
                ones += 1

        if ones % 2 == 0:
            result.append('0')
        else:
            result.append('1')


    return result




def generate(data):
    result = []
    parity_bits = []
    count = 0
    indexes = []



    for x in range(len(data)):
        parity_bits.append(pow(2, x))



    for x in range(len(data) + 4):
        if x + 1 in parity_bits:
            result.append(None)
            indexes.append(x)
            continue

        else:
            if count < len(data):
                result.append(data[count])
                count += 1

    count = 1


    res = ''
    sequence = []
    length = len(result)


    for j in indexes:
        res_arr = result[j:]
        arr = cal_valid_moves(count, result)

        for x in range(len(res_arr)):
            if (arr[x] >= len(res_arr) or arr[x] >= len(res_arr) - 1):
                break

            if res_arr[arr[x]] != None:
                res += str(res_arr[arr[x]])


        count += count
        sequence.append(res)
        res = ''


    p_bits = flip_parity_bits(sequence)
    index = 0


    for x in p_bits:
        result[indexes[index]] = x
        index += 1


    result = ''.join(result)
    return result



def error_correct(data):
    parity_bits = []
    indexes = []
    data = list(data)
    result = data
    count = 1
    res = ''
    sequence = []



    for x in range(len(data)):
        parity_bits.append(pow(2, x))



    for x in range(len(data) + 4):
        if x + 1 in parity_bits:
            if x <= len(data):
                indexes.append(x)
            continue

    save_p_bits = []
    for i in indexes:
        if i <= len(result) - 1:
            save_p_bits.append(result[i])


    for j in indexes:
        res_arr = result[j:]
        arr = cal_valid_moves(count, result)

        for x in range(len(res_arr)):
            if (arr[x] >= len(res_arr) or arr[x] >= len(res_arr) - 1):
                break

            if res_arr[arr[x]] != None:
                res += str(res_arr[arr[x]])


        count += count
        sequence.append(res)
        res = ''


    for x in range(len(sequence)):
        sequence[x] = sequence[x][1:]


    p_bits = flip_parity_bits(sequence)


    index = 0
    
    new_indexes = indexes

    for x in range(len(new_indexes)):
        new_indexes[x] = new_indexes[x] + 1



    for x in range(len(p_bits)):
        if (x < len(p_bits) - 1 or x < len(save_p_bits) - 1):
            if p_bits[x] == save_p_bits[x]:
                continue
            else:
                index += new_indexes[x]


    index -= 1




    if result[index] == '0':
        result[index] = '1'

    elif result[index] == '1':
        result[index] = '0'

    result = ''.join(result)

    return result



def choose_rand_bit(string):
    string = list(string)
    index = random.randint(0,len(string) - 1)
    if string[index] == '1':
        string[index] = '0'

    elif string[index] == '0':
        string[index] = '1'

    return ''.join(string)




def generate_bits(amount):
    res = ''
    for i in range(amount):
        res += random.choice(['0','1'])
    return res


data = input('Enter your data: ')

result = generate(data)
print('GENERATED: ' + result)


result = choose_rand_bit(result)
print('ERROR: ' + result)


result = error_correct(result)
print('FIXED: ' + result)




'''
amount = 0

while amount != 100:
    check = []
    bit = generate_bits(12)
    result = generate(bit)
    print(result)
    check.append(result)
    data = choose_rand_bit(result)
    print(data)
    result = error_correct(data)
    print(result)
    check.append(result)

    if check[0] == check[1]:
        print(True)
    else:
        print(False)
    print()
    amount += 1


'''

