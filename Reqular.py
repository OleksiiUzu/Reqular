import re
import random
import string


# Function to generate random text with a specified length
def generate_random_text(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace

    # Use random.choice to pick characters randomly and join them
    random_text = ''.join(random.choice(characters) for _ in range(length))

    return random_text


def time_check():
    for i in range(0, 29):
        for j in range(0, 90):
            pattern = r'[.|,|;|:|(|-|\s](([0-9]|[0-2][0-3]|1[0-9]|0[0-9]):([0-5][0-9]|[0-9]))[.|,|;|:|)|-|\s]'
            time = f'{generate_random_text(50)} {i}:{j} {generate_random_text(50)}'
            print(time, '\n')
            itms = re.findall(pattern, str(time))
            if itms:
                print(f"{i}:{j} - True, {itms}")
            else:
                print(f"{i}:{j} - False, {itms}")
            print('------------------')


time_check()
