# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/responses/get_gmap_settings_response.proto

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
  name='pogoprotos/networking/platform/responses/get_gmap_settings_response.proto',
  package='pogoprotos.networking.platform.responses',
  syntax='proto3',
  serialized_pb=_b('\nIpogoprotos/networking/platform/responses/get_gmap_settings_response.proto\x12(pogoprotos.networking.platform.responses\"\x99\x02\n\x17GetGmapSettingsResponse\x12X\n\x06result\x18\x01 \x01(\x0e\x32H.pogoprotos.networking.platform.responses.GetGmapSettingsResponse.Result\x12\x19\n\x11gmap_template_url\x18\x02 \x01(\t\x12\"\n\x1amax_poi_distance_in_meters\x18\x03 \x01(\x05\"e\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x18\n\x14\x45RROR_MISSING_CONFIG\x10\x03\x12\x16\n\x12\x45RROR_NO_UNIQUE_ID\x10\x04\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETGMAPSETTINGSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.platform.responses.GetGmapSettingsResponse.Result',
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
      name='ERROR_MISSING_CONFIG', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NO_UNIQUE_ID', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=300,
  serialized_end=401,
)
_sym_db.RegisterEnumDescriptor(_GETGMAPSETTINGSRESPONSE_RESULT)


_GETGMAPSETTINGSRESPONSE = _descriptor.Descriptor(
  name='GetGmapSettingsResponse',
  full_name='pogoprotos.networking.platform.responses.GetGmapSettingsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.platform.responses.GetGmapSettingsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gmap_template_url', full_name='pogoprotos.networking.platform.responses.GetGmapSettingsResponse.gmap_template_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_poi_distance_in_meters', full_name='pogoprotos.networking.platform.responses.GetGmapSettingsResponse.max_poi_distance_in_meters', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETGMAPSETTINGSRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=401,
)

_GETGMAPSETTINGSRESPONSE.fields_by_name['result'].enum_type = _GETGMAPSETTINGSRESPONSE_RESULT
_GETGMAPSETTINGSRESPONSE_RESULT.containing_type = _GETGMAPSETTINGSRESPONSE
DESCRIPTOR.message_types_by_name['GetGmapSettingsResponse'] = _GETGMAPSETTINGSRESPONSE

GetGmapSettingsResponse = _reflection.GeneratedProtocolMessageType('GetGmapSettingsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETGMAPSETTINGSRESPONSE,
  __module__ = 'pogoprotos.networking.platform.responses.get_gmap_settings_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.GetGmapSettingsResponse)
  ))
_sym_db.RegisterMessage(GetGmapSettingsResponse)


# @@protoc_insertion_point(module_scope)
