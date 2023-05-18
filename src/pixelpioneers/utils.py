from pathlib import Path


def get_output_paths(input_paths: list, output_dir: str, action: str):
    output_paths = []
    for input_path in input_paths:
        input_path = Path(input_path)
        output_paths.append(Path(output_dir).joinpath(str(input_path.stem) + f"_{action}" + input_path.suffix))

    return output_paths
