def twoSum(lst, target):
    seen = set()
    
    for val in lst:
        cmp = target - val
        if cmp in seen:
            return True
        seen.add(val)
        
    return False


lst = list(map(int, input("enrer num space sep: ").split()))
target = int(input("Enter target: "))

# ---- Output ----
if twoSum(lst, target):
    print("Pair exists")
else:
    print("No pair found")