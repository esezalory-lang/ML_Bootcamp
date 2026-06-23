from typing import Any
# import pandas as pd


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

    def print(self: "Vector") -> None:
        print(self.values)
        print(self.shape)

    def dot(self: "Vector", vector2: "Vector") -> float:
        sum = 0
        if not all(a == b for a, b in zip(self.shape, vector2.shape)):
            raise Exception("ERROR: Shapes of vectors are different")
        if self.is_column is True:
            for i in range(self.col_len):
                sum += self.values[i][0] * vector2.values[i][0]
        else:
            for i in range(self.row_len):
                sum += self.values[0][i] * vector2.values[0][i]
        return sum

    def T(self: "Vector") -> "Vector":
        pass
