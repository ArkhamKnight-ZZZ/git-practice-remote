"""Temperature conversion helpers."""


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def print_conversion_table(start: int, stop: int, step: int = 5) -> None:
    if start > stop:
        raise ValueError("start must not exceed stop")
    print("Celsius | Fahrenheit")
    for celsius in range(start, stop + 1, step):
        temp_f = celsius_to_fahrenheit(celsius)
        print(f"{celsius:>7} | {temp_f:>10.1f}")


if __name__ == "__main__":
    print_conversion_table(0, 30, 10)
