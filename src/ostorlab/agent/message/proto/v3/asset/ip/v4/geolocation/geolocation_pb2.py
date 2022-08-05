# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ostorlab/agent/message/proto/v3/asset/ip/v4/geolocation/geolocation.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ostorlab/agent/message/proto/v3/asset/ip/v4/geolocation/geolocation.proto',
  package='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nIostorlab/agent/message/proto/v3/asset/ip/v4/geolocation/geolocation.proto\x12\x37ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation\"\x94\x02\n\x07Message\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04mask\x18\x02 \x01(\t\x12\x12\n\x07version\x18\x03 \x01(\x05:\x01\x34\x12\x11\n\tcontinent\x18\x05 \x01(\t\x12\x16\n\x0e\x63ontinent_code\x18\x06 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x07 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x08 \x01(\t\x12\x0e\n\x06region\x18\t \x01(\t\x12\x13\n\x0bregion_name\x18\n \x01(\t\x12\x0c\n\x04\x63ity\x18\x0b \x01(\t\x12\x0b\n\x03zip\x18\x0c \x01(\t\x12\x10\n\x08latitude\x18\r \x01(\x02\x12\x11\n\tlongitude\x18\x0e \x01(\x02\x12\x10\n\x08timezone\x18\x0f \x01(\t\x12\x10\n\x08\x64istrict\x18\x10 \x01(\t'
)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mask', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.mask', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.version', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=4,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='continent', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.continent', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='continent_code', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.continent_code', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.country', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.country_code', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.region', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region_name', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.region_name', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='city', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.city', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zip', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.zip', index=10,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.latitude', index=11,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.longitude', index=12,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.timezone', index=13,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='district', full_name='ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message.district', index=14,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=411,
)

DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.geolocation_pb2'
  # @@protoc_insertion_point(class_scope:ostorlab.agent.message.proto.v3.asset.ip.v4.geolocation.Message)
  })
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
