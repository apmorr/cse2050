import time
from functions import number_adder, item_returner, card_maker

def time_f(f, *args, n_trials=10):
    best_time = float("inf")
    for n in range(n_trials):
        start = time.time()
        f(*args)
        end = time.time()
        if (end - start) < best_time:
            best_time = (end - start)

    return best_time


print("=" * 50, end="\n")
print(f"{'n':8}{'t_const (ms)':16}{'t_lin (ms)':15}{'t_quad (ms)':32}")
print("-" * 50, end="\n")
for n in [1, 2, 3, 4, 5]:
    t_const = 1000*time_f(number_adder, 74837598347593875983475, 4567239456239874562397854, n_trials=n)
    t_lin = 1000*time_f(item_returner, [i for i in range(99999999)], n_trials=n)
    t_quad = 1000*time_f(card_maker, [i for i in range(9999999)], [i for i in range(3738743)], n_trials=n)
    print(f"{n:<4}\t{t_const:<10.3g}\t{t_lin:<10.3g}\t{t_quad:<10.3g}") # Specifies table whitespace size. the < indicates left-right


L = [i for i in range(1000000)]
S = {i for i in range(1000000)}
T = {i for i in range(1000000)}
def stringMaker(character, length):
    return character*length

STR = stringMaker('a', 1000000)

def find_i(storage, num):
    if num in storage:
        return True
    return False

print("=" * 50, end="\n")
print(f"{'Contains (times in ms)':>35}")
print("-" * 50, end="\n")
print(f"{'n':>0}{'t_list':>12}{'t_tup':>12}{'t_str':>12}{'t_set':>12}")
print("-" * 50, end="\n")
for n in [200, 400, 600, 800, 1000]:
    t_list = float(1000*time_f(find_i, L, -1, n_trials=n))
    t_tup = float(1000*time_f(find_i, T, -1, n_trials=n))
    t_str = float(1000*time_f(find_i, STR, "x", n_trials=n))
    t_set = float(1000*time_f(find_i, S, -1, n_trials=n))
    print(f"{n:>1}\t{t_list:>2.5g}\t{t_tup:>8.5g}\t{t_str:<15.5g}\t{t_set:>1.5g}")
