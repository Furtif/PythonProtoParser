# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/gym_badge_gmt_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/gym_badge_gmt_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_pb=_b('\n7pogoprotos/settings/master/gym_badge_gmt_settings.proto\x12\x1apogoprotos.settings.master\"\xf9\x01\n\x13GymBadgeGmtSettings\x12\x0e\n\x06target\x18\x01 \x03(\x05\x12,\n$battle_winning_score_per_defender_cp\x18\x02 \x01(\x02\x12&\n\x1egym_defending_score_per_minute\x18\x03 \x01(\x02\x12\x1b\n\x13\x62\x65rry_feeding_score\x18\x04 \x01(\x05\x12\x1c\n\x14pokemon_deploy_score\x18\x05 \x01(\x05\x12!\n\x19raid_battle_winning_score\x18\x06 \x01(\x05\x12\x1e\n\x16lose_all_battles_score\x18\x07 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GYMBADGEGMTSETTINGS = _descriptor.Descriptor(
  name='GymBadgeGmtSettings',
  full_name='pogoprotos.settings.master.GymBadgeGmtSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='pogoprotos.settings.master.GymBadgeGmtSettings.target', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_winning_score_per_defender_cp', full_name='pogoprotos.settings.master.GymBadgeGmtSettings.battle_winning_score_per_defender_cp', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gym_defending_score_per_minute', full_name='pogoprotos.settings.master.GymBadgeGmtSettings.gym_defending_score_per_minute', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='berry_feeding_score', full_name='pogoprotos.settings.master.GymBadgeGmtSettings.berry_feeding_score', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_deploy_score', full_name='pogoprotos.settings.master.GymBadgeGmtSettings.pokemon_deploy_score', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_battle_winning_score', full_name='pogoprotos.settings.master.GymBadgeGmtSettings.raid_battle_winning_score', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lose_all_battles_score', full_name='pogoprotos.settings.master.GymBadgeGmtSettings.lose_all_battles_score', index=6,
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
  serialized_start=88,
  serialized_end=337,
)

DESCRIPTOR.message_types_by_name['GymBadgeGmtSettings'] = _GYMBADGEGMTSETTINGS

GymBadgeGmtSettings = _reflection.GeneratedProtocolMessageType('GymBadgeGmtSettings', (_message.Message,), dict(
  DESCRIPTOR = _GYMBADGEGMTSETTINGS,
  __module__ = 'pogoprotos.settings.master.gym_badge_gmt_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.GymBadgeGmtSettings)
  ))
_sym_db.RegisterMessage(GymBadgeGmtSettings)


# @@protoc_insertion_point(module_scope)
