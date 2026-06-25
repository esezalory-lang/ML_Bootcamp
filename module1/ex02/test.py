from vector import Vector

if __name__ == "__main__":
    # # Column vector of shape n * 1
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = v1 * 5
    print(v2)
    print("Expected output: Vector([[0.0], [5.0], [10.0], [15.0]])\n")

    v1 = Vector((0, 3))
    v2 = v1 * 5
    print(v2)
    print("Expected output: Vector([[0.0], [5.0], [10.0], [15.0]])\n")

    # Row vector of shape 1 * n
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = v1 * 5
    print(v2)
    print("Expected output: Vector([[0.0, 5.0, 10.0, 15.0]])\n")

    v2 = v1 / 2.0
    print(v2)
    print("Expected output: Vector([[0.0, 0.5, 1.0, 1.5]])\n")

    # v2 = v1 / 0.0
    # print(v2)
    # print("Expected ouput: ZeroDivisionError: division by zero.\n")

    # v2 = 2.0 / v1
    # print(v2)
    # print("Expected output: NotImplementedError:",
    #       "Division of a scalar by a Vector is not defined here.\n")

    print("Column vector of shape (n, 1):")
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
    print("Expected output: (4,1)\n")

    print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
    print("Expected output: [[0.0], [1.0], [2.0], [3.0]]\n")

    print("Row vector of shape (1, n):")
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
    print("Expected output: (1,4)\n")

    print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
    print("Expected output: [[0.0, 1.0, 2.0, 3.0]]\n")

    print(".T() Example 1:")
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v1.shape)
    print("Expected output: (4,1)\n")

    print(v1.T())
    print("Expected output: Vector([[0.0, 1.0, 2.0, 3.0]])\n")

    print(v1.T().shape)
    print("Expected output: (1,4)\n")

    print(".T() Example 2:")
    v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v2.shape)
    print("Expected output: (1,4)\n")

    print(v2.T())
    print("Expected output: Vector([[0.0], [1.0], [2.0], [3.0]])\n")

    print(v2.T().shape)
    print("Expected output: (4,1)\n")

    print(".dot() Example 1:")
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    print(v1.dot(v2))
    print("Expected output: 18.0\n")

    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    print(v3.dot(v4))
    print("Expected output: 14.0\n")

    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    v5 = v3 + v4
    print(v5)
    print("Expected output: Vector([[3.0, 7.0]])\n")

    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    v5 = v3 - v4
    print(v5)
    print("Expected output: Vector([[-1.0, -1.0]])\n")
