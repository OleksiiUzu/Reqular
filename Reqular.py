import re


def time_check():
    for i in range(0, 24):
        i = str(i).zfill(2)
        for j in range(0, 60):
            j = str(j).zfill(2)
            pattern = r'^(?:[0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$'
            time = f'{i}:{j}'
            if re.match(pattern, str(time)):
                print(f"{time} - True")
            else:
                print(f"{time} - False")


time_check()
