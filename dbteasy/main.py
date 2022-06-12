from invoke import Collection, Program
from dbteasy import tasks
from constants import VERSION

program = Program(namespace=Collection.from_module(tasks), version=VERSION)
