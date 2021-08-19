from typing import Optional
"""Task1"""
def to_power(x, exp):

    if exp == 1:
        return x * exp
    else:
        if exp <= 0:
            raise Exception(ValueError, "This function works only with exp > 0")
        else:
            return x * to_power(x, exp-1)

"""Task2"""

def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) <= 1:
        return True
    else:
        if looking_str[0] == looking_str[-1]:
            return is_palindrome(looking_str[1:-1])
        else:
            return False

"""Task3"""

def mult(a: int, n: int) -> int:
    if a == 0:
        return 0
    elif a == 1:
        return n
    elif n == 1:
        return a
    elif n < 0:
        raise ValueError(Exception, "This function works only with postive integers")
    else:
        return n + mult(a - 1, n)

"""Task4"""

def reverse(input_str: str) -> str:
    if len(input_str)==0:
        return input_str
    else:
        return reverse(input_str[1:])+input_str[0]


"""Task5"""

def sum_of_digits(digit_string: str) -> int:
    if digit_string=="":
        return 0
    else:
        if digit_string.isdigit():
            return int(digit_string[0]) + sum_of_digits(digit_string[1:])
        else:
            raise Exception(ValueError("input string must be digit string"))


if __name__ == '__main__':
   x = to_power(20, 2)
   print(x)

   y = is_palindrome('b', 1)
   print(y)
   z = is_palindrome('bla', 1)
   print(z)
   m = mult(2,4)
   print(m)

   r = reverse('bla')
   print(r)

   s = sum_of_digits('12345')
   print(s)




