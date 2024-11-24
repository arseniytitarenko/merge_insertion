import matplotlib.pyplot as plt

def reeead(file_name, title):
    plt.figure(figsize=(15, 10))
    plt.title(title)
    plt.xlabel('Ось size')
    plt.ylabel('Ось time, microseconds')
    plt.legend()
    size_coords = []
    time_coords = []
    with open(file_name) as f:
        for line in f.readlines():
            line = line.rstrip('\n')
            size_str, time_str = line.split(';')[0], line.split(';')[1]
            size_i, time_i = int(size_str.split(' = ')[1]), float(time_str.split(' = ')[1])
            size_coords.append(size_i)
            time_coords.append(time_i)
    plt.plot(size_coords, time_coords, marker='o', markersize=3, color='red')
    plt.savefig(f'{file_name.split('.')[0]}.png')
    plt.close()


reeead(r'merge_desc.txt', 'Зависимость времени merge_sort от размера развёрнутого массива')
reeead(r'merge_nearly.txt', 'Зависимость времени merge_sort от размера почти отсортированного массива')
reeead(r'merge_random.txt', 'Зависимость времени merge_sort от размера массива со случайными значениями')
reeead(r'merge_ins_desc.txt', 'Зависимость времени merge_insertion_sort от размера развёрнутого массива')
reeead(r'merge_ins_nearly.txt', 'Зависимость времени merge_insertion_sort от размера почти отсортированного массива')
reeead(r'merge_ins_random.txt', 'Зависимость времени merge_insertion_sort от размера массива со случайными значениями')