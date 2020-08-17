import subprocess
import sys
import random



import pytest
import session5
from session5 import time_it, polygon_area, squared_power_list, speed_converter, temp_converter
import time
import os.path
import re
import inspect 

README_CONTENT_CHECK_FOR = [
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'Test Cases',
    'speed_converter',
    'time_it'
]



def test_print_type_error():
    with pytest.raises(TypeError, match=r".* keyword .*"):
        output, avg_time = time_it(print, 1, 2, 3, sep='-', endi= ' ***\n', repetitions=5)

def test_squared_power_list_type_error():
    with pytest.raises(TypeError, match=r".* keyword .*"):
        output, avg_time = time_it(squared_power_list, 1, sep='-', endi= ' ***\n', repetitions=5)

def test_polygon_area_type_error():
    with pytest.raises(TypeError, match=r".* keyword .*"):
        output, avg_time = time_it(polygon_area, 1, sep='-', endi= ' ***\n', repetitions=5)

def test_temp_converter_type_error():
    with pytest.raises(TypeError, match=r".* keyword .*"):
        output, avg_time = time_it(temp_converter, 1, sep='-', endi= ' ***\n', repetitions=5)

def test_speed_converter_type_error():
    with pytest.raises(TypeError, match=r".* keyword .*"):
        output, avg_time = time_it(speed_converter, 1, sep='-', endi= ' ***\n', repetitions=5)

def test_time_it_name_error():
    with pytest.raises(NameError, match=r".* is not .*"):
        output, avg_time = time_it(printi, 1, 2, 3, sep='-', endi= ' ***\n', repetitions=5)

def test_print_func():
    output, avg_time = time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=5)
    assert output == None, "Print functionality not working"

def test_squared_power_list_func():
    output, avg_time = time_it(squared_power_list,2, start=0, end=5, repetitions=5)
    assert output == [1,2,4,8,16,32], "squared_power_list functionality not working"

def test_polygon_area_func():
    output, avg_time = time_it(polygon_area, 2, sides=4, repetitions=5)
    assert round(output,2) == 4.0, "polygon_area functionality not working"

def test_temp_converter_func():
    output, avg_time = time_it(temp_converter, 32, temp_given_in = 'f', repetitions=5)
    assert output == 0, "temp_converter functionality not working"

def test_speed_converter_func():
    output, avg_time = time_it(speed_converter, 100, dist='m', time='hr', repetitions=5)
    assert output == 100000, "Print functionality not working"

def test_squared_power_list_value_error():
    with pytest.raises(ValueError, match=r".* greater .*"):
        output, avg_time = time_it(squared_power_list,2, start=-10, end=5, repetitions=5)

def test_polygon_area_value_error():
    with pytest.raises(ValueError, match=r".* can be .*"):
        output, avg_time = time_it(polygon_area, 2, sides=2, repetitions=5)

def test_temp_converter_value_error():
    with pytest.raises(ValueError, match=r".* can be .*"):
        output, avg_time = time_it(temp_converter, 32, temp_given_in = 'r', repetitions=5)

def test_speed_converter_value_error():
    with pytest.raises(ValueError, match=r".* can be .*"):
        output, avg_time = time_it(speed_converter, -100, dist='m', time='hr', repetitions=5)

def test_speed_converter_dist_value_error():
    with pytest.raises(ValueError, match=r".* can be .*"):
        output, avg_time = time_it(speed_converter, 10, dist='min', time='hr', repetitions=5)

def test_speed_converter_time_value_error():
    with pytest.raises(ValueError, match=r".* can be .*"):
        output, avg_time = time_it(speed_converter, 10, dist='m', time='km', repetitions=5)

def test_other_print_value_error():
    with pytest.raises(ValueError, match=r".* can .*"):
        output, avg_time = time_it(speed_converter, 10, 20, dist='min', time='hr', repetitions=5)

def test_time_it_value_error():
    with pytest.raises(ValueError, match=r".* less .*"):
        output, avg_time = time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=0)
    
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
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

    
def test_all_funcs_present():
    code_lines = inspect.getsource(session5)
    funcs = ["squared_power_list","polygon_area","temp_converter","speed_converter","time_it"]
    for func in funcs:
        assert func in code_lines, func + ' not implemented'

def test_fourspace():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

