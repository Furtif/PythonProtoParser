# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/update_fitness_metrics_response.proto

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
  name='pogoprotos/networking/responses/update_fitness_metrics_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nEpogoprotos/networking/responses/update_fitness_metrics_response.proto\x12\x1fpogoprotos.networking.responses\"\xa9\x01\n\x1cUpdateFitnessMetricsResponse\x12T\n\x06status\x18\x01 \x01(\x0e\x32\x44.pogoprotos.networking.responses.UpdateFitnessMetricsResponse.Status\"3\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_UPDATEFITNESSMETRICSRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.UpdateFitnessMetricsResponse.Status',
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
  ],
  containing_type=None,
  options=None,
  serialized_start=225,
  serialized_end=276,
)
_sym_db.RegisterEnumDescriptor(_UPDATEFITNESSMETRICSRESPONSE_STATUS)


_UPDATEFITNESSMETRICSRESPONSE = _descriptor.Descriptor(
  name='UpdateFitnessMetricsResponse',
  full_name='pogoprotos.networking.responses.UpdateFitnessMetricsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.UpdateFitnessMetricsResponse.status', index=0,
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
    _UPDATEFITNESSMETRICSRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=276,
)

_UPDATEFITNESSMETRICSRESPONSE.fields_by_name['status'].enum_type = _UPDATEFITNESSMETRICSRESPONSE_STATUS
_UPDATEFITNESSMETRICSRESPONSE_STATUS.containing_type = _UPDATEFITNESSMETRICSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateFitnessMetricsResponse'] = _UPDATEFITNESSMETRICSRESPONSE

UpdateFitnessMetricsResponse = _reflection.GeneratedProtocolMessageType('UpdateFitnessMetricsResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEFITNESSMETRICSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.update_fitness_metrics_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.UpdateFitnessMetricsResponse)
  ))
_sym_db.RegisterMessage(UpdateFitnessMetricsResponse)


# @@protoc_insertion_point(module_scope)