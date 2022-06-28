# DBTeasy

_[Clique aqui ](README-pt-br.md) para ler esse artigo em português._
______________________________________

This project uses [Invoke (*pythonic* task runner) as a library](https://docs.pyinvoke.org/en/stable/concepts/library.html?highlight=invoke)

The main purpose of `dbteasy` is to provide an alternative CLI to work with [dbt core](https://github.com/dbt-labs/dbt-core) reducing the time needed to execute repetitive commands


![example workflow](https://github.com/ArthurMor4is/dbteasy/actions/workflows/publish-to-pypi.yml/badge.svg) [![Downloads](https://pepy.tech/badge/dbteasy)](https://pepy.tech/project/dbteasy)

## Requirements

- dbt core installed and with version history using git
  - [How to install dbt](https://docs.getdbt.com/dbt-cli/install/overview)
  - [How to install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)


## Installation

Install [`dbteasy`](https://pypi.org/project/dbteasy/) and check the version

```shell
$ pip install dbteasy
$ dbteasy --version
```

## Main commands

```shell
$ dbteasy --list # List available commands
```

```shell
$ dbteasy run-changed # Run dbt run only for newly modified models
```

```shell
$ dbteasy docs # Compile documentation and launch webserver on port 8000
```

```shell
$ dbteasy refresh # dbt clean ; dbt deps ; dbt seed
```
