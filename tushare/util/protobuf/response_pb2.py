# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='response.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eresponse.proto\x1a\x19google/protobuf/any.proto\"\x1f\n\rColumnDataInt\x12\x0e\n\x06values\x18\x01 \x03(\x03\"!\n\x0f\x43olumnDataFloat\x12\x0e\n\x06values\x18\x01 \x03(\x01\"\x1f\n\rColumnDataStr\x12\x0e\n\x06values\x18\x01 \x03(\t\")\n\x0b\x43olumnField\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"`\n\tDataFrame\x12\x10\n\x08has_more\x18\x01 \x01(\x08\x12\x1c\n\x06\x66ields\x18\x02 \x03(\x0b\x32\x0c.ColumnField\x12#\n\x05items\x18\x03 \x03(\x0b\x32\x14.google.protobuf.Any\"S\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x12\n\nrequest_id\x18\x03 \x01(\t\x12\x18\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\n.DataFrameb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_COLUMNDATAINT = _descriptor.Descriptor(
  name='ColumnDataInt',
  full_name='ColumnDataInt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='ColumnDataInt.values', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=76,
)


_COLUMNDATAFLOAT = _descriptor.Descriptor(
  name='ColumnDataFloat',
  full_name='ColumnDataFloat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='ColumnDataFloat.values', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=111,
)


_COLUMNDATASTR = _descriptor.Descriptor(
  name='ColumnDataStr',
  full_name='ColumnDataStr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='ColumnDataStr.values', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=144,
)


_COLUMNFIELD = _descriptor.Descriptor(
  name='ColumnField',
  full_name='ColumnField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ColumnField.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='ColumnField.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=187,
)


_DATAFRAME = _descriptor.Descriptor(
  name='DataFrame',
  full_name='DataFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='has_more', full_name='DataFrame.has_more', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fields', full_name='DataFrame.fields', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='DataFrame.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=285,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='Response.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='Response.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='Response.request_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='Response.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=370,
)

_DATAFRAME.fields_by_name['fields'].message_type = _COLUMNFIELD
_DATAFRAME.fields_by_name['items'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_RESPONSE.fields_by_name['data'].message_type = _DATAFRAME
DESCRIPTOR.message_types_by_name['ColumnDataInt'] = _COLUMNDATAINT
DESCRIPTOR.message_types_by_name['ColumnDataFloat'] = _COLUMNDATAFLOAT
DESCRIPTOR.message_types_by_name['ColumnDataStr'] = _COLUMNDATASTR
DESCRIPTOR.message_types_by_name['ColumnField'] = _COLUMNFIELD
DESCRIPTOR.message_types_by_name['DataFrame'] = _DATAFRAME
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ColumnDataInt = _reflection.GeneratedProtocolMessageType('ColumnDataInt', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNDATAINT,
  '__module__' : 'response_pb2'
  # @@protoc_insertion_point(class_scope:ColumnDataInt)
  })
_sym_db.RegisterMessage(ColumnDataInt)

ColumnDataFloat = _reflection.GeneratedProtocolMessageType('ColumnDataFloat', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNDATAFLOAT,
  '__module__' : 'response_pb2'
  # @@protoc_insertion_point(class_scope:ColumnDataFloat)
  })
_sym_db.RegisterMessage(ColumnDataFloat)

ColumnDataStr = _reflection.GeneratedProtocolMessageType('ColumnDataStr', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNDATASTR,
  '__module__' : 'response_pb2'
  # @@protoc_insertion_point(class_scope:ColumnDataStr)
  })
_sym_db.RegisterMessage(ColumnDataStr)

ColumnField = _reflection.GeneratedProtocolMessageType('ColumnField', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNFIELD,
  '__module__' : 'response_pb2'
  # @@protoc_insertion_point(class_scope:ColumnField)
  })
_sym_db.RegisterMessage(ColumnField)

DataFrame = _reflection.GeneratedProtocolMessageType('DataFrame', (_message.Message,), {
  'DESCRIPTOR' : _DATAFRAME,
  '__module__' : 'response_pb2'
  # @@protoc_insertion_point(class_scope:DataFrame)
  })
_sym_db.RegisterMessage(DataFrame)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'response_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)