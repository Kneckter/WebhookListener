# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/social/search_player_response.proto

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
  name='pogoprotos/networking/responses/social/search_player_response.proto',
  package='pogoprotos.networking.responses.social',
  syntax='proto3',
  serialized_pb=_b('\nCpogoprotos/networking/responses/social/search_player_response.proto\x12&pogoprotos.networking.responses.social\x1a+pogoprotos/data/player/player_summary.proto\"\xf3\x01\n\x14SearchPlayerResponse\x12S\n\x06result\x18\x01 \x01(\x0e\x32\x43.pogoprotos.networking.responses.social.SearchPlayerResponse.Result\x12\x35\n\x06player\x18\x02 \x01(\x0b\x32%.pogoprotos.data.player.PlayerSummary\"O\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x1a\n\x16\x45RROR_PLAYER_NOT_FOUND\x10\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_player__summary__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SEARCHPLAYERRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.social.SearchPlayerResponse.Result',
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
      name='ERROR_PLAYER_NOT_FOUND', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=321,
  serialized_end=400,
)
_sym_db.RegisterEnumDescriptor(_SEARCHPLAYERRESPONSE_RESULT)


_SEARCHPLAYERRESPONSE = _descriptor.Descriptor(
  name='SearchPlayerResponse',
  full_name='pogoprotos.networking.responses.social.SearchPlayerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.social.SearchPlayerResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player', full_name='pogoprotos.networking.responses.social.SearchPlayerResponse.player', index=1,
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
    _SEARCHPLAYERRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=400,
)

_SEARCHPLAYERRESPONSE.fields_by_name['result'].enum_type = _SEARCHPLAYERRESPONSE_RESULT
_SEARCHPLAYERRESPONSE.fields_by_name['player'].message_type = pogoprotos_dot_data_dot_player_dot_player__summary__pb2._PLAYERSUMMARY
_SEARCHPLAYERRESPONSE_RESULT.containing_type = _SEARCHPLAYERRESPONSE
DESCRIPTOR.message_types_by_name['SearchPlayerResponse'] = _SEARCHPLAYERRESPONSE

SearchPlayerResponse = _reflection.GeneratedProtocolMessageType('SearchPlayerResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHPLAYERRESPONSE,
  __module__ = 'pogoprotos.networking.responses.social.search_player_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.SearchPlayerResponse)
  ))
_sym_db.RegisterMessage(SearchPlayerResponse)


# @@protoc_insertion_point(module_scope)
