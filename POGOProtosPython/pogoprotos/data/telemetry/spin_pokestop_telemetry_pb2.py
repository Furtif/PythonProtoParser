# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/spin_pokestop_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.telemetry import pokestop_reward_pb2 as pogoprotos_dot_data_dot_telemetry_dot_pokestop__reward__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/spin_pokestop_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_pb=_b('\n7pogoprotos/data/telemetry/spin_pokestop_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a/pogoprotos/data/telemetry/pokestop_reward.proto\"\xa7\x01\n\x15SpinPokestopTelemetry\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x0f\n\x07\x66ort_id\x18\x02 \x01(\t\x12\x11\n\tfort_type\x18\x03 \x01(\x05\x12\x43\n\x10pokestop_rewards\x18\x04 \x03(\x0b\x32).pogoprotos.data.telemetry.PokestopReward\x12\x15\n\rtotal_rewards\x18\x05 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_telemetry_dot_pokestop__reward__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SPINPOKESTOPTELEMETRY = _descriptor.Descriptor(
  name='SpinPokestopTelemetry',
  full_name='pogoprotos.data.telemetry.SpinPokestopTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.telemetry.SpinPokestopTelemetry.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.data.telemetry.SpinPokestopTelemetry.fort_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_type', full_name='pogoprotos.data.telemetry.SpinPokestopTelemetry.fort_type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokestop_rewards', full_name='pogoprotos.data.telemetry.SpinPokestopTelemetry.pokestop_rewards', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_rewards', full_name='pogoprotos.data.telemetry.SpinPokestopTelemetry.total_rewards', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=136,
  serialized_end=303,
)

_SPINPOKESTOPTELEMETRY.fields_by_name['pokestop_rewards'].message_type = pogoprotos_dot_data_dot_telemetry_dot_pokestop__reward__pb2._POKESTOPREWARD
DESCRIPTOR.message_types_by_name['SpinPokestopTelemetry'] = _SPINPOKESTOPTELEMETRY

SpinPokestopTelemetry = _reflection.GeneratedProtocolMessageType('SpinPokestopTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _SPINPOKESTOPTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.spin_pokestop_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.SpinPokestopTelemetry)
  ))
_sym_db.RegisterMessage(SpinPokestopTelemetry)


# @@protoc_insertion_point(module_scope)