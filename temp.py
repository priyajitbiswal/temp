def format_output(x, spec):
    return f"{x:{spec}}"
x = 1234.56789
print(format_output(x, '0.2f'))  # Output: 1234.56
print(format_output(x, '>10.1f'))  # Output:    1234.5
print(format_output(x, '<10.1f')) 
#hi what do I do??