# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class Ping(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    text: typing___Text = ...
    def __init__(
        self,
        *,
        text: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["text", b"text"]
    ) -> None: ...

type___Ping = Ping

class Pong(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    text: typing___Text = ...
    len: builtin___int = ...
    def __init__(
        self,
        *,
        text: typing___Optional[typing___Text] = None,
        len: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["len", b"len", "text", b"text"]
    ) -> None: ...

type___Pong = Pong
