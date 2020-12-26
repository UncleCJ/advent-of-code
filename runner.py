import math
import pretty_errors
import pyperclip
import time


# Taken from repl.it AOC python template
# https://repl.it/@Scoder12/aoc-python-template
def format_runtime(ms):
    # Microseconds
    if ms <= 1:
        return f"{round(ms * 1000)}µs"
    # Milliseconds
    if ms < 1000:
        whole_ms = math.floor(ms)
        rem_ms = ms - whole_ms
        return f"{whole_ms}ms " + format_runtime(rem_ms)
    sec = ms / 1000
    # Seconds
    if sec < 60:
        whole_sec = math.floor(sec)
        rem_ms = ms - whole_sec * 1000
        return f'{whole_sec}s ' + format_runtime(rem_ms)
    # Minutes (hopefully it doesn't get to this point lol)
    return f"{math.floor(sec / 60)}m " + format_runtime((sec % 60) * 1000)


def run(part_one_func, part_two_func, file):
    with open((file.rstrip("code.py") + "input.txt"), 'r') as input_file:
        data = input_file.read()
        total_time = 0
        copied_part = 0
        for part, func in enumerate((part_one_func, part_two_func)):
            print(f"Running part {part + 1}...")
            start = time.perf_counter()
            val = func(data)
            end = time.perf_counter()
            if val is not None:
                pyperclip.copy(val)
                copied_part = part + 1
            print(f"\tOutput: {val}")
            rtime = (end - start) * 1000  # sec -> ms
            total_time += rtime
            print(f"\tTook {format_runtime(rtime)}")
        print(f"Took {format_runtime(total_time)}")
        if copied_part > 0:
            print(f"Copied part {copied_part}")