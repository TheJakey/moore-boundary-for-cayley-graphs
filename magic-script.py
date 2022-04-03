import cmath


def calculate_quadratic_equation(a, b, c):
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)

    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)

    print('Quadratic equation solutions are {0} and {1}'.format(sol1, sol2))

    return sol1, sol2


def main():
    while True:
        n = input("Insert number of vertices: ")
        d = calculate_quadratic_equation(1, 2, 2 - (2 * int(n)))[1].real

        # find the closest existing valid number of vertices `n` for given depth `d`

        # generate Z collection from `n` vertices

        # verify if Z collection represents Cayley graph with depth of `d`

        print(d)


if __name__ == "__main__":
    main()
