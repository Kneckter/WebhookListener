# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/social/create_invite_code_message.proto

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
  name='pogoprotos/networking/requests/social/create_invite_code_message.proto',
  package='pogoprotos.networking.requests.social',
  syntax='proto3',
  serialized_pb=_b('\nFpogoprotos/networking/requests/social/create_invite_code_message.proto\x12%pogoprotos.networking.requests.social\"6\n\x17\x43reateInviteCodeMessage\x12\x1b\n\x13\x66orce_generate_code\x18\x01 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CREATEINVITECODEMESSAGE = _descriptor.Descriptor(
  name='CreateInviteCodeMessage',
  full_name='pogoprotos.networking.requests.social.CreateInviteCodeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='force_generate_code', full_name='pogoprotos.networking.requests.social.CreateInviteCodeMessage.force_generate_code', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=113,
  serialized_end=167,
)

DESCRIPTOR.message_types_by_name['CreateInviteCodeMessage'] = _CREATEINVITECODEMESSAGE

CreateInviteCodeMessage = _reflection.GeneratedProtocolMessageType('CreateInviteCodeMessage', (_message.Message,), dict(
  DESCRIPTOR = _CREATEINVITECODEMESSAGE,
  __module__ = 'pogoprotos.networking.requests.social.create_invite_code_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.social.CreateInviteCodeMessage)
  ))
_sym_db.RegisterMessage(CreateInviteCodeMessage)


# @@protoc_insertion_point(module_scope)
