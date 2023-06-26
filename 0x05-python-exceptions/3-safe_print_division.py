#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divi = a / b
    except (TypeError, ZeroDivisionError):
        divi = None
    finally:
        f = "Inside result:"
        print("{} {}".format(f, divi))
    return (divi)
