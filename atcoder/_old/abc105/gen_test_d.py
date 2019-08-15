from d import count_lr_old
import random
import pickle


def generate_test_case(size, number_size):
    test_cases = []
    for _ in range(size):
        n = random.randint(1, number_size)
        m = random.randint(2, number_size)
        a = [random.randint(1, number_size) for _ in range(10**4)]

        count = count_lr_old(n, m, a)

        test_cases.append(((n, m), a, count))

    with open('test_case_d.pickle', mode='wb') as f:
        pickle.dump(test_cases, f)


if __name__ == "__main__":
    generate_test_case(3, 10**3)
