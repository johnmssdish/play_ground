
def is_palindrome(n):
    if n < 10:
        return False
    q = n
    k = 0
    while n:
        print(f'n: {n}')
        print(f'k: {k}')
        k = k*10 + n % 10
        n = n//10
        print('after calculation:')
        print(f'n: {n}')
        print(f'k: {k}')
        print('\n')
    return k == q

def n_palindrome(n):
    n_str = str(n)
    if len(n_str) < 2:
        return False
    if n_str == n_str[::-1]:
        return True
    else:
        return False


def s_palindrome(s):
    print(f'list(s) : {list(s)}')
    a_list = list(s)
    a_list.reverse()
    print(f'list(s).reverse(): {a_list}')
    s_reverse = "".join(a_list)
    # print(reversed(s))
    print(f's_reverse: {s_reverse}')
    if s == s_reverse and s == s[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":

    assert not is_palindrome(1)
    assert not is_palindrome(10)
    assert not is_palindrome(201)
    assert is_palindrome(101)
    assert is_palindrome(14041)
    assert is_palindrome(11)
    assert s_palindrome('121')
    assert not s_palindrome('122')