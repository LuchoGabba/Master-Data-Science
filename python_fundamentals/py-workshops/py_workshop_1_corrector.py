from typing import List, Callable

# Test cases
tests = [(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"],
                                                                        ["WEST"]),
        (["NORTH", "WEST", "SOUTH", "EAST"],
                                            ["NORTH", "WEST", "SOUTH", "EAST"]),
        (["NORTH", "SOUTH", "EAST", "WEST"],
                                            []),
        (["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"],
                                                            ["WEST", "WEST"])
        ]


# Test runner function
# Test runner function
def run_tests(dirReduc: Callable[[List[str]], List[str]]) -> None:
    """Run a suite of tests on the dirReduc function.
    
    Args:
    dirReduc: A callable that takes a list of strings representing directions
              and returns a list of strings with the directions reduced.

    Raises:
    AssertionError: If any of the test cases fail, indicating that the dirReduc
                    function does not perform as expected.

    Returns:
    None: The function has no return value; it prints the result of the test cases.
    """
    for i, (input_plan, expected_output) in enumerate(tests):
        assert dirReduc(input_plan) == expected_output, f"Test case {i+1} failed: {dirReduc(input_plan)} != {expected_output}"
    print("All tests passed!")

# This allows the script to be imported without immediately running the test
if __name__ == "__main__":
    run_tests()

    
