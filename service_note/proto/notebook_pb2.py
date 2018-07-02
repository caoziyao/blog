# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/notebook.proto

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
  name='proto/notebook.proto',
  package='notebook',
  syntax='proto3',
  serialized_pb=_b('\n\x14proto/notebook.proto\x12\x08notebook\"\x1f\n\x0fNotebookRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"H\n\x10NotebookResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\r\n\x05title\x18\x04 \x03(\t2V\n\x08Notebook\x12J\n\x0fGetNotebookInfo\x12\x19.notebook.NotebookRequest\x1a\x1a.notebook.NotebookResponse\"\x00\x62\x06proto3')
)




_NOTEBOOKREQUEST = _descriptor.Descriptor(
  name='NotebookRequest',
  full_name='notebook.NotebookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='notebook.NotebookRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=34,
  serialized_end=65,
)


_NOTEBOOKRESPONSE = _descriptor.Descriptor(
  name='NotebookResponse',
  full_name='notebook.NotebookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='notebook.NotebookResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='notebook.NotebookResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='notebook.NotebookResponse.age', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='notebook.NotebookResponse.title', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=67,
  serialized_end=139,
)

DESCRIPTOR.message_types_by_name['NotebookRequest'] = _NOTEBOOKREQUEST
DESCRIPTOR.message_types_by_name['NotebookResponse'] = _NOTEBOOKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NotebookRequest = _reflection.GeneratedProtocolMessageType('NotebookRequest', (_message.Message,), dict(
  DESCRIPTOR = _NOTEBOOKREQUEST,
  __module__ = 'proto.notebook_pb2'
  # @@protoc_insertion_point(class_scope:notebook.NotebookRequest)
  ))
_sym_db.RegisterMessage(NotebookRequest)

NotebookResponse = _reflection.GeneratedProtocolMessageType('NotebookResponse', (_message.Message,), dict(
  DESCRIPTOR = _NOTEBOOKRESPONSE,
  __module__ = 'proto.notebook_pb2'
  # @@protoc_insertion_point(class_scope:notebook.NotebookResponse)
  ))
_sym_db.RegisterMessage(NotebookResponse)



_NOTEBOOK = _descriptor.ServiceDescriptor(
  name='Notebook',
  full_name='notebook.Notebook',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=141,
  serialized_end=227,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetNotebookInfo',
    full_name='notebook.Notebook.GetNotebookInfo',
    index=0,
    containing_service=None,
    input_type=_NOTEBOOKREQUEST,
    output_type=_NOTEBOOKRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NOTEBOOK)

DESCRIPTOR.services_by_name['Notebook'] = _NOTEBOOK

# @@protoc_insertion_point(module_scope)
