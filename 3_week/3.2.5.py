def update_dictionary(d, key, value):
    if key in d: #если лючи есть в словаре: словарю с этим ключом добавляем методом append.(значение)
        d[key].append(value) #проверяет,соответвует ли текущий ключ ключу, и добавляет значение (ключ1 = ключ1)
    elif 2*key in d: #или если перемноженный ключ если в словаре:[перемноженному ключу], добавляем +=[значение]
        d[2 * key] += [value] #проверяет,ключ зависит от ключа созданного ранее и добавляет значение (ключ2 = ключ2)
    else: #в остальных случаях у нас [перемноженный ключ] равен [значении]
        d[2 * key] = [value] # добавляет первый словарь с ключем, умножает ключ1 и добавляет значение -1, пример print(update_dictionary(d, 1, -1))
