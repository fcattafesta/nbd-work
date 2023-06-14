import argparse

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--nfiles", type=int, default=-1, help="Number of files")
parser.add_argument(
    "--resume", type=int, default=1, help="Resume from file number (starts from 1)"
)
parser.add_argument("--range", type=int, default=None, help="Number of events per file")
parser.add_argument("--device", type=str, default="cuda:0", help="Device to use")
parser.add_argument("--cpu", type=int, default=1, help="How many CPUs to use")
args = parser.parse_args()
