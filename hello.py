"""Print a greeting when run as a script."""

import argparse

DEFAULT_GREETING_NAME = "world"


def main() -> None:
    argument_parser = argparse.ArgumentParser(description="Print a greeting.")
    argument_parser.add_argument(
        "--name",
        default=DEFAULT_GREETING_NAME,
        help="Name to greet. Defaults to world.",
    )
    parsed_arguments = argument_parser.parse_args()
    print(f"Hello, {parsed_arguments.name}!")


if __name__ == "__main__":
    main()
