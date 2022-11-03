def fact(v):
    if v == 1:
        return 1
    return v * fact(v-1)

print(fact(4))        