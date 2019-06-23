# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/social/accept_friend_invite_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.player import player_summary_pb2 as pogoprotos_dot_data_dot_player_dot_player__summary__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/social/accept_friend_invite_response.proto',
  package='pogoprotos.networking.responses.social',
  syntax='proto3',
  serialized_pb=_b('\nJpogoprotos/networking/responses/social/accept_friend_invite_response.proto\x12&pogoprotos.networking.responses.social\x1a+pogoprotos/data/player/player_summary.proto\"\x9d\x03\n\x1a\x41\x63\x63\x65ptFriendInviteResponse\x12Y\n\x06result\x18\x01 \x01(\x0e\x32I.pogoprotos.networking.responses.social.AcceptFriendInviteResponse.Result\x12\x35\n\x06\x66riend\x18\x02 \x01(\x0b\x32%.pogoprotos.data.player.PlayerSummary\"\xec\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x1f\n\x1b\x45RROR_INVITE_DOES_NOT_EXIST\x10\x03\x12+\n\'ERROR_MAX_FRIENDS_LIMIT_REACHED_DELETED\x10\x04\x12#\n\x1f\x45RROR_INVITE_HAS_BEEN_CANCELLED\x10\x05\x12 \n\x1c\x45RROR_SENDER_HAS_MAX_FRIENDS\x10\x06\x12\"\n\x1e\x45RROR_RECEIVER_HAS_MAX_FRIENDS\x10\x07\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_player__summary__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ACCEPTFRIENDINVITERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.social.AcceptFriendInviteResponse.Result',
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
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVITE_DOES_NOT_EXIST', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_MAX_FRIENDS_LIMIT_REACHED_DELETED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVITE_HAS_BEEN_CANCELLED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_SENDER_HAS_MAX_FRIENDS', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_RECEIVER_HAS_MAX_FRIENDS', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=341,
  serialized_end=577,
)
_sym_db.RegisterEnumDescriptor(_ACCEPTFRIENDINVITERESPONSE_RESULT)


_ACCEPTFRIENDINVITERESPONSE = _descriptor.Descriptor(
  name='AcceptFriendInviteResponse',
  full_name='pogoprotos.networking.responses.social.AcceptFriendInviteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.social.AcceptFriendInviteResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend', full_name='pogoprotos.networking.responses.social.AcceptFriendInviteResponse.friend', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACCEPTFRIENDINVITERESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=577,
)

_ACCEPTFRIENDINVITERESPONSE.fields_by_name['result'].enum_type = _ACCEPTFRIENDINVITERESPONSE_RESULT
_ACCEPTFRIENDINVITERESPONSE.fields_by_name['friend'].message_type = pogoprotos_dot_data_dot_player_dot_player__summary__pb2._PLAYERSUMMARY
_ACCEPTFRIENDINVITERESPONSE_RESULT.containing_type = _ACCEPTFRIENDINVITERESPONSE
DESCRIPTOR.message_types_by_name['AcceptFriendInviteResponse'] = _ACCEPTFRIENDINVITERESPONSE

AcceptFriendInviteResponse = _reflection.GeneratedProtocolMessageType('AcceptFriendInviteResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACCEPTFRIENDINVITERESPONSE,
  __module__ = 'pogoprotos.networking.responses.social.accept_friend_invite_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.AcceptFriendInviteResponse)
  ))
_sym_db.RegisterMessage(AcceptFriendInviteResponse)


# @@protoc_insertion_point(module_scope)
