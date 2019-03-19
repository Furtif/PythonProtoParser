# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/item/incense_attributes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_type_pb2 as pogoprotos_dot_enums_dot_pokemon__type__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/item/incense_attributes.proto',
  package='pogoprotos.settings.master.item',
  syntax='proto3',
  serialized_pb=_b('\n8pogoprotos/settings/master/item/incense_attributes.proto\x12\x1fpogoprotos.settings.master.item\x1a#pogoprotos/enums/pokemon_type.proto\x1a!pogoprotos/enums/pokemon_id.proto\"\xa0\x04\n\x11IncenseAttributes\x12 \n\x18incense_lifetime_seconds\x18\x01 \x01(\x05\x12\x33\n\x0cpokemon_type\x18\x02 \x03(\x0e\x32\x1d.pogoprotos.enums.PokemonType\x12(\n pokemon_incense_type_probability\x18\x03 \x01(\x02\x12\x30\n(standing_time_between_encounters_seconds\x18\x04 \x01(\x05\x12-\n%moving_time_between_encounter_seconds\x18\x05 \x01(\x05\x12\x35\n-distance_required_for_shorter_interval_meters\x18\x06 \x01(\x05\x12$\n\x1cpokemon_attracted_length_sec\x18\x07 \x01(\x05\x12W\n\x0bspawn_table\x18\x08 \x03(\x0b\x32\x42.pogoprotos.settings.master.item.IncenseAttributes.IncensedPokemon\x12\x1f\n\x17spawn_table_probability\x18\t \x01(\x02\x1aR\n\x0fIncensedPokemon\x12/\n\npokemon_id\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x0e\n\x06weight\x18\x02 \x01(\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__type__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INCENSEATTRIBUTES_INCENSEDPOKEMON = _descriptor.Descriptor(
  name='IncensedPokemon',
  full_name='pogoprotos.settings.master.item.IncenseAttributes.IncensedPokemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.settings.master.item.IncenseAttributes.IncensedPokemon.pokemon_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight', full_name='pogoprotos.settings.master.item.IncenseAttributes.IncensedPokemon.weight', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_start=628,
  serialized_end=710,
)

_INCENSEATTRIBUTES = _descriptor.Descriptor(
  name='IncenseAttributes',
  full_name='pogoprotos.settings.master.item.IncenseAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incense_lifetime_seconds', full_name='pogoprotos.settings.master.item.IncenseAttributes.incense_lifetime_seconds', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_type', full_name='pogoprotos.settings.master.item.IncenseAttributes.pokemon_type', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_incense_type_probability', full_name='pogoprotos.settings.master.item.IncenseAttributes.pokemon_incense_type_probability', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='standing_time_between_encounters_seconds', full_name='pogoprotos.settings.master.item.IncenseAttributes.standing_time_between_encounters_seconds', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moving_time_between_encounter_seconds', full_name='pogoprotos.settings.master.item.IncenseAttributes.moving_time_between_encounter_seconds', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance_required_for_shorter_interval_meters', full_name='pogoprotos.settings.master.item.IncenseAttributes.distance_required_for_shorter_interval_meters', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_attracted_length_sec', full_name='pogoprotos.settings.master.item.IncenseAttributes.pokemon_attracted_length_sec', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spawn_table', full_name='pogoprotos.settings.master.item.IncenseAttributes.spawn_table', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spawn_table_probability', full_name='pogoprotos.settings.master.item.IncenseAttributes.spawn_table_probability', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_INCENSEATTRIBUTES_INCENSEDPOKEMON, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=710,
)

_INCENSEATTRIBUTES_INCENSEDPOKEMON.fields_by_name['pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_INCENSEATTRIBUTES_INCENSEDPOKEMON.containing_type = _INCENSEATTRIBUTES
_INCENSEATTRIBUTES.fields_by_name['pokemon_type'].enum_type = pogoprotos_dot_enums_dot_pokemon__type__pb2._POKEMONTYPE
_INCENSEATTRIBUTES.fields_by_name['spawn_table'].message_type = _INCENSEATTRIBUTES_INCENSEDPOKEMON
DESCRIPTOR.message_types_by_name['IncenseAttributes'] = _INCENSEATTRIBUTES

IncenseAttributes = _reflection.GeneratedProtocolMessageType('IncenseAttributes', (_message.Message,), dict(

  IncensedPokemon = _reflection.GeneratedProtocolMessageType('IncensedPokemon', (_message.Message,), dict(
    DESCRIPTOR = _INCENSEATTRIBUTES_INCENSEDPOKEMON,
    __module__ = 'pogoprotos.settings.master.item.incense_attributes_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.item.IncenseAttributes.IncensedPokemon)
    ))
  ,
  DESCRIPTOR = _INCENSEATTRIBUTES,
  __module__ = 'pogoprotos.settings.master.item.incense_attributes_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.item.IncenseAttributes)
  ))
_sym_db.RegisterMessage(IncenseAttributes)
_sym_db.RegisterMessage(IncenseAttributes.IncensedPokemon)


# @@protoc_insertion_point(module_scope)
