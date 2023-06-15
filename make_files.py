import os
import multiprocessing as mp
import psutil
from utils import nanomaker_wrapped, get_files, mpwise_loop


def make_files(
    obj_list, args, custom_path="/scratchnvme/cattafe/FlashSim", **dir_kwargs
):
    # Get input and output files
    input_files, output_files = get_files(**dir_kwargs)
    if args.nfiles > 0:
        input_files = input_files[(args.resume - 1) : (args.resume - 1 + args.nfiles)]
        output_files = output_files[(args.resume - 1) : (args.resume - 1 + args.nfiles)]
    else:
        input_files = input_files[(args.resume - 1) :]
        output_files = output_files[(args.resume - 1) :]
    print(f"Found {len(input_files)} input files")
    # Make pool of processes
    # Make files
    for input_list, output_list in mpwise_loop(input_files, output_files, args.cpu):
        pool = mp.Pool(processes=args.cpu)
        print(f"Making {len(input_list)} files")
        for input_file, output_file in zip(input_list, output_list):
            pool.apply_async(
                nanomaker_wrapped,
                args=(
                    input_file,
                    output_file,
                    obj_list,
                    args.device,
                    args.range,
                    args.filter_ak8,
                    args.oversampling_factor,
                    dir_kwargs["flash_dir"],
                    custom_path,
                ),
            )
        pool.close()
        pool.join()
        # Memory usage in GB
        print(
            f"Memory usage: {(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2):.0f} MB"
        )
        print("Done!")
