# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/item/battle_attributes.proto

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
  name='pogoprotos/settings/master/item/battle_attributes.proto',
  package='pogoprotos.settings.master.item',
  syntax='proto3',
  serialized_pb=_b('\n7pogoprotos/settings/master/item/battle_attributes.proto\x12\x1fpogoprotos.settings.master.item\"e\n\x10\x42\x61ttleAttributes\x12\x13\n\x0bsta_percent\x18\x01 \x01(\x02\x12\x13\n\x0b\x61tk_percent\x18\x02 \x01(\x02\x12\x13\n\x0b\x64\x65\x66_percent\x18\x03 \x01(\x02\x12\x12\n\nduration_s\x18\x04 \x01(\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BATTLEATTRIBUTES = _descriptor.Descriptor(
  name='BattleAttributes',
  full_name='pogoprotos.settings.master.item.BattleAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sta_percent', full_name='pogoprotos.settings.master.item.BattleAttributes.sta_percent', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='atk_percent', full_name='pogoprotos.settings.master.item.BattleAttributes.atk_percent', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='def_percent', full_name='pogoprotos.settings.master.item.BattleAttributes.def_percent', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration_s', full_name='pogoprotos.settings.master.item.BattleAttributes.duration_s', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=92,
  serialized_end=193,
)

DESCRIPTOR.message_types_by_name['BattleAttributes'] = _BATTLEATTRIBUTES

BattleAttributes = _reflection.GeneratedProtocolMessageType('BattleAttributes', (_message.Message,), dict(
  DESCRIPTOR = _BATTLEATTRIBUTES,
  __module__ = 'pogoprotos.settings.master.item.battle_attributes_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.item.BattleAttributes)
  ))
_sym_db.RegisterMessage(BattleAttributes)


# @@protoc_insertion_point(module_scope)
