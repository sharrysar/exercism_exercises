def is_armstrong_number(num):
    num = str(num)
    length_of_num = (len(num))
    total = 0
    for n in num:
        total += int(n) ** length_of_num

    if total != int(num):
        return False
    return True

print(is_armstrong_number(153))