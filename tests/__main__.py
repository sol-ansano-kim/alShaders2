import argparse
parser = argparse.ArgumentParser()

parser.add_argument("filter", type=str, help="Wildcard enabled filter for test IDs.")
args = parser.parse_args()

if __name__ == '__main__':
    import tests
    tests.run_arnold_tests(args.filter)
