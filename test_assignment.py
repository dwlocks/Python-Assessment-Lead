''' Unit tests for the assignment module. '''
import os

import pytest
from tinydb import TinyDB, Query

from assignment import WidgetTask, GadgetTask
from task_runner import TaskRunner


def test_widget(widget_parameters):
    task = WidgetTask()

    output = task.run(widget_parameters)

    assert len(output) == 1

    text = output[0].decode()

    assert text == "Peter Parker"


def test_gadget(gadget_parameters):
    task = GadgetTask()

    output = task.run(gadget_parameters)

    assert len(output) == 1

    duration = int(output[0].decode())

    assert duration == 789


def test_widget_runs_locally(local_environment):
    runner = TaskRunner()
    task = WidgetTask()
    text = None

    # Run the task as if running locally and retrieve the task output
    output = runner.run(task)
    assert len(output) == 1

    text = output[0].decode()

    assert text == "Penny Parker"


def test_widget_runs_in_batch(batch_environment):
    text = None

    # Run the task as if running in AWS Batch and retrieve the task output

    assert text == "Peter Porker"


def test_widget_runs_in_lambda(widget_lambda_event, lambda_env):
    text = None

    # Run the task as if running in a Lambda function and retrieve the task output

    assert text == "Miles Morales"


def test_gadget_runs_locally(local_environment):
    duration = None
    runner = TaskRunner()
    task = GadgetTask()

    # Run the task as if running locally and retrieve the task output
    output = runner.run(task)
    assert len(output) == 1

    duration = int(output[0].decode())

    # Run the task as if running locally and retrieve the task output

    assert duration == 300


def test_gadget_runs_in_batch(batch_environment):
    duration = None

    # Run the task as if running in AWS Batch and retrieve the task output

    assert duration == 256


def test_gadget_runs_in_lambda(gadget_lambda_event, lambda_env):
    duration = None

    # Run the task as if running in a Lambda function and retrieve the task output

    assert duration == 456


@pytest.fixture
def widget_parameters():
    return {
        "first_name": "Peter",
        "last_name": "Parker"
    }


@pytest.fixture
def gadget_parameters():
    return {
        "start_time": "987",
        "end_time": "1776"
    }


@pytest.fixture
def local_environment():
    current_environment = os.environ.copy()

    os.environ["TASK_ENV"] = 'local'
    os.environ["PARAMETER_FILE"] = 'parameters.json'

    yield os.environ

    os.environ.clear()
    os.environ.update(current_environment)


@pytest.fixture
def batch_environment():
    current_environment = os.environ.copy()

    os.environ['TASK_ENV'] = 'batch'
    os.environ["PARAMETER_DATABASE"] = 'configuration_db.json'

    yield os.environ

    os.environ.clear()
    os.environ.update(current_environment)


@pytest.fixture
def lambda_env():
    current_environment = os.environ.copy()

    # TODO: set lambda env in python-lambda-local runtime script?
    os.environ['TASK_ENV'] = 'lambda'

    yield os.environ

    os.environ.clear()
    os.environ.update(current_environment)


@pytest.fixture
def widget_lambda_event():
    return {"first_name": "Miles", "last_name": "Morales"}


@pytest.fixture
def gadget_lambda_event():
    return {"start_time": "654", "end_time": "1110"}