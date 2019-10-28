def explain_strings(list_value):
    if list_value:
        for v in list_value:
            str_len = len(v)
            upper_str = v.upper()
            print_string = f"The string has a length of {str_len} and uppercase is {upper_str}"
            print(print_string)
    else:
        print("The list is empty")




str_list = ['pam', 'jim', 'michael', 'kevin', 'Phillis', 'Stanley']

explain_strings(str_list)