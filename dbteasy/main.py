from invoke import Collection, Program
from dbteasy import tasks

program = Program(namespace=Collection.from_module(tasks), version="0.2.3")
