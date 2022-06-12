from invoke import task
import subprocess
import logging

logging.getLogger().setLevel(logging.INFO)


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


@task
def clean(c):
    """
    Equivalent to dbt clean.
    """
    print(bcolors.OKGREEN + "Removing temporary files ..." + bcolors.ENDC)
    c.run("dbt clean")


@task
def deps(c):
    """
    Equivalent to dbt deps.
    """
    print(
        bcolors.OKGREEN
        + "Pulling the most recent version of the dependencies ..."
        + bcolors.ENDC
    )
    c.run("dbt deps")


@task
def seed(c):
    """
    Equivalent to dbt seed.
    """
    print(
        bcolors.OKGREEN
        + "Loading csv files located in the seed-paths directory ..."
        + bcolors.ENDC
    )
    c.run("dbt seed")


@task(clean, deps, seed)
def refresh(c):
    """
    Equivalent to dbt clean ; dbt deps ; dbt seed.
    """
    pass


@task(deps)
def docs(c):
    """
    Equivalent to dbt docs generate ; dbt docs serve.
    """
    print(
        bcolors.OKGREEN
        + "Generating your project's documentation website ..."
        + bcolors.ENDC
    )
    c.run("dbt docs generate")
    print(
        bcolors.OKGREEN
        + "Starting a webserver on port 8000 to serve your documentation locally ..."
        + bcolors.ENDC
    )
    c.run("dbt docs serve")


@task
def run_changed(c, compare_branch=""):
    """
    Capture modified sql files from models using git diff (n_models) against current branch or, 
    optionally, againts another branch defined by the argument 'compare_branch'.

    It runs `dbt run --models (n_models)`.
    """
    if compare_branch == "":
        print(f"Capturing modified sql files from models against current branch...")
    else:
        print(f"Capturing modified sql files from models against {compare_branch} branch...")
    models_diff_result = (
        subprocess.Popen(
            f"git diff --name-only {compare_branch}| grep '\.sql'$",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        .communicate()[0]
        .decode("utf-8")
    )
    models_diff_list = models_diff_result.split("\n")
    models_diff_list = [model for model in models_diff_list if model != ""]
    if len(models_diff_list) > 0:
        result_model_list = []
        for model in models_diff_list:
            model_name = model.split("/")[-1].split(".")[0]
            result_model_list.append(model_name)
        result_models = " ".join(result_model_list)
        print(bcolors.OKBLUE + f"Models changed: {result_models}" + bcolors.OKBLUE)
        c.run("dbt run --models {}".format(result_models))
    else:
        print(bcolors.OKBLUE + f"No models changed" + bcolors.OKBLUE)
