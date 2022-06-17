from typing import List
import subprocess


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def get_modified_files(compare_branch: str = "") -> List[str]:
    """
    Returns a list of files that have been modified in the given branch.
    """
    compare_branch_string = f"{compare_branch}" if compare_branch else "current"
    print(
        f"Capturing modified sql files from models against {compare_branch_string} branch..."
    )
    modified_files: List[str] = (
        subprocess.Popen(
            f"git diff --name-only {compare_branch}",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        .communicate()[0]
        .decode("utf-8")
        .split("\n")
    )
    modified_files = [model for model in modified_files if model != ""]
    return modified_files


def extract_only_model_names(model_paths: List[str]) -> List[str]:
    """
    Extracts the model name from a file name.
    """
    model_names = []
    for model in model_paths:
        model_name = model.split("/")[-1].split(".")[0]
        model_names.append(model_name)
    return model_names


def get_changed_models(compare_branch: str = "") -> List[str]:
    """
    Returns a list of models that have been modified in the given branch.
    """
    modified_files: List[str] = get_modified_files(compare_branch)
    changed_models: List[str] = extract_only_model_names(modified_files)
    if modified_files:
        models_string = "\n".join(changed_models)
        print(bcolors.OKBLUE + f"Models changed: {models_string}" + bcolors.OKBLUE)
    else:
        print(bcolors.OKBLUE + f"No models changed" + bcolors.OKBLUE)
    return changed_models
