def check_lista(lista,n):
    return n in lista
my_list = list(range(180))
check = check_lista(my_list,181)
print(check)