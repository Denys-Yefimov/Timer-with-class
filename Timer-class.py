import time


class Timer:

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        diff_time = end - self.start
        print(f"cod completed in {round(diff_time, 4)}")

with Timer():
    for i in range(100009):
        print(i)
