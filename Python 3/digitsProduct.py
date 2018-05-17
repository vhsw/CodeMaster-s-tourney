# Given an integer product, find the smallest positive 
# (i.e. greater than 0) integer the product of whose digits is equal to product.
#  If there is no such integer, return -1 instead.


def digitsProduct(product):

    answerDigits = []
    answer = 0

    if product == 0:
        return 10

    if product == 1:
        return 1

    for divisor in range(9, 1, -1):
        while product % divisor == 0:
            product /= divisor
            answerDigits.append(divisor)

    if product > 1:
        return -1


    for i in range(len(answerDigits) - 1, -1, -1):
        answer = 10 * answer + answerDigits[i]
    return answer

