# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/ex_raid_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import friendship_level_milestone_pb2 as pogoprotos_dot_enums_dot_friendship__level__milestone__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/ex_raid_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_pb=_b('\n1pogoprotos/settings/master/ex_raid_settings.proto\x12\x1apogoprotos.settings.master\x1a\x31pogoprotos/enums/friendship_level_milestone.proto\"a\n\x0e\x45xRaidSettings\x12O\n\x1bminimum_ex_raid_share_level\x18\x01 \x01(\x0e\x32*.pogoprotos.enums.FriendshipLevelMilestoneb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_friendship__level__milestone__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EXRAIDSETTINGS = _descriptor.Descriptor(
  name='ExRaidSettings',
  full_name='pogoprotos.settings.master.ExRaidSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minimum_ex_raid_share_level', full_name='pogoprotos.settings.master.ExRaidSettings.minimum_ex_raid_share_level', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=132,
  serialized_end=229,
)

_EXRAIDSETTINGS.fields_by_name['minimum_ex_raid_share_level'].enum_type = pogoprotos_dot_enums_dot_friendship__level__milestone__pb2._FRIENDSHIPLEVELMILESTONE
DESCRIPTOR.message_types_by_name['ExRaidSettings'] = _EXRAIDSETTINGS

ExRaidSettings = _reflection.GeneratedProtocolMessageType('ExRaidSettings', (_message.Message,), dict(
  DESCRIPTOR = _EXRAIDSETTINGS,
  __module__ = 'pogoprotos.settings.master.ex_raid_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.ExRaidSettings)
  ))
_sym_db.RegisterMessage(ExRaidSettings)


# @@protoc_insertion_point(module_scope)
