# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/pokemon_anim.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/pokemon_anim.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n#pogoprotos/enums/pokemon_anim.proto\x12\x10pogoprotos.enums*\x94\x01\n\x0bPokemonAnim\x12\x15\n\x11NONE_POKEMON_ANIM\x10\x00\x12\x0b\n\x07IDLE_01\x10\x01\x12\x0b\n\x07IDLE_02\x10\x02\x12\x08\n\x04LAND\x10\x03\x12\r\n\tATTACK_01\x10\x04\x12\r\n\tATTACK_02\x10\x05\x12\x0b\n\x07\x44\x41MAGED\x10\x06\x12\x0b\n\x07STUNNED\x10\x07\x12\x08\n\x04LOOP\x10\x08\x12\x08\n\x04_MAX\x10\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_POKEMONANIM = _descriptor.EnumDescriptor(
  name='PokemonAnim',
  full_name='pogoprotos.enums.PokemonAnim',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_POKEMON_ANIM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IDLE_01', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IDLE_02', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAND', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTACK_01', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTACK_02', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DAMAGED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STUNNED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOOP', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='_MAX', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=58,
  serialized_end=206,
)
_sym_db.RegisterEnumDescriptor(_POKEMONANIM)

PokemonAnim = enum_type_wrapper.EnumTypeWrapper(_POKEMONANIM)
NONE_POKEMON_ANIM = 0
IDLE_01 = 1
IDLE_02 = 2
LAND = 3
ATTACK_01 = 4
ATTACK_02 = 5
DAMAGED = 6
STUNNED = 7
LOOP = 8
_MAX = 9


DESCRIPTOR.enum_types_by_name['PokemonAnim'] = _POKEMONANIM


# @@protoc_insertion_point(module_scope)
