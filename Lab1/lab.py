from random import randint

def simulate_single_die(n: int) -> dict:
    """
    Simulates rolling a single die n times
    :param n: The number of times to roll
    :return: The face value and amount of times rolled as key-value pairs
    """
    times = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for _ in range(n):
        roll = randint(1, 6)
        times[roll] += 1
    return times

def simulate_two_dice(n: int) -> dict:
    """
    Simulates rolling two dice n times
    :param n: The number of times to roll
    :return: The sum of the dice and the amount of times rolled as key-value pairs
    """
    total = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for _ in range(n):
        roll = randint(1, 6) + randint(1, 6)
        total[roll] += 1
    return total

if __name__ == '__main__':
    print('Single Die: n=1000')
    print(simulate_single_die(1000))
    print('Single Die: n=10,000')
    print(simulate_single_die(10_000))
    print('Single Die: n=100,000')
    print(simulate_single_die(100_000))
    print('Two Dice: n=1000')
    print(simulate_two_dice(1000))
    print('Two Dice: n=10,000')
    print(simulate_two_dice(10_000))
    print('Two Dice: n=100,000')
    print(simulate_two_dice(100_000))

