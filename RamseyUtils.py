

def get_subset(super_set, k, idx, current):
    if len(current) == k:
        x = copy.deepcopy(current)
        solution.append(x)
        return
    if idx == len(super_set):
        return
    current.append(super_set[idx])
    get_subset(super_set, k, idx + 1, current)
    current.remove(super_set[idx])
    get_subset(super_set, k, idx + 1, current)