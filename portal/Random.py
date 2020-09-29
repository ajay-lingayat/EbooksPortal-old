import random

def pick3( sections ):
    
    new_sections = list()

    for section in sections:
        lst = list()
        if len(section[1]) > 3:
           item = section[1][:3]
           lst.append(section[0])
           lst.append(item)
        else:
           new_sections.append(section)
        if lst:
           new_sections.append(lst)

    return new_sections