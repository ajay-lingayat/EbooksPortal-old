import random

def pick3( sections ):
    
    new_sections = list()

    for section in sections:
        lst = list()
        if len(section[1]) > 3:
           books = section[1][:3]
           lst.append(section[0])
           lst.append(books)
        else:
           lst.append(section)
        new_sections.append(lst)

    return new_sections