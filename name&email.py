
t = input()
while t != 0:
    inp = input()
    for i in range(int(inp)):
        a = 0
        s = input()
        frequencies ={}
        for char in s:
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1

        for char in frequencies.values():
            if int(char) < int(inp) :
                print("NO")
                a = 1
                break
            elif int(char) % int(inp) != 0:
                print("NO")
                a = 1
                break
t = t - 1
