# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/echo_message.proto

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
  name='pogoprotos/networking/requests/messages/echo_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\n:pogoprotos/networking/requests/messages/echo_message.proto\x12\'pogoprotos.networking.requests.messages\"\r\n\x0b\x45\x63hoMessageb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ECHOMESSAGE = _descriptor.Descriptor(
  name='EchoMessage',
  full_name='pogoprotos.networking.requests.messages.EchoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=103,
  serialized_end=116,
)

DESCRIPTOR.message_types_by_name['EchoMessage'] = _ECHOMESSAGE

EchoMessage = _reflection.GeneratedProtocolMessageType('EchoMessage', (_message.Message,), dict(
  DESCRIPTOR = _ECHOMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.echo_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.EchoMessage)
  ))
_sym_db.RegisterMessage(EchoMessage)


# @@protoc_insertion_point(module_scope)
