from random import uniform

def simulate(n: int) -> None:
    """
    Simulates n trials of a Gaussian distribution simulation
    For each iteration, 12 random numbers between [0,1] are generated, summed, and then subtracted by 6
    Writes data to a file
    :param n: Number of iterations
    :return: None
    """
    f = open('data.txt', 'w')
    lines = []
    for _ in range(n):
        lines.append(str(sum([uniform(0, 1) for i in range(12)]) - 6)+'\n')
    f.writelines(lines)
    f.close()

if __name__ == '__main__':
    simulate(10**6)

