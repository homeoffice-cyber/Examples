import time
import argparse


def main(pause_time):
    for i in range(1000):
        print(i)
        time.sleep(pause_time)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='simplebot')
    parser.add_argument('--pause_time', default=5, type=int,
                        help='pause time')
    clargs = parser.parse_args()
    main(pause_time=clargs.pause_time)
