def bytes_to_string_dict(d):
    nd = {k.decode('utf-8'):v.decode('utf-8') for k,v in d.items()}
    return nd

def bytes_to_string_list(l):
    nl = [item.decode('utf-8') for item in l]
    return nl

def bytes_to_string_set(s):
    ns = {item.decode('utf-8') for item in s}
    return ns
