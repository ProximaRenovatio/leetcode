from solutions.math_geometry.medium._1352_product_of_numbers import ProductOfNumbers


def test_product_of_numbers():
    operations = [
        "ProductOfNumbers", "add", "add", "add", "add", "add",
        "getProduct", "getProduct", "getProduct", "add", "getProduct"
    ]

    arguments = [
        [], [3], [0], [2], [5], [4],
        [2], [3], [4], [8], [2]
    ]

    expected = [
        None, None, None, None, None, None,
        20, 40, 0, None, 32
    ]

    solution = None

    for operation, args, result in zip(operations, arguments, expected):
        if operation == "ProductOfNumbers":
            solution = ProductOfNumbers()
        elif operation == "add":
            solution.add(args[0])
        elif operation == "getProduct":
            assert solution.getProduct(args[0]) == result