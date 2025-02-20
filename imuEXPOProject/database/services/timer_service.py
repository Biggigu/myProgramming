import time
import threading

class TimerService:
    def __init__(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0

    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            print("Timer started.")

    def stop_timer(self):
        if self.running:
            self.elapsed_time = int(time.time() - self.start_time)
            self.running = False
            print(f"Timer stopped. Elapsed time: {self.elapsed_time} seconds")
            return self.elapsed_time
        return None

    def reset_timer(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        print("Timer reset.")

    def get_elapsed_time(self):
        if self.running:
            return int(time.time() - self.start_time)
        return self.elapsed_time

# Example Usage
# timer = TimerService()
# timer.start_timer()
# time.sleep(5)
# elapsed = timer.stop_timer()
# print(f"Recorded time: {elapsed} seconds")
