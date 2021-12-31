# def fizzbuzz(n=100):
#     """returns: a string with lines 1 through n,
#     where the ith line is "Fizz" if is divisible by 3 but not 5,
#                           "Buzz" if its divisible by 5 but not 3,
#                           "FizzBuzz" if its divisible by both,
#                           and the number itself if divisible by neither
#     """
#     out = ''
#     for num in range(1,n+1):
#         if num % 3 == 0 and num % 5 == 0:
#             out += "FizzBuzz\n"
#             continue
#         elif num % 3 == 0:
#             out += "Fizz\n"
#             continue
#         elif num % 5 == 0:
#             out += "Buzz\n"
#             continue
#         else:
#             out += f'{num}\n'
#     return out

def fizzbuzz(n=100):
    """returns: a string with lines 1 through n,
    where the ith line is "Fizz" if is divisible by 3 but not 5,
                          "Buzz" if its divisible by 5 but not 3,
                          "FizzBuzz" if its divisible by both,
                          and the number itself if divisible by neither
    """
    out = ''
    for num in range(1,n+1):
        if num % 3 == 0 and num % 5 == 0:
            out += "FizzBuzz\n"
            continue
        elif num % 3 == 0:
            out += "Fizz\n"
            continue
        elif num % 5 == 0:
            out += "Buzz\n"
            continue

    return out