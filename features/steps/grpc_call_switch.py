import time
import unittest
from typing import Type

import oaas
from behave import step, use_step_matcher

from features.steps.testsvc.testsvc_pb2 import ProcessNameIn, ProcessNameOut
from features.steps.testsvc.testsvc_pb2_grpc import ProcessNameStub
from features.support.model import BaseContext
from features.support.process_execution import ProcessExecution

test = unittest.TestCase()
use_step_matcher("re")

port: int = 9000


@step("I add a process named '(.*?)' for the '(.*?)' service")
@step("I add back '(.*?)' for the '(.*?)' service")
@step("I have a process '(.*?)' serving the service '(.*?)'")
def step_impl(context: BaseContext, process_name: str, service_name: str) -> None:
    global port

    process = ProcessExecution(
        command=[
            "python",
            "-m",
            "features.steps.testsvc.testsvc_main",
            str(port),
            service_name,
            process_name,
        ]
    )

    context.processes[process_name] = process

    while True:
        stdout = process.stdout

        print(stdout)
        if f"test server running on {port}" in stdout:
            break

        time.sleep(0.1)

    port += 1


def get_client(context: BaseContext, t: Type[ProcessNameStub]) -> ProcessNameStub:
    if context.client:
        return context.client

    context.client = oaas.get_client(t)

    return context.client


@step("I try to access the 'process-name' service")
def step_impl(context: BaseContext):
    client = get_client(context, ProcessNameStub)
    try:
        out: ProcessNameOut = client.get_process_name(ProcessNameIn())
        context.call_result = out.name
        context.call_error = None
    except Exception as e:
        context.call_result = None
        context.call_error = e


@step("I stop the '(.*?)' process")
def step_impl(context: BaseContext, process_name):
    context.processes[process_name].kill()


@step("I get back '(.*?)' from oaas")
@step("I still get back '(.*?)' from oaas since I have a persistent connection")
@step("I get back '(.*?)' from oaas since 'A' is dead")
def step_impl(context: BaseContext, expected):
    if context.call_error:
        raise Exception(f"Expected {expected} but the service got an error: {context.call_error}")
    test.assertEqual(expected, context.call_result)


@step("I get an exception since there is no process serving 'process-name'")
def step_impl(context: BaseContext) -> None:
    test.assertIsNotNone(context.call_error)


@step("the '(.+?)' is not registered anymore in the registry")
def step_impl(context: BaseContext, process_name: str) -> None:
    raise NotImplementedError(u'STEP: And the \'process-name\' is not registered anymore in the registry')
