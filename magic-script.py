import subsetsum

import cmath
import itertools


def calculate_quadratic_equation(a, b, c):
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)

    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)

    print('Quadratic equation solutions are {0} and {1}'.format(sol1, sol2))

    return sol1, sol2


degree_max_n_table = {
    3: 10,
    4: 15,
    5: 24,
    6: 32,
    7: 50
}


def find_closest_n(given_n):
    for k in degree_max_n_table.keys():
        if given_n < degree_max_n_table[k]:
            if k == 3:
                return k
            else:
                return k - 1


def generate_inverse_elements(n, num_of_elements):
    inverse_elements = []

    for i in range(1, num_of_elements):
        inverse_elements.append([i, n - i])

    print("Inverse elements: ", inverse_elements)
    return inverse_elements


def get_self_inverse_element(all_inverse_elements):
    for element in all_inverse_elements:
        if element[0] == element[1]:
            return element[0]

    return None


def remove_self_inverse_element(all_inverse_elements):
    self_inverse_element = get_self_inverse_element(all_inverse_elements)
    if (self_inverse_element):
        copy = all_inverse_elements.copy()
        copy.remove([self_inverse_element, self_inverse_element])
        return copy

    return all_inverse_elements


def generate_z_collections(n, d, num_of_elements):
    all_inverse_elements = generate_inverse_elements(n, num_of_elements)

    all_possible_combinations = []
    for subset in itertools.combinations(remove_self_inverse_element(all_inverse_elements), int(d / 2)):
        all_possible_combinations.append(list(itertools.chain.from_iterable(subset)))

    # transfer combinations into z_collections
    self_inverse = get_self_inverse_element(all_inverse_elements)
    if (d % 2 == 1 and self_inverse):
        for subset in all_possible_combinations:
            subset.append(all_inverse_elements[len(all_inverse_elements) - 1][0])

    elif (d % 2 == 1 and not self_inverse):
        print(f"ERROR: Unable to construct Z_Collection with provided d {d} and n {n} values")
        return []

    print("Z_Collections: ", all_possible_combinations)
    return all_possible_combinations


def all_subsets(arr, n, res, elements_used_counts):
    if (n == 0):
        # print(res)
        elements_used_counts.append(res)
        return

    for i in range(len(arr)):
        if (n >= arr[i]):
            all_subsets(arr, n - arr[i], (res + 1), elements_used_counts)


def get_all_solutions(arr, target, n):
    print(f"getting all solutions for {arr} with target {target}")

    elements_used_counts = []
    all_subsets(arr, target, 0, elements_used_counts)
    all_subsets(arr, target + n - 1, 0, elements_used_counts)

    print("result: ", elements_used_counts)

    return elements_used_counts



def verify_diameter(n, z_collection):
    max_diameter = 0
    for target in range(1, n):

        has_solution = subsetsum.has_solution(z_collection, target)
        min_diameter = 999 # len(z_collection)
        min_subset = []

        # solutions = subsetsum.get_all_solutions(z_collection, target)
        solutions = get_all_solutions(z_collection, target, n)

        # if not (any(solutions)):
        #     print("WARN: Unable to construct required subset for target: ", target)
        #     return False

        diamater_two = 0
        for solution_elem_count in solutions:
            if solution_elem_count <= 2:
                diamater_two += 1

        if diamater_two == 0:
            return False


        # for solution in solutions:
        #     # `solution` contains indices of elements in `z_collection`
        #     subset = [z_collection[i] for i in solution]
        #     if (min_diameter > len(subset)):
        #         min_diameter = len(subset)
        #         min_subset = subset
        #
        #         if (min_diameter > 2):
        #             print("WARN: Diameter larger than 2")
        #             return False
        #
        #     if (max_diameter < min_diameter):
        #         max_diameter = min_diameter
        #
        #     print(f"Min diameter for {target} is {min_diameter} through {min_subset}")

    # print(f"Max diam {max_diameter}")
    # return max_diameter
    return True


def main():
    n = int(input("Insert number of vertices: "))
    num_of_elements = int(n / 2) + 1

    d = calculate_quadratic_equation(1, 2, 2 - (2 * int(n)))[1].real
    print(F"Calculated d is: {d}")
    d = int(d)
    d = d+1
    # # find the closest existing valid number of vertices `n` for given depth `d`
    # n = find_closest_n(n)

    # generate Z collection from `n` vertices
    z_collections = generate_z_collections(n, d, num_of_elements)

    # verify if Z collection represents Cayley graph with depth of `d`
    for z_collection in z_collections:
        if (verify_diameter(n, z_collection)):
            print("SUCCESS!")
            print("Used z_collection: ", z_collection)
            return

    print("No result found :(")


if __name__ == "__main__":
    while True:
        main()
