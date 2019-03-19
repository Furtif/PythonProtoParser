# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/rpc_socket_response_time.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/rpc_socket_response_time.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_pb=_b('\n8pogoprotos/data/telemetry/rpc_socket_response_time.proto\x12\x19pogoprotos.data.telemetry\"\x90\x01\n\x15RpcSocketResponseTime\x12\x12\n\nrequest_id\x18\x01 \x01(\x04\x12\x10\n\x08probe_id\x18\x02 \x01(\t\x12\x15\n\rresponse_time\x18\x03 \x01(\x02\x12\x14\n\x0cside_channel\x18\x04 \x01(\x08\x12\x0e\n\x06\x61\x64_hoc\x18\x05 \x01(\x08\x12\x14\n\x0c\x61\x64_hoc_delay\x18\x06 \x01(\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RPCSOCKETRESPONSETIME = _descriptor.Descriptor(
  name='RpcSocketResponseTime',
  full_name='pogoprotos.data.telemetry.RpcSocketResponseTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='pogoprotos.data.telemetry.RpcSocketResponseTime.request_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='probe_id', full_name='pogoprotos.data.telemetry.RpcSocketResponseTime.probe_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response_time', full_name='pogoprotos.data.telemetry.RpcSocketResponseTime.response_time', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='side_channel', full_name='pogoprotos.data.telemetry.RpcSocketResponseTime.side_channel', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ad_hoc', full_name='pogoprotos.data.telemetry.RpcSocketResponseTime.ad_hoc', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ad_hoc_delay', full_name='pogoprotos.data.telemetry.RpcSocketResponseTime.ad_hoc_delay', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=232,
)

DESCRIPTOR.message_types_by_name['RpcSocketResponseTime'] = _RPCSOCKETRESPONSETIME

RpcSocketResponseTime = _reflection.GeneratedProtocolMessageType('RpcSocketResponseTime', (_message.Message,), dict(
  DESCRIPTOR = _RPCSOCKETRESPONSETIME,
  __module__ = 'pogoprotos.data.telemetry.rpc_socket_response_time_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.RpcSocketResponseTime)
  ))
_sym_db.RegisterMessage(RpcSocketResponseTime)


# @@protoc_insertion_point(module_scope)
