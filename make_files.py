import os
import multiprocessing as mp
import psutil
from utils import nanomaker_wrapped, get_files, mpwise_loop, scp


def log_exception(exception, output_file):
    print(f"Task raised exception: {exception} in {output_file}\n")


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

    pool = mp.get_context("spawn").Pool(processes=args.cpu)
    for input_list, output_list in mpwise_loop(input_files, output_files, args.cpu):
        print(f"Making {len(input_list)} files")
        results = []
        for input_file, output_file in zip(input_list, output_list):
            result = pool.apply_async(
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
            results.append((result, output_file))

        for result, file in results:
            try:
                result.get(timeout=3600)  # adjust timeout as needed
            except Exception as e:
                log_exception(e, file)

        print("Copying files to FlashSim directory")
        for input_file, output_file in zip(input_list, output_list):
            try:
                scp(
                    output_file,
                    output_file.replace(custom_path, dir_kwargs["flash_dir"]),
                )
            except:
                raise Exception(f"Failed to copy {output_file}")
        print("Done!")

        # Memory usage in GB
        print(
            f"Memory usage: {(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2):.0f} MB"
        )
        print("Done!")
    pool.close()
    pool.join()
