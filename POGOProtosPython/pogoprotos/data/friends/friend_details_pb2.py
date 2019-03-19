# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/friends/friend_details.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.player import player_summary_pb2 as pogoprotos_dot_data_dot_player_dot_player__summary__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/friends/friend_details.proto',
  package='pogoprotos.data.friends',
  syntax='proto3',
  serialized_pb=_b('\n,pogoprotos/data/friends/friend_details.proto\x12\x17pogoprotos.data.friends\x1a+pogoprotos/data/player/player_summary.proto\"\x88\x01\n\rFriendDetails\x12\x35\n\x06player\x18\x01 \x01(\x0b\x32%.pogoprotos.data.player.PlayerSummary\x12\x1b\n\x13\x66riend_visible_data\x18\x02 \x01(\x0c\x12\r\n\x05score\x18\x03 \x01(\x05\x12\x14\n\x0c\x64\x61ta_with_me\x18\x04 \x01(\x0c\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_player__summary__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FRIENDDETAILS = _descriptor.Descriptor(
  name='FriendDetails',
  full_name='pogoprotos.data.friends.FriendDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player', full_name='pogoprotos.data.friends.FriendDetails.player', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend_visible_data', full_name='pogoprotos.data.friends.FriendDetails.friend_visible_data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='pogoprotos.data.friends.FriendDetails.score', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_with_me', full_name='pogoprotos.data.friends.FriendDetails.data_with_me', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=119,
  serialized_end=255,
)

_FRIENDDETAILS.fields_by_name['player'].message_type = pogoprotos_dot_data_dot_player_dot_player__summary__pb2._PLAYERSUMMARY
DESCRIPTOR.message_types_by_name['FriendDetails'] = _FRIENDDETAILS

FriendDetails = _reflection.GeneratedProtocolMessageType('FriendDetails', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDDETAILS,
  __module__ = 'pogoprotos.data.friends.friend_details_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.friends.FriendDetails)
  ))
_sym_db.RegisterMessage(FriendDetails)


# @@protoc_insertion_point(module_scope)
