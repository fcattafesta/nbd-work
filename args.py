import argparse

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=str, help="Input file")
parser.add_argument("--limit", type=int, default=None, help="Number of events per file")
parser.add_argument("--device", type=str, default="cuda:0", help="Device to use")
parser.add_argument("--filter_ak8", action="store_true", help="Filter AK8 jets")
parser.add_argument(
    "--oversampling_factor", type=int, default=1, help="Oversampling factor"
)
parser.add_argument(
    "--old_dir",
    type=str,
    default="/gpfs/ddn/srm/cms//store/mc/",
    help="Old directory",
)
parser.add_argument(
    "--new_dir",
    type=str,
    default="/gpfs/ddn/cms/user/cattafe/FlashSim/",
    help="New directory",
)
parser.add_argument(
    "--obj_list",
    default=["Electron", "Electron_fromJets", "Muon", "Jet"],
    help="List of objects",
)
# parser.add_argument("--nfiles", type=int, default=-1, help="Number of files")
# parser.add_argument(
#     "--resume", type=int, default=1, help="Resume from file number (starts from 1)"
# )
# parser.add_argument("--cpu", type=int, default=1, help="How many CPUs to use")
args = parser.parse_args()
