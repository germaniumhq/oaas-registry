# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: testsvc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="testsvc.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\rtestsvc.proto"\x0f\n\rProcessNameIn"\x1e\n\x0eProcessNameOut\x12\x0c\n\x04name\x18\x01 \x01(\t2B\n\x0bProcessName\x12\x33\n\x10get_process_name\x12\x0e.ProcessNameIn\x1a\x0f.ProcessNameOutb\x06proto3',
)


_PROCESSNAMEIN = _descriptor.Descriptor(
    name="ProcessNameIn",
    full_name="ProcessNameIn",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=17,
    serialized_end=32,
)


_PROCESSNAMEOUT = _descriptor.Descriptor(
    name="ProcessNameOut",
    full_name="ProcessNameOut",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="ProcessNameOut.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=34,
    serialized_end=64,
)

DESCRIPTOR.message_types_by_name["ProcessNameIn"] = _PROCESSNAMEIN
DESCRIPTOR.message_types_by_name["ProcessNameOut"] = _PROCESSNAMEOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProcessNameIn = _reflection.GeneratedProtocolMessageType(
    "ProcessNameIn",
    (_message.Message,),
    {
        "DESCRIPTOR": _PROCESSNAMEIN,
        "__module__": "testsvc_pb2"
        # @@protoc_insertion_point(class_scope:ProcessNameIn)
    },
)
_sym_db.RegisterMessage(ProcessNameIn)

ProcessNameOut = _reflection.GeneratedProtocolMessageType(
    "ProcessNameOut",
    (_message.Message,),
    {
        "DESCRIPTOR": _PROCESSNAMEOUT,
        "__module__": "testsvc_pb2"
        # @@protoc_insertion_point(class_scope:ProcessNameOut)
    },
)
_sym_db.RegisterMessage(ProcessNameOut)


_PROCESSNAME = _descriptor.ServiceDescriptor(
    name="ProcessName",
    full_name="ProcessName",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=66,
    serialized_end=132,
    methods=[
        _descriptor.MethodDescriptor(
            name="get_process_name",
            full_name="ProcessName.get_process_name",
            index=0,
            containing_service=None,
            input_type=_PROCESSNAMEIN,
            output_type=_PROCESSNAMEOUT,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_PROCESSNAME)

DESCRIPTOR.services_by_name["ProcessName"] = _PROCESSNAME

# @@protoc_insertion_point(module_scope)