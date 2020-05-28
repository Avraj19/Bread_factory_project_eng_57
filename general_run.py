from general_test_file import formated_name


# test setup
known_input = '    avraj   '
expected_output = 'Avraj'

f_name = formated_name('    avraj   ')
print(formated_name(known_input) == expected_output)