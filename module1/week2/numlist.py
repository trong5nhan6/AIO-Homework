def find_max_with_k(list, k):
    lenght = len(list)
    result = []
    for i in range(lenght - k + 1):
        k_num_list = []
        for j in range(i, i+k):
            k_num_list.append(list[j])
        result.append(max(k_num_list))
    return result


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(find_max_with_k(num_list, k))
