# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/friends/player_friend_display.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_display_pb2 as pogoprotos_dot_data_dot_pokemon__display__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/friends/player_friend_display.proto',
  package='pogoprotos.data.friends',
  syntax='proto3',
  serialized_pb=_b('\n3pogoprotos/data/friends/player_friend_display.proto\x12\x17pogoprotos.data.friends\x1a%pogoprotos/data/pokemon_display.proto\"\xb1\x02\n\x13PlayerFriendDisplay\x12.\n\x05\x62uddy\x18\x01 \x01(\x0b\x32\x1f.pogoprotos.data.PokemonDisplay\x12 \n\x18\x62uddy_display_pokemon_id\x18\x02 \x01(\x05\x12\x1e\n\x16\x62uddy_pokemon_nickname\x18\x03 \x01(\t\x12<\n\x13last_pokemon_caught\x18\x04 \x01(\x0b\x32\x1f.pogoprotos.data.PokemonDisplay\x12&\n\x1elast_pokemon_caught_display_id\x18\x05 \x01(\x05\x12%\n\x1dlast_pokemon_caught_timestamp\x18\x06 \x01(\x03\x12\x1b\n\x13\x62uddy_candy_awarded\x18\x07 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__display__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PLAYERFRIENDDISPLAY = _descriptor.Descriptor(
  name='PlayerFriendDisplay',
  full_name='pogoprotos.data.friends.PlayerFriendDisplay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buddy', full_name='pogoprotos.data.friends.PlayerFriendDisplay.buddy', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buddy_display_pokemon_id', full_name='pogoprotos.data.friends.PlayerFriendDisplay.buddy_display_pokemon_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buddy_pokemon_nickname', full_name='pogoprotos.data.friends.PlayerFriendDisplay.buddy_pokemon_nickname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_pokemon_caught', full_name='pogoprotos.data.friends.PlayerFriendDisplay.last_pokemon_caught', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_pokemon_caught_display_id', full_name='pogoprotos.data.friends.PlayerFriendDisplay.last_pokemon_caught_display_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_pokemon_caught_timestamp', full_name='pogoprotos.data.friends.PlayerFriendDisplay.last_pokemon_caught_timestamp', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buddy_candy_awarded', full_name='pogoprotos.data.friends.PlayerFriendDisplay.buddy_candy_awarded', index=6,
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
  serialized_start=120,
  serialized_end=425,
)

_PLAYERFRIENDDISPLAY.fields_by_name['buddy'].message_type = pogoprotos_dot_data_dot_pokemon__display__pb2._POKEMONDISPLAY
_PLAYERFRIENDDISPLAY.fields_by_name['last_pokemon_caught'].message_type = pogoprotos_dot_data_dot_pokemon__display__pb2._POKEMONDISPLAY
DESCRIPTOR.message_types_by_name['PlayerFriendDisplay'] = _PLAYERFRIENDDISPLAY

PlayerFriendDisplay = _reflection.GeneratedProtocolMessageType('PlayerFriendDisplay', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERFRIENDDISPLAY,
  __module__ = 'pogoprotos.data.friends.player_friend_display_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.friends.PlayerFriendDisplay)
  ))
_sym_db.RegisterMessage(PlayerFriendDisplay)


# @@protoc_insertion_point(module_scope)
