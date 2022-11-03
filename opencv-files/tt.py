a = {
    "name": "arbaz",
    "rollno": "119"
}
a["rollno"] = "68"
print(a.items())


def print_formatted(n):
    v = len(bin(n)[2:])
    for i in range(1, n+1):
        o = str(oct(i)[2:])
        h = str(hex(i)[2:])
        b = str(bin(i)[2:])
        print(str(i).center(v, " "), o.rjust(v, " "),
              h.rjust(v, " "), b.rjust(v, " "))


print_formatted(17)
