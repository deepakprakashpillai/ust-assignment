import threading
import time

class SpaceProbe(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(5):
            time.sleep(1)
            print(f"{self.name}: Processing data packet {i+1}")

if __name__ == "__main__":
    probes = [SpaceProbe(f"Probe-{i}") for i in range(3)]
    for probe in probes:
        probe.start()
    for probe in probes:
        probe.join()
