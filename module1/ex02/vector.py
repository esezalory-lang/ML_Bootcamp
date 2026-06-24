from typing import Any


class Vector():
    range_types = (int, tuple)
    is_column = False

    def __init__(self: "Vector", values: Any):
        self.values = []
        self.col_len = 0
        self.row_len = 0
        if isinstance(values, self.range_types):
            self.init_range(values)
            self.is_column = True
        else:
            if len(values) == 1:
                self.is_column = False
                for i in values[0]:
                    if not isinstance(i, float):
                        raise Exception("ERROR: List does not contain floats")
                    self.row_len += 1
                self.values.append(values[0])
            else:
                self.is_column = True
                for i in values:
                    if not isinstance(i[0], float):
                        raise Exception("ERROR: List does not contain floats")
                    self.col_len += 1
                    self.values.append(i)
        if self.is_column is True:
            self.shape = tuple((self.col_len, 1))
        else:
            self.shape = tuple((1, self.row_len))

    def init_range(self: "Vector", range_values: int | tuple) -> None:
        if isinstance(range_values, int):
            for i in range(range_values):
                self.values.append([float(i)])
                self.col_len += 1
        else:
            if range_values[0] > range_values[1]:
                raise Exception("ERROR: Range 1 is greater than Range 2")
            for i in range(range_values[0], range_values[1]):
                self.values.append([float(i)])
                self.col_len += 1

    def dot(self: "Vector", vector2: "Vector") -> float:
        ttl_sum = 0
        if not all(a == b for a, b in zip(self.shape, vector2.shape)):
            raise Exception("ERROR: Shapes of vectors are different")
        if self.is_column is True:
            ttl_sum = sum(self.values[i][0] *
                          vector2.values[i][0] for i in range(self.col_len))
        else:
            ttl_sum = sum(self.values[0][i] *
                          vector2.values[0][i] for i in range(self.row_len))
        return ttl_sum

    def T(self: "Vector") -> "Vector":
        if self.is_column is True:
            new_vector = Vector([[self.values[i][0] for i in range(
                self.col_len)]])
        else:
            new_vector = Vector([[self.values[0][i]] for i in range(
                self.row_len)])
        return new_vector

    def __str__(self: "Vector") -> str:
        return f"Vector({self.values})"
    
    def __repr__(self: "Vector") -> str:
        return f"{self.values}"

    def __mul__(self: "Vector", factor: int | float) -> "Vector":
        if not isinstance(factor, (int, float)):
            raise NotImplementedError("ERROR: Wrong type for multiplication")
        if self.is_column is True:
            prod_vector = Vector([[self.values[i][0] * factor] for i in range(
                self.col_len)])
        else:
            prod_vector = Vector([[self.values[0][i] * factor for i in range(
                self.row_len)]])
        return prod_vector

    def __rmul__(self: "Vector", factor: int | float) -> "Vector":
        if not isinstance(factor, (int, float)):
            raise NotImplementedError("ERROR: Wrong type for rmultiplication")
        if self.is_column is True:
            prod_vector = Vector([[factor * self.values[i][0]] for i in range(
                self.col_len)])
        else:
            prod_vector = Vector([[factor * self.values[0][i] for i in range(
                self.row_len)]])
        return prod_vector

    def __truediv__(self: "Vector", divisor: int | float):
        if not isinstance(divisor, (int, float)):
            raise NotImplementedError("ERROR: Wrong type for division")
        if divisor == 0:
            raise ZeroDivisionError("ERROR: Division by zero")
        if self.is_column is True:
            rem_vector = Vector([[self.values[i][0] / divisor] for i in range(
                self.col_len)])
        else:
            rem_vector = Vector([[self.values[0][i] / divisor for i in range(
                self.row_len)]])
        return rem_vector

    def __rtruediv__(self: "Vector", divisor: int | float):
        raise NotImplementedError(
            "Division of a scalar by a Vector is not defined here.")

    def __add__(self: "Vector", addend: Any) -> "Vector":
        if not isinstance(addend, Vector):
            raise NotImplementedError(
                "ERROR: Addition w/ scalar not supported")
        if not all(a == b for a, b in zip(self.shape, addend.shape)):
            raise Exception("ERROR: Shapes of vectors are different")
        if self.is_column is True:
            sum_vector = Vector([[self.values[i][0] + addend.values[i][0]]
                                for i in range(
                self.col_len)])
        else:
            sum_vector = Vector([[self.values[0][i] + addend.values[0][i]
                                for i in range(self.row_len)]])
        return sum_vector

    def __sub__(self: "Vector", addend: Any) -> "Vector":
        if not isinstance(addend, Vector):
            raise NotImplementedError(
                "ERROR: Addition w/ scalar not supported")
        if not all(a == b for a, b in zip(self.shape, addend.shape)):
            raise Exception("ERROR: Shapes of vectors are different")
        if self.is_column is True:
            sum_vector = Vector([[self.values[i][0] - addend.values[i][0]]
                                for i in range(
                self.col_len)])
        else:
            sum_vector = Vector([[self.values[0][i] - addend.values[0][i]
                                for i in range(self.row_len)]])
        return sum_vector
