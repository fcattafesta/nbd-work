# the loop for generating new events starting from gen-level information in the files
import os
import subprocess
from nbd.builder.nanomaker import nanomaker


def scp(source_path, destination_path, private_key_path="~/.ssh/id_rsa"):
    scp_command = f"scp -i {private_key_path} {source_path} cattafe@cmsanalysis:{destination_path}"
    rm_command = f"rm {source_path}"
    subprocess.call(scp_command, shell=True)
    subprocess.call(rm_command, shell=True)


def nanomaker_wrapped(
    input_file,
    output_file,
    objects_keys,
    device,
    limit,
    filter_ak8,
    oversampling_factor,
    old_dir,
    new_dir,
):
    nanomaker(
        input_file,
        output_file,
        objects_keys,
        device,
        limit,
        filter_ak8,
        oversampling_factor,
    )
    # if device != "cpu":
    #     scp(output_file, output_file.replace(old_dir, new_dir))


def get_files(mc_dir, prod_camp, sample, nano, flash_dir):
    root_nano = os.path.join(mc_dir, prod_camp, sample, nano)
    # FlashSim path
    new_dir = os.path.join(flash_dir, prod_camp, sample, nano)
    # Make FlashSim directory
    if os.path.isdir(new_dir) is False:
        os.makedirs(new_dir)
    # Get list of subdirectories of FullSim dataset
    subdirs = os.listdir(root_nano)
    # Make subdirectories in FlashSim dataset
    for subdir in subdirs:
        if os.path.isdir(os.path.join(new_dir, subdir)) is False:
            os.mkdir(os.path.join(new_dir, subdir))
    # Get list of files in FullSim dataset as subdir/file.root
    files = [
        os.path.join(subdir, file)
        for subdir in subdirs
        for file in os.listdir(os.path.join(root_nano, subdir))
    ]
    # Get paths to FullSim files
    input_files = [os.path.join(root_nano, file) for file in files]
    # Get paths to FlashSim files
    output_files = [os.path.join(new_dir, file) for file in files]
    return (
        input_files,
        output_files,
    )


def mpwise_loop(input_list, output_list, nps):
    for i in range(0, len(input_list), nps):
        yield input_list[i : i + nps], output_list[i : i + nps]
