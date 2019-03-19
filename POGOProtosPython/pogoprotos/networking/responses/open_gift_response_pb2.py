# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/open_gift_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import loot_pb2 as pogoprotos_dot_inventory_dot_loot__pb2
from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.data.friends import friendship_level_data_pb2 as pogoprotos_dot_data_dot_friends_dot_friendship__level__data__pb2
from pogoprotos.data.player import player_public_profile_pb2 as pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/open_gift_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n8pogoprotos/networking/responses/open_gift_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x1fpogoprotos/inventory/loot.proto\x1a\"pogoprotos/data/pokemon_data.proto\x1a\x33pogoprotos/data/friends/friendship_level_data.proto\x1a\x32pogoprotos/data/player/player_public_profile.proto\"\xb0\x04\n\x10OpenGiftResponse\x12H\n\x06result\x18\x01 \x01(\x0e\x32\x38.pogoprotos.networking.responses.OpenGiftResponse.Result\x12)\n\x05items\x18\x02 \x01(\x0b\x32\x1a.pogoprotos.inventory.Loot\x12\x31\n\x0b\x65gg_pokemon\x18\x03 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12M\n\x17updated_friendship_data\x18\x04 \x01(\x0b\x32,.pogoprotos.data.friends.FriendshipLevelData\x12\x43\n\x0e\x66riend_profile\x18\x05 \x01(\x0b\x32+.pogoprotos.data.player.PlayerPublicProfile\"\xdf\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x19\n\x15\x45RROR_PLAYER_BAG_FULL\x10\x03\x12\x1e\n\x1a\x45RROR_PLAYER_LIMIT_REACHED\x10\x04\x12\x1d\n\x19\x45RROR_GIFT_DOES_NOT_EXIST\x10\x05\x12\x1a\n\x16\x45RROR_FRIEND_NOT_FOUND\x10\x06\x12\x1b\n\x17\x45RROR_INVALID_PLAYER_ID\x10\x07\x12\x17\n\x13\x45RROR_FRIEND_UPDATE\x10\x08\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_loot__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_friends_dot_friendship__level__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_OPENGIFTRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.OpenGiftResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_BAG_FULL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_LIMIT_REACHED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_GIFT_DOES_NOT_EXIST', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FRIEND_NOT_FOUND', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_PLAYER_ID', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FRIEND_UPDATE', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=605,
  serialized_end=828,
)
_sym_db.RegisterEnumDescriptor(_OPENGIFTRESPONSE_RESULT)


_OPENGIFTRESPONSE = _descriptor.Descriptor(
  name='OpenGiftResponse',
  full_name='pogoprotos.networking.responses.OpenGiftResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.OpenGiftResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='pogoprotos.networking.responses.OpenGiftResponse.items', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_pokemon', full_name='pogoprotos.networking.responses.OpenGiftResponse.egg_pokemon', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated_friendship_data', full_name='pogoprotos.networking.responses.OpenGiftResponse.updated_friendship_data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend_profile', full_name='pogoprotos.networking.responses.OpenGiftResponse.friend_profile', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OPENGIFTRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=268,
  serialized_end=828,
)

_OPENGIFTRESPONSE.fields_by_name['result'].enum_type = _OPENGIFTRESPONSE_RESULT
_OPENGIFTRESPONSE.fields_by_name['items'].message_type = pogoprotos_dot_inventory_dot_loot__pb2._LOOT
_OPENGIFTRESPONSE.fields_by_name['egg_pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_OPENGIFTRESPONSE.fields_by_name['updated_friendship_data'].message_type = pogoprotos_dot_data_dot_friends_dot_friendship__level__data__pb2._FRIENDSHIPLEVELDATA
_OPENGIFTRESPONSE.fields_by_name['friend_profile'].message_type = pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2._PLAYERPUBLICPROFILE
_OPENGIFTRESPONSE_RESULT.containing_type = _OPENGIFTRESPONSE
DESCRIPTOR.message_types_by_name['OpenGiftResponse'] = _OPENGIFTRESPONSE

OpenGiftResponse = _reflection.GeneratedProtocolMessageType('OpenGiftResponse', (_message.Message,), dict(
  DESCRIPTOR = _OPENGIFTRESPONSE,
  __module__ = 'pogoprotos.networking.responses.open_gift_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.OpenGiftResponse)
  ))
_sym_db.RegisterMessage(OpenGiftResponse)


# @@protoc_insertion_point(module_scope)
