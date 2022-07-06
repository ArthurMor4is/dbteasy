from typing import List

from invoke import task
from dbteasy.utils import (
    get_changed_models,
    get_modified_files,
    extract_only_model_names,
    bcolors,
)

import logging

logging.getLogger().setLevel(logging.INFO)


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
    changed_models: List[str] = get_changed_models(compare_branch)
    if changed_models:
        c.run("dbt run --models {}".format(" ".join(changed_models)))


@task
def test_changed(c, compare_branch=""):
    """
    Test modified models against current branch or, optionally,
    againts another branch defined by the argument 'compare_branch'.
    """
    changed_models: List[str] = get_changed_models(compare_branch)
    c.run("dbt test --models {}".format(" ".join(changed_models)))
