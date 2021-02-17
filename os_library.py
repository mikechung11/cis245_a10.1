import os
from os.path import isdir

def isValidPath(path):
    if os.path.isdir(path):
        return True
    else:
        print('That directory does not exist. Please try again.')
        return False

validDir = False
while validDir == False:
    print('Enter the directory location you want to save the file.')
    directory = input()
    validDir = isValidPath(directory)
os.chdir(directory)

print('Enter the name of the file (without any extension).')
filename = input() + '.txt'
print('Enter your name.')
name = input()
print('Enter your address.')
address = input()
print('Enter your phone number.')
phone = input()

with open(filename,'w') as file:
    file.write(', '.join([name,address,phone]))

with open(filename) as file:
    contents = file.read()

print('Location:')
print(os.path.join(directory,filename))
print('Contents:')
print(contents)
