def get_da(n,db):
    li=[]
    for el in db:
        li.append(el.split()[n])
    return li


def sort(n,db):
    li=[]
    for el in db:
        if n in el:
            li.append(el)
    return li    