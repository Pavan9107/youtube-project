s = "Hello world"

v= set("aeiouAEIOU")
l = list(s)

left = 0
right = len(l)-1

while left < right:
    if l[left] not in v:
        left+=1
    elif l[right] not in v:
        right-=1
    else:
        l[left], l[right] = l[right], l[left]
        left+=1
        right-=1

print(" ".join(l))

