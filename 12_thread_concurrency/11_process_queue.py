from multiprocessing import Process, Queue

def prepare_chai(queue, type_):
    queue.put(f"{type_} Chai is ready!")


if __name__ == "__main__":
    queue = Queue()

    p1 = Process(target=prepare_chai, args=(queue, "Masala"))
    p2 = Process(target=prepare_chai, args=(queue, "Ginger"))
    p2.start()
    p2.join()
    p1.start()
    p1.join()

    print(queue.get())


# Here we are discussing how many processes can share the same resource or processes share resources