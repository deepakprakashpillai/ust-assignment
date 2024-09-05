import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def satellite_task(name, duration):
    print(f"{name} started...")
    time.sleep(duration)
    print(f"{name} completed after {duration} seconds")

# Worker function for task processing
def worker(task_queue):
    while not task_queue.empty():
        task = task_queue.get()
        satellite_task(*task)
        task_queue.task_done()

if __name__ == "__main__":
    task_queue = queue.Queue()

    tasks = [("Task1", 3), ("Task2", 2), ("Task3", 1)]

    for task in tasks:
        task_queue.put(task)

    num_threads = 3
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for _ in range(num_threads):
            executor.submit(worker, task_queue)

    task_queue.join()

    print("All tasks completed!")
