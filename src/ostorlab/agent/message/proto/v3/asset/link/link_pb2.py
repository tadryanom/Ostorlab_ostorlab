# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3/asset/link/link.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v3/asset/link/link.proto',
  package='v3.asset.link',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x18v3/asset/link/link.proto\x12\rv3.asset.link\"%\n\x06Header\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"%\n\x06\x43ookie\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"7\n\x0cLocalStorage\x12\x0b\n\x03url\x18\x01 \x02(\t\x12\x0b\n\x03key\x18\x02 \x02(\t\x12\r\n\x05value\x18\x03 \x02(\t\"6\n\tFormInput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x02(\t\x12\x0c\n\x04type\x18\x03 \x02(\t\"A\n\x04\x46orm\x12(\n\x06inputs\x18\x01 \x03(\x0b\x32\x18.v3.asset.link.FormInput\x12\x0f\n\x07\x65nctype\x18\x02 \x02(\t\">\n\x0e\x46ormCredential\x12\r\n\x05login\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\"\"\n\x10ScriptCredential\x12\x0e\n\x06script\x18\x01 \x01(\t\"\xab\x03\n\x07Message\x12\x0b\n\x03url\x18\x01 \x02(\t\x12\x0e\n\x06method\x18\x02 \x02(\t\x12\x0e\n\x04\x62ody\x18\x03 \x01(\x0cH\x00\x12#\n\x04\x66orm\x18\x04 \x01(\x0b\x32\x13.v3.asset.link.FormH\x00\x12,\n\rextra_headers\x18\x05 \x03(\x0b\x32\x15.v3.asset.link.Header\x12&\n\x07\x63ookies\x18\x06 \x03(\x0b\x32\x15.v3.asset.link.Cookie\x12\x38\n\x0f\x66orm_credential\x18\x07 \x01(\x0b\x32\x1d.v3.asset.link.FormCredentialH\x01\x12<\n\x11script_credential\x18\x08 \x01(\x0b\x32\x1f.v3.asset.link.ScriptCredentialH\x01\x12&\n\x06parent\x18\t \x01(\x0b\x32\x16.v3.asset.link.Message\x12\x36\n\x11localstorageitems\x18\n \x03(\x0b\x32\x1b.v3.asset.link.LocalStorageB\x0c\n\nbody_oneofB\x12\n\x10\x63redential_oneof')
)




_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='v3.asset.link.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='v3.asset.link.Header.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v3.asset.link.Header.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=43,
  serialized_end=80,
)


_COOKIE = _descriptor.Descriptor(
  name='Cookie',
  full_name='v3.asset.link.Cookie',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='v3.asset.link.Cookie.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v3.asset.link.Cookie.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=82,
  serialized_end=119,
)


_LOCALSTORAGE = _descriptor.Descriptor(
  name='LocalStorage',
  full_name='v3.asset.link.LocalStorage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='v3.asset.link.LocalStorage.url', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='v3.asset.link.LocalStorage.key', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v3.asset.link.LocalStorage.value', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=121,
  serialized_end=176,
)


_FORMINPUT = _descriptor.Descriptor(
  name='FormInput',
  full_name='v3.asset.link.FormInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='v3.asset.link.FormInput.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v3.asset.link.FormInput.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='v3.asset.link.FormInput.type', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=178,
  serialized_end=232,
)


_FORM = _descriptor.Descriptor(
  name='Form',
  full_name='v3.asset.link.Form',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='v3.asset.link.Form.inputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enctype', full_name='v3.asset.link.Form.enctype', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=234,
  serialized_end=299,
)


_FORMCREDENTIAL = _descriptor.Descriptor(
  name='FormCredential',
  full_name='v3.asset.link.FormCredential',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='v3.asset.link.FormCredential.login', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='v3.asset.link.FormCredential.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='v3.asset.link.FormCredential.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=301,
  serialized_end=363,
)


_SCRIPTCREDENTIAL = _descriptor.Descriptor(
  name='ScriptCredential',
  full_name='v3.asset.link.ScriptCredential',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='script', full_name='v3.asset.link.ScriptCredential.script', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=365,
  serialized_end=399,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='v3.asset.link.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='v3.asset.link.Message.url', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method', full_name='v3.asset.link.Message.method', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='v3.asset.link.Message.body', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='form', full_name='v3.asset.link.Message.form', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra_headers', full_name='v3.asset.link.Message.extra_headers', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cookies', full_name='v3.asset.link.Message.cookies', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='form_credential', full_name='v3.asset.link.Message.form_credential', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script_credential', full_name='v3.asset.link.Message.script_credential', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='v3.asset.link.Message.parent', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localstorageitems', full_name='v3.asset.link.Message.localstorageitems', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='body_oneof', full_name='v3.asset.link.Message.body_oneof',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='credential_oneof', full_name='v3.asset.link.Message.credential_oneof',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=402,
  serialized_end=829,
)

_FORM.fields_by_name['inputs'].message_type = _FORMINPUT
_MESSAGE.fields_by_name['form'].message_type = _FORM
_MESSAGE.fields_by_name['extra_headers'].message_type = _HEADER
_MESSAGE.fields_by_name['cookies'].message_type = _COOKIE
_MESSAGE.fields_by_name['form_credential'].message_type = _FORMCREDENTIAL
_MESSAGE.fields_by_name['script_credential'].message_type = _SCRIPTCREDENTIAL
_MESSAGE.fields_by_name['parent'].message_type = _MESSAGE
_MESSAGE.fields_by_name['localstorageitems'].message_type = _LOCALSTORAGE
_MESSAGE.oneofs_by_name['body_oneof'].fields.append(
  _MESSAGE.fields_by_name['body'])
_MESSAGE.fields_by_name['body'].containing_oneof = _MESSAGE.oneofs_by_name['body_oneof']
_MESSAGE.oneofs_by_name['body_oneof'].fields.append(
  _MESSAGE.fields_by_name['form'])
_MESSAGE.fields_by_name['form'].containing_oneof = _MESSAGE.oneofs_by_name['body_oneof']
_MESSAGE.oneofs_by_name['credential_oneof'].fields.append(
  _MESSAGE.fields_by_name['form_credential'])
_MESSAGE.fields_by_name['form_credential'].containing_oneof = _MESSAGE.oneofs_by_name['credential_oneof']
_MESSAGE.oneofs_by_name['credential_oneof'].fields.append(
  _MESSAGE.fields_by_name['script_credential'])
_MESSAGE.fields_by_name['script_credential'].containing_oneof = _MESSAGE.oneofs_by_name['credential_oneof']
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Cookie'] = _COOKIE
DESCRIPTOR.message_types_by_name['LocalStorage'] = _LOCALSTORAGE
DESCRIPTOR.message_types_by_name['FormInput'] = _FORMINPUT
DESCRIPTOR.message_types_by_name['Form'] = _FORM
DESCRIPTOR.message_types_by_name['FormCredential'] = _FORMCREDENTIAL
DESCRIPTOR.message_types_by_name['ScriptCredential'] = _SCRIPTCREDENTIAL
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.Header)
  ))
_sym_db.RegisterMessage(Header)

Cookie = _reflection.GeneratedProtocolMessageType('Cookie', (_message.Message,), dict(
  DESCRIPTOR = _COOKIE,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.Cookie)
  ))
_sym_db.RegisterMessage(Cookie)

LocalStorage = _reflection.GeneratedProtocolMessageType('LocalStorage', (_message.Message,), dict(
  DESCRIPTOR = _LOCALSTORAGE,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.LocalStorage)
  ))
_sym_db.RegisterMessage(LocalStorage)

FormInput = _reflection.GeneratedProtocolMessageType('FormInput', (_message.Message,), dict(
  DESCRIPTOR = _FORMINPUT,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.FormInput)
  ))
_sym_db.RegisterMessage(FormInput)

Form = _reflection.GeneratedProtocolMessageType('Form', (_message.Message,), dict(
  DESCRIPTOR = _FORM,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.Form)
  ))
_sym_db.RegisterMessage(Form)

FormCredential = _reflection.GeneratedProtocolMessageType('FormCredential', (_message.Message,), dict(
  DESCRIPTOR = _FORMCREDENTIAL,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.FormCredential)
  ))
_sym_db.RegisterMessage(FormCredential)

ScriptCredential = _reflection.GeneratedProtocolMessageType('ScriptCredential', (_message.Message,), dict(
  DESCRIPTOR = _SCRIPTCREDENTIAL,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.ScriptCredential)
  ))
_sym_db.RegisterMessage(ScriptCredential)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
