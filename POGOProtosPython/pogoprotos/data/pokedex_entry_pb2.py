# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/pokedex_entry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import costume_pb2 as pogoprotos_dot_enums_dot_costume__pb2
from pogoprotos.enums import form_pb2 as pogoprotos_dot_enums_dot_form__pb2
from pogoprotos.enums import gender_pb2 as pogoprotos_dot_enums_dot_gender__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/pokedex_entry.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_pb=_b('\n#pogoprotos/data/pokedex_entry.proto\x12\x0fpogoprotos.data\x1a\x1epogoprotos/enums/costume.proto\x1a\x1bpogoprotos/enums/form.proto\x1a\x1dpogoprotos/enums/gender.proto\x1a!pogoprotos/enums/pokemon_id.proto\"\xba\x04\n\x0cPokedexEntry\x12/\n\npokemon_id\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x19\n\x11times_encountered\x18\x02 \x01(\x05\x12\x16\n\x0etimes_captured\x18\x03 \x01(\x05\x12\x1e\n\x16\x65volution_stone_pieces\x18\x04 \x01(\x05\x12\x18\n\x10\x65volution_stones\x18\x05 \x01(\x05\x12\x34\n\x11\x63\x61ptured_costumes\x18\x06 \x03(\x0e\x32\x19.pogoprotos.enums.Costume\x12.\n\x0e\x63\x61ptured_forms\x18\x07 \x03(\x0e\x32\x16.pogoprotos.enums.Form\x12\x32\n\x10\x63\x61ptured_genders\x18\x08 \x03(\x0e\x32\x18.pogoprotos.enums.Gender\x12\x16\n\x0e\x63\x61ptured_shiny\x18\t \x01(\x08\x12\x37\n\x14\x65ncountered_costumes\x18\n \x03(\x0e\x32\x19.pogoprotos.enums.Costume\x12\x31\n\x11\x65ncountered_forms\x18\x0b \x03(\x0e\x32\x16.pogoprotos.enums.Form\x12\x35\n\x13\x65ncountered_genders\x18\x0c \x03(\x0e\x32\x18.pogoprotos.enums.Gender\x12\x19\n\x11\x65ncountered_shiny\x18\r \x01(\x08\x12\x1c\n\x14times_lucky_received\x18\x0e \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_costume__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_form__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_gender__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POKEDEXENTRY = _descriptor.Descriptor(
  name='PokedexEntry',
  full_name='pogoprotos.data.PokedexEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.data.PokedexEntry.pokemon_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times_encountered', full_name='pogoprotos.data.PokedexEntry.times_encountered', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times_captured', full_name='pogoprotos.data.PokedexEntry.times_captured', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolution_stone_pieces', full_name='pogoprotos.data.PokedexEntry.evolution_stone_pieces', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolution_stones', full_name='pogoprotos.data.PokedexEntry.evolution_stones', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='captured_costumes', full_name='pogoprotos.data.PokedexEntry.captured_costumes', index=5,
      number=6, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='captured_forms', full_name='pogoprotos.data.PokedexEntry.captured_forms', index=6,
      number=7, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='captured_genders', full_name='pogoprotos.data.PokedexEntry.captured_genders', index=7,
      number=8, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='captured_shiny', full_name='pogoprotos.data.PokedexEntry.captured_shiny', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encountered_costumes', full_name='pogoprotos.data.PokedexEntry.encountered_costumes', index=9,
      number=10, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encountered_forms', full_name='pogoprotos.data.PokedexEntry.encountered_forms', index=10,
      number=11, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encountered_genders', full_name='pogoprotos.data.PokedexEntry.encountered_genders', index=11,
      number=12, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encountered_shiny', full_name='pogoprotos.data.PokedexEntry.encountered_shiny', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times_lucky_received', full_name='pogoprotos.data.PokedexEntry.times_lucky_received', index=13,
      number=14, type=5, cpp_type=1, label=1,
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
  serialized_start=184,
  serialized_end=754,
)

_POKEDEXENTRY.fields_by_name['pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_POKEDEXENTRY.fields_by_name['captured_costumes'].enum_type = pogoprotos_dot_enums_dot_costume__pb2._COSTUME
_POKEDEXENTRY.fields_by_name['captured_forms'].enum_type = pogoprotos_dot_enums_dot_form__pb2._FORM
_POKEDEXENTRY.fields_by_name['captured_genders'].enum_type = pogoprotos_dot_enums_dot_gender__pb2._GENDER
_POKEDEXENTRY.fields_by_name['encountered_costumes'].enum_type = pogoprotos_dot_enums_dot_costume__pb2._COSTUME
_POKEDEXENTRY.fields_by_name['encountered_forms'].enum_type = pogoprotos_dot_enums_dot_form__pb2._FORM
_POKEDEXENTRY.fields_by_name['encountered_genders'].enum_type = pogoprotos_dot_enums_dot_gender__pb2._GENDER
DESCRIPTOR.message_types_by_name['PokedexEntry'] = _POKEDEXENTRY

PokedexEntry = _reflection.GeneratedProtocolMessageType('PokedexEntry', (_message.Message,), dict(
  DESCRIPTOR = _POKEDEXENTRY,
  __module__ = 'pogoprotos.data.pokedex_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.PokedexEntry)
  ))
_sym_db.RegisterMessage(PokedexEntry)


# @@protoc_insertion_point(module_scope)
