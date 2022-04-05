from multiprocessing import Pool, Manager, Lock


def worker(x, y):
    print(x + y)
    print(111)
    print(type(test_dict))
    print(222)
    print(f"test_dict: {test_dict}")
    test_dict[x] = y
    print(test_dict)


def test1():
    p = Pool()
    for i in range(4):
        p.apply_async(worker, args=(i, i))
    p.close()
    p.join()


def test():
    test1()


if __name__ == '__main__':
    manager = Manager()
    test_dict = manager.dict()
    # lock = Lock()
    test_dict['a'] = 1
    test()
    print("end")
    print(test_dict)
