def sort_ascend(list_of_strings):
    for i in range(0, len(list_of_strings)):
        
        current_min = len(list_of_strings[i])
        min_index = i

        for j in range(i, len(list_of_strings)):
            if len(list_of_strings[j]) < current_min:
                current_min = len(list_of_strings[j])
                min_index = j

        list_of_strings[i], list_of_strings[min_index] = list_of_strings[min_index], list_of_strings[i]
    
    return list_of_strings


def sort_descend(list_of_strings):
    for i in range(0, len(list_of_strings)):
        
        current_max = len(list_of_strings[i])
        max_index = i

        for j in range(i, len(list_of_strings)):
            if len(list_of_strings[j]) > current_max:
                current_max = len(list_of_strings[j])
                max_index = j

        list_of_strings[i], list_of_strings[max_index] = list_of_strings[max_index], list_of_strings[i]
    
    return list_of_strings


strings = [
    "assdsdasad",
    "asdsad",
    "sdsadasdasdassa",
    "ass"
]

print(sort_ascend(strings))
print(sort_descend(strings))