#!/usr/bin/python3
"""Create script"""

def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    lines_read = 0

    try:
        for line in sys.stdin:
            lines_read += 1
            parts = line.split()

            if len(parts) > 0:
                try:
                    file_size += int(parts[-1])
                    status_code = int(parts[-2])
                    if status_code in status_codes:
                        status_codes[status_code] += 1
                except (IndexError, ValueError):
                    pass

            if lines_read % 10 == 0:
                print("File size: {:d}".format(file_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print("{:d}: {:d}".format(code, status_codes[code]))

    except KeyboardInterrupt:
        print("File size: {:d}".format(file_size))
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print("{:d}: {:d}".format(code, status_codes[code]))
