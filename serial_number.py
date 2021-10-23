import random
import string

_serial_numbers = dict()


def generate_serial_number():
    global _serial_numbers
    for _ in range(100):
        key = "".join(random.choices(string.ascii_uppercase, k=4))
        value = "".join(random.choices(string.ascii_uppercase, k=4))
        if key in _serial_numbers:
            continue

        _serial_numbers[key] = key + value
        return key + value
    raise RuntimeError("Can't generate new keys")


def save(path):
    global _serial_numbers
    with open(path, "w") as file:
        for serial_number in _serial_numbers.values():
            file.write(serial_number)
            file.write("\n")


def load(path):
    global _serial_numbers
    with open(path, "r") as file:
        for line in file.readlines():
            key = line[:4]
            value = line[4:]
            _serial_numbers[key] = key + value


def format(serial_number: str):
    return f"{serial_number[:4]}-{serial_number[4:]}"


# if __name__ == "__main__":
#     for _ in range(100):
#         print(format(generate_serial_number()))
#     save("/media/ramdisk/test_serial_numbers.txt")
