import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            all_data.append(line)
    return all_data


if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    duration = time.time() - start_time
    print(duration)

    # Многопроцессный
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    duration2 = time.time() - start_time
    print(duration2)