def mylen(some_list):
    '''
    determines the length of a list
    '''
    if some_list == []:
        return 0
    else:
        return 1 + mylen(some_list[1:])

def intDivision(dividend, divisor):
    '''
    Integer division
    '''
    if type(dividend) is not int and type(divisor) is not int:
        raise Exception('Its not integer')
    if dividend <0 and divisor <=0:
        raise Exception('Its not positive')
    if dividend < divisor:
        return 0
    else:
        return 1 + intDivision(dividend-divisor,divisor)
    
def sumDigits(some_num):
    '''
    the sum of digits of an integer
    '''
    if some_num <= 0 :
        raise Exception('its not positive')
    if some_num < 10:
        return some_num
    return some_num % 10 + sumDigits(some_num // 10)

def reverseDisplay(some_num):
    '''
    reverse an integer
    '''
    if some_num <= 0:
        raise Exception('its not positive')
    if some_num < 10:
        print(some_num)
    else:
        print( some_num % 10, end = '') 
        reverseDisplay(some_num // 10)

def binary_search2(key,alist,low,high):
    '''
    finds and returns the position of key in alist
    or returns 'Item is not in the list'
    - key is the target integer that we are looking for
    - alist is a list of valid integers that is searched
    - low is the lowest index of alist
    - high is the highest index of alist
    '''
    # [-8,-2,10,3,5,7,9] key = 9
    if low > high:
        return 'Item is not in the list' 
    guess = (high + low) // 2
    if key == alist[guess]:
        return guess
    elif key < alist[guess]: 
        return binary_search2(key, alist, low, guess - 1)
    else: 
        return binary_search2(key, alist, guess + 1, high)
    
def main():
    alist=[43,'ss',97,86]
    print(mylen(alist))
    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print('Integer division', n, '//', m, '=', intDivision(n,m))
    number = int(input('Enter a number:'))
    print(sumDigits(number))
    number = int(input('Enter a number:'))
    reverseDisplay(number)
    some_list = [-8,-2,10,3,5,7,9]
    print(binary_search2(9,some_list,0,len(some_list)-1))
    print(binary_search2(-8,some_list,0,len(some_list)-1))
    print(binary_search2(4,some_list,0,len(some_list)-1))

main()
