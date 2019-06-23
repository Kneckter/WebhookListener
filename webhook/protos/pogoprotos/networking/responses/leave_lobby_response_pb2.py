# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/leave_lobby_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.raid import lobby_pb2 as pogoprotos_dot_data_dot_raid_dot_lobby__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/leave_lobby_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n:pogoprotos/networking/responses/leave_lobby_response.proto\x12\x1fpogoprotos.networking.responses\x1a pogoprotos/data/raid/lobby.proto\"\xe5\x01\n\x12LeaveLobbyResponse\x12J\n\x06result\x18\x01 \x01(\x0e\x32:.pogoprotos.networking.responses.LeaveLobbyResponse.Result\x12*\n\x05lobby\x18\x02 \x01(\x0b\x32\x1b.pogoprotos.data.raid.Lobby\"W\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1a\n\x16\x45RROR_RAID_UNAVAILABLE\x10\x02\x12\x19\n\x15\x45RROR_LOBBY_NOT_FOUND\x10\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_raid_dot_lobby__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_LEAVELOBBYRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.LeaveLobbyResponse.Result',
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
      name='ERROR_RAID_UNAVAILABLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_LOBBY_NOT_FOUND', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=272,
  serialized_end=359,
)
_sym_db.RegisterEnumDescriptor(_LEAVELOBBYRESPONSE_RESULT)


_LEAVELOBBYRESPONSE = _descriptor.Descriptor(
  name='LeaveLobbyResponse',
  full_name='pogoprotos.networking.responses.LeaveLobbyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.LeaveLobbyResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lobby', full_name='pogoprotos.networking.responses.LeaveLobbyResponse.lobby', index=1,
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
    _LEAVELOBBYRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=359,
)

_LEAVELOBBYRESPONSE.fields_by_name['result'].enum_type = _LEAVELOBBYRESPONSE_RESULT
_LEAVELOBBYRESPONSE.fields_by_name['lobby'].message_type = pogoprotos_dot_data_dot_raid_dot_lobby__pb2._LOBBY
_LEAVELOBBYRESPONSE_RESULT.containing_type = _LEAVELOBBYRESPONSE
DESCRIPTOR.message_types_by_name['LeaveLobbyResponse'] = _LEAVELOBBYRESPONSE

LeaveLobbyResponse = _reflection.GeneratedProtocolMessageType('LeaveLobbyResponse', (_message.Message,), dict(
  DESCRIPTOR = _LEAVELOBBYRESPONSE,
  __module__ = 'pogoprotos.networking.responses.leave_lobby_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.LeaveLobbyResponse)
  ))
_sym_db.RegisterMessage(LeaveLobbyResponse)


# @@protoc_insertion_point(module_scope)
