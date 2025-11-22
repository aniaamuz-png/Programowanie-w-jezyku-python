def lista(lista1,lista2):
    first_list = list(set(lista1+ lista2))
    second_list = [x**3 for x in first_list]
    return second_list

lista1 = list(range(7))
lista2 = list(range(10))

second_list = lista(lista1,lista2)
print(second_list)