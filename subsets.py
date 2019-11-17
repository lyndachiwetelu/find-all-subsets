#Find All Subsets

def combine(item, arr):
  new_arr = []
  for x in arr:
    if len(x) > 0:
      new = [item] + x
      new_arr.append(new)
  new_arr.append([item])
  return arr + new_arr


def get_subsets(arr):
  if len(arr) == 1:
    return [[arr[0]]]
  if len(arr) == 0:
    return [[]]
  i = 0
  j = len(arr) 
  new_slice = slice(i+1, j)
  new_arr = arr[new_slice]
  return combine(arr[i], get_subsets(new_arr))

x = get_subsets(["11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]);
print(x)
