# You have a apples, and your friend has b apples.
# You will be happy if - and only if - you both have the same number of apples.
# Given integers a and b, check if you will be happy after 
# you give your friend one of your apples.

def shareAnApple(a, b):
    return a - 1 == b + 1