n=int(input())

phoneBook = dict(input().split() for _ in range(n))

for i in range(n):
    name = input().strip()
    if name in phoneBook:
        print(name + "=" + phoneBook[name])
    else:
        print("Not found")
