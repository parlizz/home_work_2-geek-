float_i = 12.443
int_i = 12
complex_i = complex(1, 2)
string_i = 'это строка'
list_i = [1, 2, 3]
tuple_i = tuple('это кортеж')
set_i = set('это набор')
bool_i = True
list_of_types = [float_i, int_i, complex_i, string_i, list_i, tuple_i, set_i, bool_i]

for variable in list_of_types:
    print(type(variable))
