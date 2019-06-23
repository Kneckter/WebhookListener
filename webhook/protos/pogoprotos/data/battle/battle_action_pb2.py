# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/battle/battle_action.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.battle import battle_results_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__results__pb2
from pogoprotos.data.battle import battle_action_type_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__action__type__pb2
from pogoprotos.data.battle import battle_participant_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2
from pogoprotos.data.friends import leveled_up_friends_pb2 as pogoprotos_dot_data_dot_friends_dot_leveled__up__friends__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/battle/battle_action.proto',
  package='pogoprotos.data.battle',
  syntax='proto3',
  serialized_pb=_b('\n*pogoprotos/data/battle/battle_action.proto\x12\x16pogoprotos.data.battle\x1a+pogoprotos/data/battle/battle_results.proto\x1a/pogoprotos/data/battle/battle_action_type.proto\x1a/pogoprotos/data/battle/battle_participant.proto\x1a\x30pogoprotos/data/friends/leveled_up_friends.proto\"\xca\x04\n\x0c\x42\x61ttleAction\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.pogoprotos.data.battle.BattleActionType\x12\x17\n\x0f\x61\x63tion_start_ms\x18\x02 \x01(\x03\x12\x13\n\x0b\x64uration_ms\x18\x03 \x01(\x05\x12\x14\n\x0c\x65nergy_delta\x18\x05 \x01(\x05\x12\x16\n\x0e\x61ttacker_index\x18\x06 \x01(\x05\x12\x14\n\x0ctarget_index\x18\x07 \x01(\x05\x12\x19\n\x11\x61\x63tive_pokemon_id\x18\x08 \x01(\x06\x12@\n\rplayer_joined\x18\t \x01(\x0b\x32).pogoprotos.data.battle.BattleParticipant\x12=\n\x0e\x62\x61ttle_results\x18\n \x01(\x0b\x32%.pogoprotos.data.battle.BattleResults\x12)\n!damage_windows_start_timestamp_ms\x18\x0b \x01(\x03\x12\'\n\x1f\x64\x61mage_windows_end_timestamp_ms\x18\x0c \x01(\x03\x12>\n\x0bplayer_left\x18\r \x01(\x0b\x32).pogoprotos.data.battle.BattleParticipant\x12\x19\n\x11target_pokemon_id\x18\x0e \x01(\x06\x12\x45\n\x12leveled_up_friends\x18\x0f \x01(\x0b\x32).pogoprotos.data.friends.LeveledUpFriendsb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_battle_dot_battle__results__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_battle_dot_battle__action__type__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_friends_dot_leveled__up__friends__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BATTLEACTION = _descriptor.Descriptor(
  name='BattleAction',
  full_name='pogoprotos.data.battle.BattleAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.data.battle.BattleAction.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_start_ms', full_name='pogoprotos.data.battle.BattleAction.action_start_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration_ms', full_name='pogoprotos.data.battle.BattleAction.duration_ms', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='energy_delta', full_name='pogoprotos.data.battle.BattleAction.energy_delta', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attacker_index', full_name='pogoprotos.data.battle.BattleAction.attacker_index', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_index', full_name='pogoprotos.data.battle.BattleAction.target_index', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_pokemon_id', full_name='pogoprotos.data.battle.BattleAction.active_pokemon_id', index=6,
      number=8, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_joined', full_name='pogoprotos.data.battle.BattleAction.player_joined', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_results', full_name='pogoprotos.data.battle.BattleAction.battle_results', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='damage_windows_start_timestamp_ms', full_name='pogoprotos.data.battle.BattleAction.damage_windows_start_timestamp_ms', index=9,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='damage_windows_end_timestamp_ms', full_name='pogoprotos.data.battle.BattleAction.damage_windows_end_timestamp_ms', index=10,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_left', full_name='pogoprotos.data.battle.BattleAction.player_left', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_pokemon_id', full_name='pogoprotos.data.battle.BattleAction.target_pokemon_id', index=12,
      number=14, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='leveled_up_friends', full_name='pogoprotos.data.battle.BattleAction.leveled_up_friends', index=13,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=264,
  serialized_end=850,
)

_BATTLEACTION.fields_by_name['type'].enum_type = pogoprotos_dot_data_dot_battle_dot_battle__action__type__pb2._BATTLEACTIONTYPE
_BATTLEACTION.fields_by_name['player_joined'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2._BATTLEPARTICIPANT
_BATTLEACTION.fields_by_name['battle_results'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__results__pb2._BATTLERESULTS
_BATTLEACTION.fields_by_name['player_left'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2._BATTLEPARTICIPANT
_BATTLEACTION.fields_by_name['leveled_up_friends'].message_type = pogoprotos_dot_data_dot_friends_dot_leveled__up__friends__pb2._LEVELEDUPFRIENDS
DESCRIPTOR.message_types_by_name['BattleAction'] = _BATTLEACTION

BattleAction = _reflection.GeneratedProtocolMessageType('BattleAction', (_message.Message,), dict(
  DESCRIPTOR = _BATTLEACTION,
  __module__ = 'pogoprotos.data.battle.battle_action_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.battle.BattleAction)
  ))
_sym_db.RegisterMessage(BattleAction)


# @@protoc_insertion_point(module_scope)
