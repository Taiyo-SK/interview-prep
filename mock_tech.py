
def get_mode(input):
    """Return the mode(s) from a list of numbers."""

    results = {}
    mode = set()

    for item in input:
        # print(f"Item is {item}")
        results[item] = results.get(item, 0) + 1
        # print(f"Value is {results[item]}")

    # print(f"The results dict is: {results}")

    results_values = results.values()

    # print(f"The results_values are: {results_values}")

    max_num = max(results_values)

    results_items = results.items()

    for result in results_items:
        if result[1] == max_num:
            mode.add(result[0])

    return print(f"The mode is {mode}.")

# Test 1

test1 = [1, 2, 2, 3]

get_mode(test1)

# Test 2

test2 = [1, 1, 2, 2, 3]

get_mode(test2)