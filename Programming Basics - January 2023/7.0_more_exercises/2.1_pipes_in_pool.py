# read
V = int(input())  # volume of pool
P1 = int(input())  # pipe 1 capacity for an hour
P2 = int(input())  # pipe 2 capacity for an hour
H = float(input())  # hours that the worker is missing

# logic
pipe_1_fill = P1 * H
pipe_2_fill = P2 * H
pool_fill = pipe_1_fill + pipe_2_fill

pipe_1_fill_percent = (pipe_1_fill / pool_fill) * 100
pipe_2_fill_percent = (pipe_2_fill / pool_fill) * 100
pool_fill_percent = (pool_fill / V) * 100

if V >= pool_fill:
    print(f"The pool is {pool_fill_percent:.2f}% full."
          f" Pipe 1: {pipe_1_fill_percent:.2f}%. Pipe 2: {pipe_2_fill_percent:.2f}%.")
else:
    excess_water = pool_fill - V
    print(f"For {H} hours the pool overflows with {excess_water} liters.")
