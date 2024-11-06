def transpose(matrix: list[list[int]]) -> list[list[int]]:
    transposed = [
        [matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))
    ]
    return transposed


def format_table(
    benchmark: list[str], algos: list[str], results: list[list[float]]
) -> None:
    result = str()
    first_column_size = max(list(map(lambda x: len(x), benchmark + ["Benchmark"])))
    column_sizes = list()
    for i in range(len(algos)):
        current_column_size = max(
            len(algos[i]), max(map(lambda x: len(str(x)), transpose(results)[i]))
        )
        column_sizes.append(current_column_size)

    header = "| " + "Benchmark" + (first_column_size - 9) * " " + " | "
    for i in range(len(column_sizes) - 1):
        header += algos[i] + " " * (column_sizes[i] - len(algos[i])) + " | "
    header += algos[-1] + " " * (column_sizes[-1] - len(algos[-1])) + " |"

    sepator_indexes = [i for i in range(len(header)) if header[i] == "|"]
    separator = str()
    for i in range(len(header)):
        if i in sepator_indexes:
            separator += "|"
        else:
            separator += "-"

    result += header + "\n"
    result += separator + "\n"

    for i in range(len(benchmark)):
        row = str()
        row += (
            "| " + benchmark[i] + (first_column_size - len(benchmark[i])) * " " + " |"
        )
        for j in range(len(column_sizes)):
            current_result = str(results[i][j])
            row += (
                " "
                + current_result
                + (column_sizes[j] - len(current_result)) * " "
                + " |"
            )
        result += row
        if i != len(benchmark) - 1:
            result += "\n"

    print(result)


benchmarks = ["short", "long benchmark"]
algos = ["a", "medium length algo", "very long algorithm name"]
results = [[0.1, 0.25, 0.333], [1.0, 1.25, 1.333]]
format_table(benchmarks, algos, results)
print()

benchmarks = ["best case", "worst case"]
algos = ["quick sort", "merge sort", "bubble sort"]
results = [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]]
format_table(benchmarks, algos, results)
print()

benchmarks = ["small test", "large test"]
algos = ["a", "medium algorithm", "very long algorithm name"]
results = [[0.1, 0.25, 0.333], [1.0, 1.25, 1.333]]
format_table(benchmarks, algos, results)
