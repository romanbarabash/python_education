list_n = [1, 2, 3]
dict_n = {}


def dictfromkey(list_v, value=None):
    dict_n = {}
    for v in list_v:
        if value:
            dict_n.setdefault(v, value)
        dict_n.setdefault(v, None)
    return dict_n


print(dictfromkey(list_n, ["blah", "blalala"]))
