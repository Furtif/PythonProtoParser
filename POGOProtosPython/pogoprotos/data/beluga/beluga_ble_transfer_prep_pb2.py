# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/beluga/beluga_ble_transfer_prep.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.beluga import beluga_pokemon_pb2 as pogoprotos_dot_data_dot_beluga_dot_beluga__pokemon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/beluga/beluga_ble_transfer_prep.proto',
  package='pogoprotos.data.beluga',
  syntax='proto3',
  serialized_pb=_b('\n5pogoprotos/data/beluga/beluga_ble_transfer_prep.proto\x12\x16pogoprotos.data.beluga\x1a+pogoprotos/data/beluga/beluga_pokemon.proto\"\xa8\x01\n\x15\x42\x65lugaBleTransferPrep\x12;\n\x0cpokemon_list\x18\x01 \x03(\x0b\x32%.pogoprotos.data.beluga.BelugaPokemon\x12\x18\n\x10\x65ligble_for_item\x18\x02 \x01(\x08\x12\x16\n\x0etransaction_id\x18\x03 \x01(\x03\x12\x11\n\tbeluga_id\x18\x04 \x01(\t\x12\r\n\x05nonce\x18\x05 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_beluga_dot_beluga__pokemon__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BELUGABLETRANSFERPREP = _descriptor.Descriptor(
  name='BelugaBleTransferPrep',
  full_name='pogoprotos.data.beluga.BelugaBleTransferPrep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_list', full_name='pogoprotos.data.beluga.BelugaBleTransferPrep.pokemon_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eligble_for_item', full_name='pogoprotos.data.beluga.BelugaBleTransferPrep.eligble_for_item', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='pogoprotos.data.beluga.BelugaBleTransferPrep.transaction_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beluga_id', full_name='pogoprotos.data.beluga.BelugaBleTransferPrep.beluga_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='pogoprotos.data.beluga.BelugaBleTransferPrep.nonce', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=127,
  serialized_end=295,
)

_BELUGABLETRANSFERPREP.fields_by_name['pokemon_list'].message_type = pogoprotos_dot_data_dot_beluga_dot_beluga__pokemon__pb2._BELUGAPOKEMON
DESCRIPTOR.message_types_by_name['BelugaBleTransferPrep'] = _BELUGABLETRANSFERPREP

BelugaBleTransferPrep = _reflection.GeneratedProtocolMessageType('BelugaBleTransferPrep', (_message.Message,), dict(
  DESCRIPTOR = _BELUGABLETRANSFERPREP,
  __module__ = 'pogoprotos.data.beluga.beluga_ble_transfer_prep_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.beluga.BelugaBleTransferPrep)
  ))
_sym_db.RegisterMessage(BelugaBleTransferPrep)


# @@protoc_insertion_point(module_scope)
