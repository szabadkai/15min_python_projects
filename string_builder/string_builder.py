class StringBuilder:
    def __init__(self):
        self.buffer = []

    def __add__(self, other):
        self.buffer.append(str(other))

    def render(self):
        return "".join(self.buffer)


if __name__ == "__main__":

    import time

    test_set = list(range(1000000))
    start = time.time()

    builder = ""
    for i in test_set:
        builder += str(i)
    print(builder)
    print(time.time() - start)

    start = time.time()

    builder = StringBuilder()
    for i in test_set:
        builder + i

    print(builder.render())
    print(time.time() - start)
