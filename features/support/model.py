from typing import Dict, Optional

from features.steps.testsvc.testsvc_pb2_grpc import ProcessNameStub
from features.support.process_execution import ProcessExecution


class BaseContext:
    processes: Dict[str, ProcessExecution]
    clients: Dict[str, ProcessNameStub]

    client: ProcessNameStub
    call_result: Optional[str]
    call_error: Optional[Exception]
