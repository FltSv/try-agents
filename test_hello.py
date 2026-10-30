"""Verify that running hello.py prints the expected greeting."""

import subprocess
import sys
import unittest
from pathlib import Path

HELLO_SCRIPT_PATH = Path(__file__).resolve().parent / "hello.py"
EXPECTED_STDOUT = "Hello, world!\n"


class HelloScriptTest(unittest.TestCase):
    def test_running_script_prints_hello_world(self) -> None:
        completed_process = subprocess.run(
            [sys.executable, str(HELLO_SCRIPT_PATH)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed_process.returncode, 0)
        self.assertEqual(completed_process.stdout, EXPECTED_STDOUT)
        self.assertEqual(completed_process.stderr, "")


if __name__ == "__main__":
    unittest.main()
