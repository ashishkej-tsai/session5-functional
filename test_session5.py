import subprocess
import sys
import random
import math
from decimal import Decimal
import decimal

import pytest
import session4
import time
import os.path
import re
import inspect 

README_CONTENT_CHECK_FOR = [
    'Qualean',
    'Decimal',
    'Test Cases',
]

def test_add_100_times():
    tot_sum = Decimal('0')
    q = Decimal(str(session4.Qualean(1)))
    for _ in range(100):
        tot_sum += q
    assert tot_sum == 100 * q, "q + q + ... 100 times is not equal to 100 * q"

def test_qualean_eq_decimal_sqrt():
    q = session4.Qualean(1)
    if q.imag < 0:
        q.imag = q.__invertsign__()
    assert q.__sqrt__() == Decimal(str(q)).sqrt(), "Sqrt Function is not equal to Decimal sqrt"

def test_sum_million_different_eq_zero():
    with decimal.localcontext() as ctx:
        ctx.prec = 10
        tot_sum = Decimal('0')
        for _ in range(1000000):
            tot_sum += Decimal(str(session4.Qualean(random.choice([-1,0,1]))))
    
    assert math.isclose(tot_sum,0.0), "Sum of million different Qualeans should be close to zero"

def test_and_undefined():
    q1 = session4.Qualean(0) #q1 is False
    assert (q1 and q2) == False, "With undefined q2 and q1 False AND is not working"

def test_or_undefined():
    q1 = session4.Qualean(1) #q1 is not False
    assert (q1 or q2), "With undefined q2 and q1 not False OR is not working"

def test_and_functionality():
    q1 = session4.Qualean(1) #q1 is not False
    q2 = session4.Qualean(0) #q2 False
    assert q1.__and__(q2) == q2.imag, "AND function is not working"
    assert q1.__and__(q1) == q1.imag, "AND function is not working"
    assert q2.__and__(q2) == q2.imag, "AND function is not working"

def test_or_functionality():
    q1 = session4.Qualean(1) #q1 is not False
    q2 = session4.Qualean(0) #q2 False
    assert q1.__or__(q2) == q1.imag, "OR function is not working"
    assert q1.__or__(q1) == q1.imag, "OR function is not working"
    assert q2.__or__(q2) == q2.imag, "OR function is not working"

def test_le_functionality():
    q1 = session4.Qualean(1) #q1 is not False
    q2 = session4.Qualean(0) #q2 False
    if q1.imag > 0:
        assert q1.__le__(q2) == False, "LE function is not working"
        assert q1.__le__(q1) == True, "LE function is not working"
        assert q2.__le__(q2) == True, "LE function is not working"
    else:
        assert q1.__le__(q2) == True, "LE function is not working"
        assert q1.__le__(q1) == True, "LE function is not working"
        assert q2.__le__(q2) == True, "LE function is not working"

def test_lt_functionality():
    q1 = session4.Qualean(1) #q1 is not False
    q2 = session4.Qualean(0) #q2 False
    if q1.imag > 0:
        assert q1.__lt__(q2) == False, "LT function is not working"
        assert q1.__lt__(q1) == False, "LT function is not working"
        assert q2.__lt__(q2) == False, "LT function is not working"
    else:
        assert q1.__lt__(q2) == True, "LT function is not working"
        assert q1.__lt__(q1) == False, "LT function is not working"
        assert q2.__lt__(q2) == False, "LT function is not working"

def test_gt_functionality():
    q1 = session4.Qualean(1) #q1 is not False
    q2 = session4.Qualean(0) #q2 False
    if q1.imag < 0:
        assert q1.__gt__(q2) == False, "GT function is not working"
        assert q1.__gt__(q1) == False, "GT function is not working"
        assert q2.__gt__(q2) == False, "GT function is not working"
    else:
        assert q1.__gt__(q2) == True, "GT function is not working"
        assert q1.__gt__(q1) == False, "GT function is not working"
        assert q2.__gt__(q2) == False, "GT function is not working"

def test_ge_functionality():
    q1 = session4.Qualean(1) #q1 is not False
    q2 = session4.Qualean(0) #q2 False
    if q1.imag < 0:
        assert q1.__ge__(q2) == False, "GE function is not working"
        assert q1.__ge__(q1) == True, "GE function is not working"
        assert q2.__ge__(q2) == True, "GE function is not working"
    else:
        assert q1.__ge__(q2) == True, "GE function is not working"
        assert q1.__ge__(q1) == True, "GE function is not working"
        assert q2.__ge__(q2) == True, "GE function is not working"

def test_eq_functionality():
    q1 = session4.Qualean(1) #q1 is not False
    q2 = session4.Qualean(0) #q2 False
    assert q1.__eq__(q2) == False, "EQ function is not working"
    assert q1.__eq__(q1) == True, "EQ function is not working"
    assert q2.__eq__(q2) == True, "EQ function is not working"

def test_qualean_value_error_real():
    with pytest.raises(ValueError, match=r".* must .*"):
        session4.Qualean(2.0), 'Real Number must be either -1, 0 , 1 value error'

def test_invertsign_functionality():
    q1 = session4.Qualean(1) #q1 is not False
    assert q1.__invertsign__() == -q1.imag, "INVERT SIGN function is not working"

def test_add_functionality():
    q1 = session4.Qualean(1) 
    q2 = session4.Qualean(-1) 
    q1.imag = Decimal('0.5')
    q2.imag = Decimal('0.4')
    assert q1.__add__(q2) == Decimal('0.9'), "ADD function is not working"

def test_sqrt_functionality():
    q1 = session4.Qualean(1) #q1 is not False
    q1.imag = Decimal('4')
    assert q1.__sqrt__() == Decimal('2'), "SQRT function is not working"

def test_mul_functionality():
    q1 = session4.Qualean(1) #q1 is not False
    q2 = session4.Qualean(0) #q2 False
    assert q1.__mul__(q2) == 0, "MUL function not working"

def test_bool_functionality():
    q1 = session4.Qualean(0) #q1 is not False
    q2 = session4.Qualean(1) #q2 False
    assert q1.__bool__() == False, "BOOL function is not working"
    assert q2.__bool__() == True, "BOOL function is not working"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

    
def test_all_funcs_present():
    functions = inspect.getmembers(session4, inspect.isfunction)
    funcs = ["_and__",  "__or__", "__repr__", "__str__", "__add__", "__eq__", "__float__", "__ge__", "__gt__", "__invertsign__", 
                    "__le__", "__lt__", "__mul__", "__sqrt__", "__bool__"]
    for func in functions:
        assert func in code_lines, func + ' not implemented'

def test_fourspace():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

