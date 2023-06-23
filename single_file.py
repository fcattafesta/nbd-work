import os
import psutil
import time
import ROOT
from nbd.builder.nanomaker import nanomaker
from utils import scp
from args import args


def nanomaker_wrapped(input_file):
    output_file = input_file.replace(args.old_dir, args.new_dir)
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    start = time.time()
    nanomaker(
        input_file,
        output_file,
        args.obj_list,
        args.device,
        args.limit,
        args.filter_ak8,
        args.oversampling_factor,
    )
    end = time.time()
    print(f"Time elapsed: {((end - start) / 60.0):.0f} min")
    destination = os.path.dirname(output_file).replace(
        args.new_dir, "/scratchnvme/cattafe/FlashSim/"
    )
    scp(output_file, destination)
    process = psutil.Process(os.getpid())
    print(f"Memory usage: {process.memory_info().rss / 1024 / 1024:.0f} MB")


if __name__ == "__main__":
    nanomaker_wrapped(args.input_file)
