try:
    x=10
    x.append(5)
    print(x)
except AttributeError as e:
    print("can't append element in a variables:")
    print(e)