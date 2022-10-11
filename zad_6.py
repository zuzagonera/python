def listsActions(list: list, list1: list) -> list:
    list3: set = []
    for element in list + list1:
        if element ** 3 not in list3:
            list3.append(element ** 3)

    return list3


print(listsActions([4, 8, 33, 90, 20, 2], [33, 66, 12, 100, 90]))