# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/combat_global_settings.proto

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
  name='pogoprotos/settings/combat_global_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n0pogoprotos/settings/combat_global_settings.proto\x12\x13pogoprotos.settings\"\xe3\x03\n\x14\x43ombatGlobalSettings\x12\x15\n\renable_combat\x18\x01 \x01(\x08\x12&\n\x1emaximum_daily_rewarded_battles\x18\x02 \x01(\x05\x12!\n\x19\x65nable_combat_stat_stages\x18\x03 \x01(\x08\x12\x1c\n\x14minimum_player_level\x18\x04 \x01(\r\x12*\n\"maximum_daily_npc_rewarded_battles\x18\x05 \x01(\x05\x12(\n active_combat_update_interval_ms\x18\x06 \x01(\x05\x12-\n%waiting_for_player_update_interval_ms\x18\x07 \x01(\x05\x12+\n#ready_for_battle_update_interval_ms\x18\x08 \x01(\x05\x12!\n\x19pre_move_submit_window_ms\x18\t \x01(\x05\x12\"\n\x1apost_move_submit_window_ms\x18\n \x01(\x05\x12\x16\n\x0e\x65nable_sockets\x18\x0b \x01(\x08\x12\x1c\n\x14\x65nable_spin_minigame\x18\x0c \x01(\x08\x12\x1c\n\x14\x65nable_quick_swap_v2\x18\r \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_COMBATGLOBALSETTINGS = _descriptor.Descriptor(
  name='CombatGlobalSettings',
  full_name='pogoprotos.settings.CombatGlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_combat', full_name='pogoprotos.settings.CombatGlobalSettings.enable_combat', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum_daily_rewarded_battles', full_name='pogoprotos.settings.CombatGlobalSettings.maximum_daily_rewarded_battles', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enable_combat_stat_stages', full_name='pogoprotos.settings.CombatGlobalSettings.enable_combat_stat_stages', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minimum_player_level', full_name='pogoprotos.settings.CombatGlobalSettings.minimum_player_level', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum_daily_npc_rewarded_battles', full_name='pogoprotos.settings.CombatGlobalSettings.maximum_daily_npc_rewarded_battles', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_combat_update_interval_ms', full_name='pogoprotos.settings.CombatGlobalSettings.active_combat_update_interval_ms', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='waiting_for_player_update_interval_ms', full_name='pogoprotos.settings.CombatGlobalSettings.waiting_for_player_update_interval_ms', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ready_for_battle_update_interval_ms', full_name='pogoprotos.settings.CombatGlobalSettings.ready_for_battle_update_interval_ms', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_move_submit_window_ms', full_name='pogoprotos.settings.CombatGlobalSettings.pre_move_submit_window_ms', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='post_move_submit_window_ms', full_name='pogoprotos.settings.CombatGlobalSettings.post_move_submit_window_ms', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enable_sockets', full_name='pogoprotos.settings.CombatGlobalSettings.enable_sockets', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enable_spin_minigame', full_name='pogoprotos.settings.CombatGlobalSettings.enable_spin_minigame', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enable_quick_swap_v2', full_name='pogoprotos.settings.CombatGlobalSettings.enable_quick_swap_v2', index=12,
      number=13, type=8, cpp_type=7, label=1,
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
  serialized_start=74,
  serialized_end=557,
)

DESCRIPTOR.message_types_by_name['CombatGlobalSettings'] = _COMBATGLOBALSETTINGS

CombatGlobalSettings = _reflection.GeneratedProtocolMessageType('CombatGlobalSettings', (_message.Message,), dict(
  DESCRIPTOR = _COMBATGLOBALSETTINGS,
  __module__ = 'pogoprotos.settings.combat_global_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.CombatGlobalSettings)
  ))
_sym_db.RegisterMessage(CombatGlobalSettings)


# @@protoc_insertion_point(module_scope)
