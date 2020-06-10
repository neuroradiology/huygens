#!/usr/bin/env python3

from bruhat.render.sat import Variable, Solver, System


def main():
    x = Variable('x')
    y = Variable('y')
    z = Variable('z')

    items = [
        x+y >= 1.,
        x+z == 5,
        y >= 3.
    ]

    solver = Solver(items)

    result = solver.solve()
    print(result)

    system = System()
    v = system.get_var()
    u = system.get_var()
    w = system.get_var()
    system.add(v+u+w == 3.)
    system.solve()
    print(system[v] + system[u] + system[w])


if __name__ == "__main__":

    main()
    


