def set_unique_sequence(data):
    unique_sequence = []
    for number in data:
        if number not in unique_sequence:
            unique_sequence.append(number)
        else:
            continue
    return unique_sequence

print(set_unique_sequence([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]))