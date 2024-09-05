#def trigger_type_error():
#    return '1' + 1  
#
#trigger_type_error()

#def trigger_value_error():
#    return int('abc')  
#
#trigger_value_error()

#def trigger_index_error():
#    lst = [1, 2, 3]
#    return lst[5]  
#
#trigger_index_error()

def trigger_key_error():
    dct = {'a': 1}
    return dct['b']  

trigger_key_error()

