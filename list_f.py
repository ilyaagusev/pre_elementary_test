def flat_function(list_of_lists):
    flat_list = []
    for unit in list_of_lists:
        for item in unit:
            flat_list.append(item)
    return flat_list
