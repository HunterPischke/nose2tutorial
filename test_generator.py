
def test_odds():
    for i in range(2, 10):
        yield check_odd, i

def check_odd(n):
    assert (n*n)-1 % 2 != 0
