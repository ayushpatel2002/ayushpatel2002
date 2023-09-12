
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def divisible(n, d):
    return int(n[:d]) % d == 0

def find_number():
    digits = '123456789'
    for p in permutations(digits):
        number = ''.join(p)
        if number[4] == 5:
            # print("Checking all the numbers and their divisibility...\n \n \n")
            if all(divisible(number, i) for i in range(1, 10)):
                return number
        else:
            continue
        print(number)

def check_divisibility(number):
    num_array_str = str(number)
    x= 1
    while x < 10:
        if int(num_array_str[0:x])%x == 0:
            quotient = int(num_array_str[0:x])//x
            print('The first %2d digit(s) which are %2d, and it is divisible by %2d and gives quotient as %2d' % (x, int(num_array_str[0:x]), x, quotient))
            print('')
            x = x+1
        else:
            print("The number is not the one we expected")
            break


result = find_number()
print("Our mysterious number is %11d" % int(result))
check_divisibility(result)