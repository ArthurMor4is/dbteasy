# DBTeasy

_[Click here ](README.md) to read this article in english._
______________________________________

Esse projeto utiliza [Invoke (executor de tarefas *pythonico*) como uma biblioteca](https://docs.pyinvoke.org/en/stable/concepts/library.html?highlight=invoke)

O objetivo principal do `dbteasy` é fornecer um CLI alternativo para se trabalhar com [dbt core](https://github.com/dbt-labs/dbt-core) reduzindo o tempo necessário para executar comandos repetitivos


![example workflow](https://github.com/ArthurMor4is/dbteasy/actions/workflows/publish-to-pypi.yml/badge.svg)

## Requisitos

- dbt core instalado e com histórico de versão utilizando git
  - [Como instalar dbt](https://docs.getdbt.com/dbt-cli/install/overview)
  - [Como instalar git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)


## Instalação

Instale [`dbteasy`](https://pypi.org/project/dbteasy/) e verifique a versão:

```shell
$ pip install dbteasy
$ dbteasy --version
```

## Principais comandos

```shell
$ dbteasy --list # Lista comandos disponíveis
```

```shell
$ dbteasy run-changed # Executa dbt run somente para os modelos recém modificados
```

```shell
$ dbteasy docs # Compila documentação e inicializa webserver na porta 8000
```

```shell
$ dbteasy refresh # dbt clean ; dbt deps ; dbt seed
```
