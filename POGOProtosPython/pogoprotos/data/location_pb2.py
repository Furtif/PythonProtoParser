# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/location.proto

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
  name='pogoprotos/data/location.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_pb=_b('\n\x1epogoprotos/data/location.proto\x12\x0fpogoprotos.data\"2\n\x08Location\x12\x12\n\nlat_degree\x18\x01 \x01(\x01\x12\x12\n\nlng_degree\x18\x02 \x01(\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='pogoprotos.data.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat_degree', full_name='pogoprotos.data.Location.lat_degree', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lng_degree', full_name='pogoprotos.data.Location.lng_degree', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=51,
  serialized_end=101,
)

DESCRIPTOR.message_types_by_name['Location'] = _LOCATION

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'pogoprotos.data.location_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.Location)
  ))
_sym_db.RegisterMessage(Location)


# @@protoc_insertion_point(module_scope)
