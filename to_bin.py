def to_binary(n):
    output = ""
    while n > 0:
        if n % 2 == 0:
            output = "0" + output
        else:
            output = "1" + output
        n = n // 2
    return output

print(to_binary(84))
print(to_binary(19))
print(to_binary(99))
