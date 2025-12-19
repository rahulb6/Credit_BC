"""Example CLI entrypoint.

This is optional. Most users will run notebooks first.
"""

from src.config import PATHS

def main():
    print("Repo template ready.")
    print("Raw data path:", PATHS.raw)

if __name__ == "__main__":
    main()
