import os
import shutil
import argparse

def main(message_directory: str, nanopb_generator_path: str, output_dir: str):
    # gather all the .proto files in the message directory, with the full path. Do so recursively.
    proto_files = []
    for root, _, files in os.walk(message_directory):
        for file in files:
            if file.endswith(".proto"):
                proto_files.append(os.path.join(root, file))
    DIR_OUTPUT_PATHS = {
        "c": f"{output_dir}/c",
        "python": f"{output_dir}/python",
    }

    for path in DIR_OUTPUT_PATHS.values():
        shutil.rmtree(path, ignore_errors=True)
        os.makedirs(path)

    # generate the .c/.h files from the .proto files with nanopb
    nanopb_args = [
        *proto_files,
        "-D",
        DIR_OUTPUT_PATHS["c"],
    ]

    protoc_args = []

    if args.generate_python:
        protoc_args.append(f"--python_out={DIR_OUTPUT_PATHS['python']}")

    if protoc_args:
        protoc_arg_str = " ".join(protoc_args)
        nanopb_args.append(f'--protoc-opt="{protoc_arg_str}"')
        

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
    parser.add_argument("--generate_python", action="store_true")
    args = parser.parse_args()

    output_dir = args.output_dir
    message_directory = args.message_directory

    # make the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    # make the __init__.py file in the output directory
    with open(f"{output_dir}/__init__.py", "w") as f:
        f.write("")

    main(message_directory, nanopb_generator_path, output_dir=output_dir)