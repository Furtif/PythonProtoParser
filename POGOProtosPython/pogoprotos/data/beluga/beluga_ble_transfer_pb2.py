# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/beluga/beluga_ble_transfer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.beluga import beluga_ble_transfer_prep_pb2 as pogoprotos_dot_data_dot_beluga_dot_beluga__ble__transfer__prep__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/beluga/beluga_ble_transfer.proto',
  package='pogoprotos.data.beluga',
  syntax='proto3',
  serialized_pb=_b('\n0pogoprotos/data/beluga/beluga_ble_transfer.proto\x12\x16pogoprotos.data.beluga\x1a\x35pogoprotos/data/beluga/beluga_ble_transfer_prep.proto\"\xa7\x01\n\x16\x42\x65lugaBleTransferProto\x12\x46\n\x0fserver_response\x18\x01 \x01(\x0b\x32-.pogoprotos.data.beluga.BelugaBleTransferPrep\x12\x18\n\x10server_signature\x18\x02 \x01(\x0c\x12\x19\n\x11localized_origins\x18\x03 \x03(\t\x12\x10\n\x08language\x18\x04 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_beluga_dot_beluga__ble__transfer__prep__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BELUGABLETRANSFERPROTO = _descriptor.Descriptor(
  name='BelugaBleTransferProto',
  full_name='pogoprotos.data.beluga.BelugaBleTransferProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_response', full_name='pogoprotos.data.beluga.BelugaBleTransferProto.server_response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_signature', full_name='pogoprotos.data.beluga.BelugaBleTransferProto.server_signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='localized_origins', full_name='pogoprotos.data.beluga.BelugaBleTransferProto.localized_origins', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language', full_name='pogoprotos.data.beluga.BelugaBleTransferProto.language', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=132,
  serialized_end=299,
)

_BELUGABLETRANSFERPROTO.fields_by_name['server_response'].message_type = pogoprotos_dot_data_dot_beluga_dot_beluga__ble__transfer__prep__pb2._BELUGABLETRANSFERPREP
DESCRIPTOR.message_types_by_name['BelugaBleTransferProto'] = _BELUGABLETRANSFERPROTO

BelugaBleTransferProto = _reflection.GeneratedProtocolMessageType('BelugaBleTransferProto', (_message.Message,), dict(
  DESCRIPTOR = _BELUGABLETRANSFERPROTO,
  __module__ = 'pogoprotos.data.beluga.beluga_ble_transfer_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.beluga.BelugaBleTransferProto)
  ))
_sym_db.RegisterMessage(BelugaBleTransferProto)


# @@protoc_insertion_point(module_scope)
