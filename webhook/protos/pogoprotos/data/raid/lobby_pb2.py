# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/raid/lobby.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.battle import battle_participant_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2
from pogoprotos.enums import weather_condition_pb2 as pogoprotos_dot_enums_dot_weather__condition__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/raid/lobby.proto',
  package='pogoprotos.data.raid',
  syntax='proto3',
  serialized_pb=_b('\n pogoprotos/data/raid/lobby.proto\x12\x14pogoprotos.data.raid\x1a/pogoprotos/data/battle/battle_participant.proto\x1a(pogoprotos/enums/weather_condition.proto\"\x80\x03\n\x05Lobby\x12\x10\n\x08lobby_id\x18\x01 \x03(\x05\x12:\n\x07players\x18\x02 \x03(\x0b\x32).pogoprotos.data.battle.BattleParticipant\x12\x1a\n\x12player_join_end_ms\x18\x03 \x01(\x03\x12 \n\x18pokemon_selection_end_ms\x18\x04 \x01(\x03\x12\x1c\n\x14raid_battle_start_ms\x18\x05 \x01(\x03\x12\x1a\n\x12raid_battle_end_ms\x18\x06 \x01(\x03\x12\x16\n\x0eraid_battle_id\x18\x08 \x01(\t\x12\x16\n\x0eowner_nickname\x18\t \x01(\t\x12\x0f\n\x07private\x18\n \x01(\x08\x12\x13\n\x0b\x63reation_ms\x18\x0b \x01(\x03\x12\x1c\n\x14\x62\x61ttle_plfe_instance\x18\x0c \x01(\x05\x12=\n\x11weather_condition\x18\r \x01(\x0e\x32\".pogoprotos.enums.WeatherConditionb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_weather__condition__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LOBBY = _descriptor.Descriptor(
  name='Lobby',
  full_name='pogoprotos.data.raid.Lobby',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lobby_id', full_name='pogoprotos.data.raid.Lobby.lobby_id', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='players', full_name='pogoprotos.data.raid.Lobby.players', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_join_end_ms', full_name='pogoprotos.data.raid.Lobby.player_join_end_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_selection_end_ms', full_name='pogoprotos.data.raid.Lobby.pokemon_selection_end_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_battle_start_ms', full_name='pogoprotos.data.raid.Lobby.raid_battle_start_ms', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_battle_end_ms', full_name='pogoprotos.data.raid.Lobby.raid_battle_end_ms', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_battle_id', full_name='pogoprotos.data.raid.Lobby.raid_battle_id', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owner_nickname', full_name='pogoprotos.data.raid.Lobby.owner_nickname', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='private', full_name='pogoprotos.data.raid.Lobby.private', index=8,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_ms', full_name='pogoprotos.data.raid.Lobby.creation_ms', index=9,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_plfe_instance', full_name='pogoprotos.data.raid.Lobby.battle_plfe_instance', index=10,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weather_condition', full_name='pogoprotos.data.raid.Lobby.weather_condition', index=11,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=150,
  serialized_end=534,
)

_LOBBY.fields_by_name['players'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2._BATTLEPARTICIPANT
_LOBBY.fields_by_name['weather_condition'].enum_type = pogoprotos_dot_enums_dot_weather__condition__pb2._WEATHERCONDITION
DESCRIPTOR.message_types_by_name['Lobby'] = _LOBBY

Lobby = _reflection.GeneratedProtocolMessageType('Lobby', (_message.Message,), dict(
  DESCRIPTOR = _LOBBY,
  __module__ = 'pogoprotos.data.raid.lobby_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.raid.Lobby)
  ))
_sym_db.RegisterMessage(Lobby)


# @@protoc_insertion_point(module_scope)
