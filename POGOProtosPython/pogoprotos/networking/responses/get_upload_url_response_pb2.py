# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_upload_url_response.proto

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
  name='pogoprotos/networking/responses/get_upload_url_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n=pogoprotos/networking/responses/get_upload_url_response.proto\x12\x1fpogoprotos.networking.responses\"\xcd\x01\n\x14GetUploadUrlResponse\x12L\n\x06status\x18\x01 \x01(\x0e\x32<.pogoprotos.networking.responses.GetUploadUrlResponse.Status\x12\x12\n\nsigned_url\x18\x02 \x01(\t\x12#\n\x1bsupporting_image_signed_url\x18\x03 \x01(\t\".\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08\x46\x41ILURES\x10\x01\x12\x0b\n\x07SUCCESS\x10\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETUPLOADURLRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.GetUploadUrlResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURES', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=258,
  serialized_end=304,
)
_sym_db.RegisterEnumDescriptor(_GETUPLOADURLRESPONSE_STATUS)


_GETUPLOADURLRESPONSE = _descriptor.Descriptor(
  name='GetUploadUrlResponse',
  full_name='pogoprotos.networking.responses.GetUploadUrlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.GetUploadUrlResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signed_url', full_name='pogoprotos.networking.responses.GetUploadUrlResponse.signed_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supporting_image_signed_url', full_name='pogoprotos.networking.responses.GetUploadUrlResponse.supporting_image_signed_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETUPLOADURLRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=304,
)

_GETUPLOADURLRESPONSE.fields_by_name['status'].enum_type = _GETUPLOADURLRESPONSE_STATUS
_GETUPLOADURLRESPONSE_STATUS.containing_type = _GETUPLOADURLRESPONSE
DESCRIPTOR.message_types_by_name['GetUploadUrlResponse'] = _GETUPLOADURLRESPONSE

GetUploadUrlResponse = _reflection.GeneratedProtocolMessageType('GetUploadUrlResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETUPLOADURLRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_upload_url_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetUploadUrlResponse)
  ))
_sym_db.RegisterMessage(GetUploadUrlResponse)


# @@protoc_insertion_point(module_scope)
