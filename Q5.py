def f():
    x=42
    def g():
            global x
    x=43
    print("before calling g:",x)
    g()
    print("after calling g:",x)
f()
