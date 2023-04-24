def sort_by_length(arr):
    if arr is None:
        return None
    else:
        return list(sorted(arr, key=len))
        #return sorted(arr, key=len)

print(sort_by_length(["", "moderately", "brains", "pizza"]))
