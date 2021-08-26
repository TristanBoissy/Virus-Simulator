def get_value(entry_list, string):
    for i in entry_list:
        if(i[0] == string):
            return i[1]