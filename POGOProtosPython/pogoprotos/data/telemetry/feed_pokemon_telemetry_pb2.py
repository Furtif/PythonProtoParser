# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/feed_pokemon_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.telemetry import pokemon_telemetry_pb2 as pogoprotos_dot_data_dot_telemetry_dot_pokemon__telemetry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/feed_pokemon_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_pb=_b('\n6pogoprotos/data/telemetry/feed_pokemon_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a\x31pogoprotos/data/telemetry/pokemon_telemetry.proto\"\xbe\x01\n\x14\x46\x65\x65\x64PokemonTelemetry\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12<\n\x07pokemon\x18\x02 \x01(\x0b\x32+.pogoprotos.data.telemetry.PokemonTelemetry\x12\x0e\n\x06gym_id\x18\x03 \x01(\t\x12\x0c\n\x04team\x18\x04 \x01(\x05\x12\x16\n\x0e\x64\x65\x66\x65nder_count\x18\x05 \x01(\x05\x12\x12\n\nmotivation\x18\x06 \x01(\x05\x12\x0e\n\x06\x63p_now\x18\x07 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_telemetry_dot_pokemon__telemetry__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FEEDPOKEMONTELEMETRY = _descriptor.Descriptor(
  name='FeedPokemonTelemetry',
  full_name='pogoprotos.data.telemetry.FeedPokemonTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.data.telemetry.FeedPokemonTelemetry.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='pogoprotos.data.telemetry.FeedPokemonTelemetry.pokemon', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gym_id', full_name='pogoprotos.data.telemetry.FeedPokemonTelemetry.gym_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team', full_name='pogoprotos.data.telemetry.FeedPokemonTelemetry.team', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defender_count', full_name='pogoprotos.data.telemetry.FeedPokemonTelemetry.defender_count', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='motivation', full_name='pogoprotos.data.telemetry.FeedPokemonTelemetry.motivation', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cp_now', full_name='pogoprotos.data.telemetry.FeedPokemonTelemetry.cp_now', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=137,
  serialized_end=327,
)

_FEEDPOKEMONTELEMETRY.fields_by_name['pokemon'].message_type = pogoprotos_dot_data_dot_telemetry_dot_pokemon__telemetry__pb2._POKEMONTELEMETRY
DESCRIPTOR.message_types_by_name['FeedPokemonTelemetry'] = _FEEDPOKEMONTELEMETRY

FeedPokemonTelemetry = _reflection.GeneratedProtocolMessageType('FeedPokemonTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _FEEDPOKEMONTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.feed_pokemon_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.FeedPokemonTelemetry)
  ))
_sym_db.RegisterMessage(FeedPokemonTelemetry)


# @@protoc_insertion_point(module_scope)
