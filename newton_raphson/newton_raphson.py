def newton_raphson(c):
    def f(x): return c[0]*x**3 + c[1]*x**2 + c[2]*x + c[3]
    def df(x): return 3*c[0]*x**2 + 2*c[1]*x + c[2]
    
    x1 = 0

    while True:
        x2 = x1 - (f(x1)/df(x1))
        if round(x2, 3) == round(x1, 3): return round(x2, 3)
        x1 = x2


print(newton_raphson([0.0, -0.1, -0.2, 0.3]))
print(newton_raphson([-0.1, 0.4, 0.1, -0.8]))
print(newton_raphson([0.2, -0.6, 1.5, -2.7]))