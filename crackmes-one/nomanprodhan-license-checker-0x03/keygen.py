import random

def generate_valid_key():
    result_sum = 0
    result_license_code = ""
    while result_sum != 50:
        if result_sum >= 41:
            digit = 50 - result_sum
            result_license_code += str(digit)
            break
        else:
            digit = random.randint(0, 9)
            result_sum += digit
            result_license_code += str(digit)
    return result_license_code

NUM_OF_LICENCES = 12
for i in range(NUM_OF_LICENCES):
    print(generate_valid_key())
