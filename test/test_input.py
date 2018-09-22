#! /usr/bin/env python3

# Usage: ./test.py <count>
#
# Input bytes are generated by incrementing a 4-byte little-endian integer,
# starting with 1. For example, an input of length 10 would be the bytes
# [1, 0, 0, 0, 2, 0, 0, 0, 3, 0]. The goal is to make is unlikely that a bug
# like swapping or duplicating a chunk could still pass the test suite.
# Hopefully it also makes it easier to eyeball the encoded outputs.

import io
import sys

COUNTER_SIZE = 4


def write_input_stream(stream, count):
    i = 1
    while count > 0:
        ibytes = i.to_bytes(COUNTER_SIZE, "little")
        take = min(COUNTER_SIZE, count)
        stream.write(ibytes[:take])
        count -= take
        i += 1


def input_bytes(count):
    b = io.BytesIO()
    write_input_stream(b, count)
    return b.getvalue()


def main():
    if len(sys.argv) < 2:
        print("The count argument is mandatory.", file=sys.stderr)
        sys.exit(1)
    count = int(sys.argv[1])
    write_input_stream(sys.stdout.buffer, count)


if __name__ == "__main__":
    main()