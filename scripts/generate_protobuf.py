import os
import argparse

def main(message_directory: str, nanopb_generator_path: str, output_dir: str):
    # gather all the .proto files in the message directory, with the full path. Do so recursively.
    proto_files = []
    for root, _, files in os.walk(message_directory):
        for file in files:
            if file.endswith(".proto"):
                proto_files.append(os.path.join(root, file))

    c_output_dir = f"{output_dir}/c"

    # remove the output directories if they exist
    os.system(f"rm -rf {c_output_dir}")

    # Make the output directories
    os.makedirs(c_output_dir, exist_ok=True)

    # generate the .c/.h files from the .proto files with nanopb
    nanopb_args = [
        *proto_files,
        "-D",
        c_output_dir,
        "",
    ]
    print(f"{nanopb_generator_path} {' '.join(nanopb_args)}")
    os.system(f"{nanopb_generator_path} {' '.join(nanopb_args)}")


if __name__ == "__main__":
    nanopb_generator_path = "../submodules/nanopb/generator/nanopb_generator.py"
    # make the nanopb generator path relative to the script
    nanopb_generator_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), nanopb_generator_path
    )
    
    # add an argument parser for the output directory
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", type=str, default="generated")
    parser.add_argument("--message_directory", type=str, default="messages")
    args = parser.parse_args()

    output_dir = args.output_dir
    message_directory = args.message_directory

    # make the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    # make the __init__.py file in the output directory
    with open(f"{output_dir}/__init__.py", "w") as f:
        f.write("")

    main(message_directory, nanopb_generator_path, output_dir=output_dir)