# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/poi_global_settings.proto

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
  name='pogoprotos/settings/poi_global_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n-pogoprotos/settings/poi_global_settings.proto\x12\x13pogoprotos.settings\"\'\n\x11PoiGlobalSettings\x12\x12\n\nis_enabled\x18\x01 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POIGLOBALSETTINGS = _descriptor.Descriptor(
  name='PoiGlobalSettings',
  full_name='pogoprotos.settings.PoiGlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_enabled', full_name='pogoprotos.settings.PoiGlobalSettings.is_enabled', index=0,
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
  serialized_start=70,
  serialized_end=109,
)

DESCRIPTOR.message_types_by_name['PoiGlobalSettings'] = _POIGLOBALSETTINGS

PoiGlobalSettings = _reflection.GeneratedProtocolMessageType('PoiGlobalSettings', (_message.Message,), dict(
  DESCRIPTOR = _POIGLOBALSETTINGS,
  __module__ = 'pogoprotos.settings.poi_global_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.PoiGlobalSettings)
  ))
_sym_db.RegisterMessage(PoiGlobalSettings)


# @@protoc_insertion_point(module_scope)
