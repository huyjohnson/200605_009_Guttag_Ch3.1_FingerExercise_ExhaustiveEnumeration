# - Finger Exercise - Chapter 3.1
num = int(input('Please enter an integer: '))
root = 0
pwr = 2     # Started at 2 because all sets allowed for root**1 = num
endbound = 6
while pwr < endbound and root**pwr != abs(num):
    while root < abs(num):
        root += 1
        if root**pwr == abs(num):
            if num > 0:
                break
            elif num < 0 and pwr % 2 == 1:
                root = -root
                break
    if root**pwr == num:
        print('root = {}, pwr = {}'.format(root, pwr))
        break
    elif root == abs(num):
        root = 0
    pwr += 1
    
if pwr == endbound:
    print('No existing set of integers.')
