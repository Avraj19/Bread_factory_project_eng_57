from general_test_file import *


# test setup
known_input = '    avraj   '
expected_output = 'Avraj'

f_name = formated_name('    avraj   ')
print(formated_name(known_input) == expected_output)

# say_hello test
hello_known_input = ' hello  '
hello_known_output = 'Hello'

print(formated_hello(hello_known_input) == hello_known_output)