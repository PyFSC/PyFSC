from examples.fizzbuzz import fizzbuzz


def golden_fizzbuzz(n=100):
    out = ""
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            out += "FizzBuzz\n"
            continue
        elif num % 3 == 0:
            out += "Fizz\n"
            continue
        elif num % 5 == 0:
            out += "Buzz\n"
            continue
        else:
            out += f"{num}\n"
    return out


def test_fizzbuzz():
    golden = golden_fizzbuzz()
    attempt = fizzbuzz()

    line_num = 0
    for golden_line, attempt_line in zip(golden.splitlines(), attempt.splitlines()):
        line_num += 1
        assert attempt_line == golden_line, f"error on {line_num=}"