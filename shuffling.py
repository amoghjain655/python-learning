line_5 = "Amogh Jain"
print(line_5.upper())
print(line_5.lower())
print(line_5.swapcase())
import random
char = ['NaMEste ','AMogH ','JaIn ']
for x in range (1,100 ):
    random.shuffle(char)
    print(''.join(char).swapcase())