# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/sfida_connect_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/sfida_connect_state.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n*pogoprotos/enums/sfida_connect_state.proto\x12\x10pogoprotos.enums*\x97\x01\n\x11SfidaConnectState\x12\x10\n\x0c\x44ISCONNECTED\x10\x00\x12\x11\n\rDISCONNECTING\x10\x01\x12\r\n\tCONNECTED\x10\x02\x12\x0e\n\nDISCOVERED\x10\x03\x12\r\n\tCERTIFIED\x10\x04\x12\x13\n\x0fSOFTWARE_UPDATE\x10\x05\x12\n\n\x06\x46\x41ILED\x10\x06\x12\x0e\n\nCONNECTING\x10\x07\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_SFIDACONNECTSTATE = _descriptor.EnumDescriptor(
  name='SfidaConnectState',
  full_name='pogoprotos.enums.SfidaConnectState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DISCONNECTED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCONNECTING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECTED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCOVERED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CERTIFIED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOFTWARE_UPDATE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECTING', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=65,
  serialized_end=216,
)
_sym_db.RegisterEnumDescriptor(_SFIDACONNECTSTATE)

SfidaConnectState = enum_type_wrapper.EnumTypeWrapper(_SFIDACONNECTSTATE)
DISCONNECTED = 0
DISCONNECTING = 1
CONNECTED = 2
DISCOVERED = 3
CERTIFIED = 4
SOFTWARE_UPDATE = 5
FAILED = 6
CONNECTING = 7


DESCRIPTOR.enum_types_by_name['SfidaConnectState'] = _SFIDACONNECTSTATE


# @@protoc_insertion_point(module_scope)
