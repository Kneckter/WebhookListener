# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/platform_request_type.proto

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
  name='pogoprotos/networking/platform/platform_request_type.proto',
  package='pogoprotos.networking.platform',
  syntax='proto3',
  serialized_pb=_b('\n:pogoprotos/networking/platform/platform_request_type.proto\x12\x1epogoprotos.networking.platform*\xab\x06\n\x13PlatformRequestType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x15\n\x11MAP_QUERY_REQUEST\x10\x01\x12\x10\n\x0cPURCHASE_SKU\x10\x02\x12\x19\n\x15REDEEM_GOOGLE_RECEIPT\x10\x03\x12\x18\n\x14REDEEM_APPLE_RECEIPT\x10\x04\x12#\n\x1fGET_AVAILABLE_SKUS_AND_BALANCES\x10\x05\x12\x1c\n\x18SEND_ENCRYPTED_SIGNATURE\x10\x06\x12\x1a\n\x16REDEEM_DESKTOP_RECEIPT\x10\x07\x12%\n!DOWNLOAD_PLATFORM_CLIENT_SETTINGS\x10\x08\x12\x13\n\x0fREDEEM_PASSCODE\x10\t\x12\x1e\n\x1aREGISTER_PUSH_NOTIFICATION\x10\n\x12 \n\x1cUNREGISTER_PUSH_NOTIFICATION\x10\x0b\x12\x1e\n\x1aUPDATE_NOTIFICATION_STATUS\x10\x0c\x12\x0f\n\x0b\x41\x44\x44_NEW_POI\x10\r\x12\x14\n\x10\x41\x44\x44_LOGIN_ACTION\x10\x0e\x12\x17\n\x13REMOVE_LOGIN_ACTION\x10\x0f\x12\x15\n\x11LIST_LOGIN_ACTION\x10\x10\x12\x1c\n\x18\x43OLLECT_CLIENT_TELEMETRY\x10\x11\x12#\n\x1fGET_SIGNED_URL_FOR_PHOTO_UPLOAD\x10\x12\x12\x18\n\x14REPLACE_LOGIN_ACTION\x10\x13\x12\r\n\tCHALLENGE\x10\x14\x12\x18\n\x14SAFETY_NET_CHALLENGE\x10\x15\x12\x1a\n\x16UPDATE_FITNESS_METRICS\x10\x16\x12\x16\n\x12GET_FITNESS_REPORT\x10\x17\x12&\n\"SET_IN_GAME_CURRENCY_EXCHANGE_RATE\x10\x18\x12&\n\"REGISTER_DOWNSTREAM_SERVER_ACTIONS\x10\x1e\x12\x1d\n\x19\x44OWNSTREAM_SERVER_ACTIONS\x10\x1f\x12\x14\n\x10TEMP_TEST_RESULT\x10\x65\x12\x16\n\x11GET_GMAP_SETTINGS\x10\xac\'b\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PLATFORMREQUESTTYPE = _descriptor.EnumDescriptor(
  name='PlatformRequestType',
  full_name='pogoprotos.networking.platform.PlatformRequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP_QUERY_REQUEST', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PURCHASE_SKU', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDEEM_GOOGLE_RECEIPT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDEEM_APPLE_RECEIPT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_AVAILABLE_SKUS_AND_BALANCES', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_ENCRYPTED_SIGNATURE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDEEM_DESKTOP_RECEIPT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_PLATFORM_CLIENT_SETTINGS', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDEEM_PASSCODE', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_PUSH_NOTIFICATION', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNREGISTER_PUSH_NOTIFICATION', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_NOTIFICATION_STATUS', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_NEW_POI', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_LOGIN_ACTION', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_LOGIN_ACTION', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_LOGIN_ACTION', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECT_CLIENT_TELEMETRY', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_SIGNED_URL_FOR_PHOTO_UPLOAD', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLACE_LOGIN_ACTION', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAFETY_NET_CHALLENGE', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_FITNESS_METRICS', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_FITNESS_REPORT', index=23, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_IN_GAME_CURRENCY_EXCHANGE_RATE', index=24, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_DOWNSTREAM_SERVER_ACTIONS', index=25, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNSTREAM_SERVER_ACTIONS', index=26, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMP_TEST_RESULT', index=27, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_GMAP_SETTINGS', index=28, number=5036,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=95,
  serialized_end=906,
)
_sym_db.RegisterEnumDescriptor(_PLATFORMREQUESTTYPE)

PlatformRequestType = enum_type_wrapper.EnumTypeWrapper(_PLATFORMREQUESTTYPE)
UNKNOWN = 0
MAP_QUERY_REQUEST = 1
PURCHASE_SKU = 2
REDEEM_GOOGLE_RECEIPT = 3
REDEEM_APPLE_RECEIPT = 4
GET_AVAILABLE_SKUS_AND_BALANCES = 5
SEND_ENCRYPTED_SIGNATURE = 6
REDEEM_DESKTOP_RECEIPT = 7
DOWNLOAD_PLATFORM_CLIENT_SETTINGS = 8
REDEEM_PASSCODE = 9
REGISTER_PUSH_NOTIFICATION = 10
UNREGISTER_PUSH_NOTIFICATION = 11
UPDATE_NOTIFICATION_STATUS = 12
ADD_NEW_POI = 13
ADD_LOGIN_ACTION = 14
REMOVE_LOGIN_ACTION = 15
LIST_LOGIN_ACTION = 16
COLLECT_CLIENT_TELEMETRY = 17
GET_SIGNED_URL_FOR_PHOTO_UPLOAD = 18
REPLACE_LOGIN_ACTION = 19
CHALLENGE = 20
SAFETY_NET_CHALLENGE = 21
UPDATE_FITNESS_METRICS = 22
GET_FITNESS_REPORT = 23
SET_IN_GAME_CURRENCY_EXCHANGE_RATE = 24
REGISTER_DOWNSTREAM_SERVER_ACTIONS = 30
DOWNSTREAM_SERVER_ACTIONS = 31
TEMP_TEST_RESULT = 101
GET_GMAP_SETTINGS = 5036


DESCRIPTOR.enum_types_by_name['PlatformRequestType'] = _PLATFORMREQUESTTYPE


# @@protoc_insertion_point(module_scope)