import time
from datetime import datetime

def run_clock(use_24h=True):
    try:
        while True:
            fmt = "%H:%M:%S" if use_24h else "%I:%M:%S %p"
            now = datetime.now().strftime(fmt)
            print("\r" + now, end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nBye!")

if __name__ == "__main__":
    run_clock(use_24h=True)
