# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/requests/update_fitness_metrics_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.fitness import fitness_sample_pb2 as pogoprotos_dot_data_dot_fitness_dot_fitness__sample__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/requests/update_fitness_metrics_message.proto',
  package='pogoprotos.networking.platform.requests',
  syntax='proto3',
  serialized_pb=_b('\nLpogoprotos/networking/platform/requests/update_fitness_metrics_message.proto\x12\'pogoprotos.networking.platform.requests\x1a,pogoprotos/data/fitness/fitness_sample.proto\"^\n\x1bUpdateFitnessMetricsMessage\x12?\n\x0f\x66itness_samples\x18\x01 \x03(\x0b\x32&.pogoprotos.data.fitness.FitnessSampleb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_fitness_dot_fitness__sample__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UPDATEFITNESSMETRICSMESSAGE = _descriptor.Descriptor(
  name='UpdateFitnessMetricsMessage',
  full_name='pogoprotos.networking.platform.requests.UpdateFitnessMetricsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fitness_samples', full_name='pogoprotos.networking.platform.requests.UpdateFitnessMetricsMessage.fitness_samples', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=167,
  serialized_end=261,
)

_UPDATEFITNESSMETRICSMESSAGE.fields_by_name['fitness_samples'].message_type = pogoprotos_dot_data_dot_fitness_dot_fitness__sample__pb2._FITNESSSAMPLE
DESCRIPTOR.message_types_by_name['UpdateFitnessMetricsMessage'] = _UPDATEFITNESSMETRICSMESSAGE

UpdateFitnessMetricsMessage = _reflection.GeneratedProtocolMessageType('UpdateFitnessMetricsMessage', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEFITNESSMETRICSMESSAGE,
  __module__ = 'pogoprotos.networking.platform.requests.update_fitness_metrics_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.requests.UpdateFitnessMetricsMessage)
  ))
_sym_db.RegisterMessage(UpdateFitnessMetricsMessage)


# @@protoc_insertion_point(module_scope)
