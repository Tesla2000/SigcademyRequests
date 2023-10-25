def generate_questions() -> list[str]:
    return [
        '1. Create a function named "add_numbers" that takes two arguments, "a" and "b", and returns their sum.',
        '2. Create a function named "multiply_numbers" that takes two arguments, "x" and "y", and returns their product.',
        '3. Create a function named "calculate_average" that takes a list of numbers as an argument and returns the average of those numbers.',
        '4. Create a function named "is_even" that takes an integer as an argument and returns True if it is even, otherwise False.',
        '5. Create a function named "greet_person" that takes a person\'s name as an argument and returns a greeting message like "Hello, [Name]!"',
    ]


def generate_answers(question: str, _, file: bytes) -> bool | str:
    try:
        exec(compile(file, "<string>", "exec"), globals(), locals())
        if question.startswith("1"):
            if "add_numbers" not in locals() or not callable(locals()["add_numbers"]):
                return 'The function "add_numbers" is not defined or not a function.'
            result = locals()["add_numbers"](2, 3)
            if result != 5:
                return 'The function "add_numbers" does not return the correct result.'
        elif question.startswith("2"):
            if "multiply_numbers" not in locals() or not callable(
                locals()["multiply_numbers"]
            ):
                return (
                    'The function "multiply_numbers" is not defined or not a function.'
                )
            result = locals()["multiply_numbers"](4, 5)
            if result != 20:
                return 'The function "multiply_numbers" does not return the correct result.'
        elif question.startswith("3"):
            if "calculate_average" not in locals() or not callable(
                locals()["calculate_average"]
            ):
                return (
                    'The function "calculate_average" is not defined or not a function.'
                )
            result = locals()["calculate_average"]([1, 2, 3, 4, 5])
            if result != 3.0:
                return 'The function "calculate_average" does not return the correct result.'
        elif question.startswith("4"):
            if "is_even" not in locals() or not callable(locals()["is_even"]):
                return 'The function "is_even" is not defined or not a function.'
            result = locals()["is_even"](6)
            if result is not True:
                return 'The function "is_even" does not return the correct result.'
        elif question.startswith("5"):
            if "greet_person" not in locals() or not callable(locals()["greet_person"]):
                return 'The function "greet_person" is not defined or not a function.'
            result = locals()["greet_person"]("Alice")
            if result != "Hello, Alice!":
                return 'The function "greet_person" does not return the correct result.'
        return True
    except Exception as e:
        return str(e)