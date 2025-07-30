import sys
from flake8.main.cli import main as flake8_main

def run_flake8():
    sys.argv = ["flake8", "my_library"]
    flake8_main()

def main():
    run_flake8()

if __name__ == "__main__":
    main()
