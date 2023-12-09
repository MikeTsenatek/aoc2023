import time
from itertools import pairwise

day = 9

def calculate_sums(data):
    sum_part1 = 0
    sum_part2 = 0

    for series in data:
        intermediate_series = []

        # Process the series until it becomes empty
        while any(series):
            new_series = [r - l for l, r in pairwise(series)]
            intermediate_series.append(series)
            series = new_series

        # Calculate the values for part 1 and part 2
        next_value_p1, next_value_p2 = 0, 0
        for inter_series in intermediate_series[::-1]:
            next_value_p1 = inter_series[-1] + next_value_p1
            next_value_p2 = inter_series[0] - next_value_p2

        # Accumulate the sums
        sum_part1 += next_value_p1
        sum_part2 += next_value_p2

    return sum_part1, sum_part2

def parse_data():
    data = []
    with open('input', 'r') as file:
        for line in file:
            data.append([int(val) for val in line.strip().split()])
    return data

if __name__ == '__main__':
    # Record start time
    start_time = time.perf_counter_ns()

    # Parse data from the input file
    data = parse_data()
    data_time = time.perf_counter_ns()

    # Calculate sums for both parts
    part1_sum, part2_sum = calculate_sums(data)
    end_time = time.perf_counter_ns()

    # Print results and elapsed times
    print(f'''=== Day {day:02} ===\n'''
          f'''  · Loading data\n'''
          f'''  · Elapsed: {(data_time - start_time) / 10 ** 6:.3f} ms\n\n'''
          f'''  · Part 1: {part1_sum}\n'''
          f'''  · Part 2: {part2_sum}\n\n'''
          f'''  · Elapsed: {(end_time - data_time) / 10 ** 6:.3f} ms\n\n'''
          f'''  · Total elapsed: {(end_time - start_time) / 10 ** 6:.3f} ms''')
