# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/mark_read_news_article_response.proto

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
  name='pogoprotos/networking/responses/mark_read_news_article_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nEpogoprotos/networking/responses/mark_read_news_article_response.proto\x12\x1fpogoprotos.networking.responses\"\xa7\x01\n\x1bMarkReadNewsArticleResponse\x12S\n\x06result\x18\x01 \x01(\x0e\x32\x43.pogoprotos.networking.responses.MarkReadNewsArticleResponse.Result\"3\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rNO_NEWS_FOUND\x10\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_MARKREADNEWSARTICLERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.MarkReadNewsArticleResponse.Result',
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
      name='NO_NEWS_FOUND', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=223,
  serialized_end=274,
)
_sym_db.RegisterEnumDescriptor(_MARKREADNEWSARTICLERESPONSE_RESULT)


_MARKREADNEWSARTICLERESPONSE = _descriptor.Descriptor(
  name='MarkReadNewsArticleResponse',
  full_name='pogoprotos.networking.responses.MarkReadNewsArticleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.MarkReadNewsArticleResponse.result', index=0,
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
    _MARKREADNEWSARTICLERESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=274,
)

_MARKREADNEWSARTICLERESPONSE.fields_by_name['result'].enum_type = _MARKREADNEWSARTICLERESPONSE_RESULT
_MARKREADNEWSARTICLERESPONSE_RESULT.containing_type = _MARKREADNEWSARTICLERESPONSE
DESCRIPTOR.message_types_by_name['MarkReadNewsArticleResponse'] = _MARKREADNEWSARTICLERESPONSE

MarkReadNewsArticleResponse = _reflection.GeneratedProtocolMessageType('MarkReadNewsArticleResponse', (_message.Message,), dict(
  DESCRIPTOR = _MARKREADNEWSARTICLERESPONSE,
  __module__ = 'pogoprotos.networking.responses.mark_read_news_article_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.MarkReadNewsArticleResponse)
  ))
_sym_db.RegisterMessage(MarkReadNewsArticleResponse)


# @@protoc_insertion_point(module_scope)
