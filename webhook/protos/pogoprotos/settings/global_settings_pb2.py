# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/global_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.settings import event_settings_pb2 as pogoprotos_dot_settings_dot_event__settings__pb2
from pogoprotos.settings import festival_settings_pb2 as pogoprotos_dot_settings_dot_festival__settings__pb2
from pogoprotos.settings import fort_settings_pb2 as pogoprotos_dot_settings_dot_fort__settings__pb2
from pogoprotos.settings import gps_settings_pb2 as pogoprotos_dot_settings_dot_gps__settings__pb2
from pogoprotos.settings import inventory_settings_pb2 as pogoprotos_dot_settings_dot_inventory__settings__pb2
from pogoprotos.settings import level_settings_pb2 as pogoprotos_dot_settings_dot_level__settings__pb2
from pogoprotos.settings import map_settings_pb2 as pogoprotos_dot_settings_dot_map__settings__pb2
from pogoprotos.settings import news_settings_pb2 as pogoprotos_dot_settings_dot_news__settings__pb2
from pogoprotos.settings import notification_settings_pb2 as pogoprotos_dot_settings_dot_notification__settings__pb2
from pogoprotos.settings import passcode_settings_pb2 as pogoprotos_dot_settings_dot_passcode__settings__pb2
from pogoprotos.settings import sfida_settings_pb2 as pogoprotos_dot_settings_dot_sfida__settings__pb2
from pogoprotos.settings import translation_settings_pb2 as pogoprotos_dot_settings_dot_translation__settings__pb2
from pogoprotos.settings import client_performance_settings_pb2 as pogoprotos_dot_settings_dot_client__performance__settings__pb2
from pogoprotos.settings import news_global_settings_pb2 as pogoprotos_dot_settings_dot_news__global__settings__pb2
from pogoprotos.settings import telemetry_global_settings_pb2 as pogoprotos_dot_settings_dot_telemetry__global__settings__pb2
from pogoprotos.settings import login_settings_pb2 as pogoprotos_dot_settings_dot_login__settings__pb2
from pogoprotos.settings import quest_global_settings_pb2 as pogoprotos_dot_settings_dot_quest__global__settings__pb2
from pogoprotos.settings import social_client_settings_pb2 as pogoprotos_dot_settings_dot_social__client__settings__pb2
from pogoprotos.settings import trading_global_settings_pb2 as pogoprotos_dot_settings_dot_trading__global__settings__pb2
from pogoprotos.settings import upsight_logging_settings_pb2 as pogoprotos_dot_settings_dot_upsight__logging__settings__pb2
from pogoprotos.settings import beluga_global_settings_pb2 as pogoprotos_dot_settings_dot_beluga__global__settings__pb2
from pogoprotos.settings import pokecoin_purchase_display_settings_pb2 as pogoprotos_dot_settings_dot_pokecoin__purchase__display__settings__pb2
from pogoprotos.settings import helpshift_settings_pb2 as pogoprotos_dot_settings_dot_helpshift__settings__pb2
from pogoprotos.settings import combat_global_settings_pb2 as pogoprotos_dot_settings_dot_combat__global__settings__pb2
from pogoprotos.settings import third_move_global_settings_pb2 as pogoprotos_dot_settings_dot_third__move__global__settings__pb2
from pogoprotos.settings import combat_challenge_global_settings_pb2 as pogoprotos_dot_settings_dot_combat__challenge__global__settings__pb2
from pogoprotos.settings import poi_global_settings_pb2 as pogoprotos_dot_settings_dot_poi__global__settings__pb2
from pogoprotos.settings import background_mode_global_settings_pb2 as pogoprotos_dot_settings_dot_background__mode__global__settings__pb2
from pogoprotos.settings import probe_settings_pb2 as pogoprotos_dot_settings_dot_probe__settings__pb2
from pogoprotos.settings import pokemon_global_settings_pb2 as pogoprotos_dot_settings_dot_pokemon__global__settings__pb2
from pogoprotos.settings import ar_photo_global_settings_pb2 as pogoprotos_dot_settings_dot_ar__photo__global__settings__pb2
from pogoprotos.settings import avatar_global_settings_pb2 as pogoprotos_dot_settings_dot_avatar__global__settings__pb2
from pogoprotos.settings import evolution_v2_settings_pb2 as pogoprotos_dot_settings_dot_evolution__v2__settings__pb2
from pogoprotos.settings import koala_settings_pb2 as pogoprotos_dot_settings_dot_koala__settings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/global_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n)pogoprotos/settings/global_settings.proto\x12\x13pogoprotos.settings\x1a!pogoprotos/enums/pokemon_id.proto\x1a(pogoprotos/settings/event_settings.proto\x1a+pogoprotos/settings/festival_settings.proto\x1a\'pogoprotos/settings/fort_settings.proto\x1a&pogoprotos/settings/gps_settings.proto\x1a,pogoprotos/settings/inventory_settings.proto\x1a(pogoprotos/settings/level_settings.proto\x1a&pogoprotos/settings/map_settings.proto\x1a\'pogoprotos/settings/news_settings.proto\x1a/pogoprotos/settings/notification_settings.proto\x1a+pogoprotos/settings/passcode_settings.proto\x1a(pogoprotos/settings/sfida_settings.proto\x1a.pogoprotos/settings/translation_settings.proto\x1a\x35pogoprotos/settings/client_performance_settings.proto\x1a.pogoprotos/settings/news_global_settings.proto\x1a\x33pogoprotos/settings/telemetry_global_settings.proto\x1a(pogoprotos/settings/login_settings.proto\x1a/pogoprotos/settings/quest_global_settings.proto\x1a\x30pogoprotos/settings/social_client_settings.proto\x1a\x31pogoprotos/settings/trading_global_settings.proto\x1a\x32pogoprotos/settings/upsight_logging_settings.proto\x1a\x30pogoprotos/settings/beluga_global_settings.proto\x1a<pogoprotos/settings/pokecoin_purchase_display_settings.proto\x1a,pogoprotos/settings/helpshift_settings.proto\x1a\x30pogoprotos/settings/combat_global_settings.proto\x1a\x34pogoprotos/settings/third_move_global_settings.proto\x1a:pogoprotos/settings/combat_challenge_global_settings.proto\x1a-pogoprotos/settings/poi_global_settings.proto\x1a\x39pogoprotos/settings/background_mode_global_settings.proto\x1a(pogoprotos/settings/probe_settings.proto\x1a\x31pogoprotos/settings/pokemon_global_settings.proto\x1a\x32pogoprotos/settings/ar_photo_global_settings.proto\x1a\x30pogoprotos/settings/avatar_global_settings.proto\x1a/pogoprotos/settings/evolution_v2_settings.proto\x1a(pogoprotos/settings/koala_settings.proto\"\xe3\x13\n\x0eGlobalSettings\x12\x38\n\rfort_settings\x18\x02 \x01(\x0b\x32!.pogoprotos.settings.FortSettings\x12\x36\n\x0cmap_settings\x18\x03 \x01(\x0b\x32 .pogoprotos.settings.MapSettings\x12:\n\x0elevel_settings\x18\x04 \x01(\x0b\x32\".pogoprotos.settings.LevelSettings\x12\x42\n\x12inventory_settings\x18\x05 \x01(\x0b\x32&.pogoprotos.settings.InventorySettings\x12\x1e\n\x16minimum_client_version\x18\x06 \x01(\t\x12\x36\n\x0cgps_settings\x18\x07 \x01(\x0b\x32 .pogoprotos.settings.GpsSettings\x12@\n\x11\x66\x65stival_settings\x18\x08 \x01(\x0b\x32%.pogoprotos.settings.FestivalSettings\x12:\n\x0e\x65vent_settings\x18\t \x01(\x0b\x32\".pogoprotos.settings.EventSettings\x12\x19\n\x11max_pokemon_types\x18\n \x01(\x05\x12:\n\x0esfida_settings\x18\x0b \x01(\x0b\x32\".pogoprotos.settings.SfidaSettings\x12\x38\n\rnews_settings\x18\x0c \x01(\x0b\x32!.pogoprotos.settings.NewsSettings\x12\x46\n\x14translation_settings\x18\r \x01(\x0b\x32(.pogoprotos.settings.TranslationSettings\x12@\n\x11passcode_settings\x18\x0e \x01(\x0b\x32%.pogoprotos.settings.PasscodeSettings\x12H\n\x15notification_settings\x18\x0f \x01(\x0b\x32).pogoprotos.settings.NotificationSettings\x12\x1c\n\x14\x63lient_app_blacklist\x18\x10 \x03(\t\x12L\n\x14\x63lient_perf_settings\x18\x11 \x01(\x0b\x32..pogoprotos.settings.ClientPerformanceSettings\x12\x45\n\x14news_global_settings\x18\x12 \x01(\x0b\x32\'.pogoprotos.settings.NewsGlobalSettings\x12G\n\x15quest_global_settings\x18\x13 \x01(\x0b\x32(.pogoprotos.settings.QuestGlobalSettings\x12I\n\x16\x62\x65luga_global_settings\x18\x14 \x01(\x0b\x32).pogoprotos.settings.BelugaGlobalSettings\x12O\n\x19telemetry_global_settings\x18\x15 \x01(\x0b\x32,.pogoprotos.settings.TelemetryGlobalSettings\x12:\n\x0elogin_settings\x18\x16 \x01(\x0b\x32\".pogoprotos.settings.LoginSettings\x12\x42\n\x0fsocial_settings\x18\x17 \x01(\x0b\x32).pogoprotos.settings.SocialClientSettings\x12K\n\x17trading_global_settings\x18\x18 \x01(\x0b\x32*.pogoprotos.settings.TradingGlobalSettings\x12\x43\n\x1e\x61\x64\x64itional_allowed_pokemon_ids\x18\x19 \x03(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12M\n\x18upsight_logging_settings\x18\x1a \x01(\x0b\x32+.pogoprotos.settings.UpsightLoggingSettings\x12I\n\x16\x63ombat_global_settings\x18\x1b \x01(\x0b\x32).pogoprotos.settings.CombatGlobalSettings\x12I\n\x13third_move_settings\x18\x1c \x01(\x0b\x32,.pogoprotos.settings.ThirdMoveGlobalSettings\x12\\\n combat_challenge_global_settings\x18\x1d \x01(\x0b\x32\x32.pogoprotos.settings.CombatChallengeGlobalSettings\x12Q\n\x16\x62gmode_global_settings\x18\x1e \x01(\x0b\x32\x31.pogoprotos.settings.BackgroundModeGlobalSettings\x12:\n\x0eprobe_settings\x18\x1f \x01(\x0b\x32\".pogoprotos.settings.ProbeSettings\x12P\n\x12purchased_settings\x18  \x01(\x0b\x32\x34.pogoprotos.settings.PokecoinPurchaseDisplaySettings\x12\x42\n\x12helpshift_settings\x18! \x01(\x0b\x32&.pogoprotos.settings.HelpshiftSettings\x12\x45\n\x11\x61r_photo_settings\x18\" \x01(\x0b\x32*.pogoprotos.settings.ArPhotoGlobalSettings\x12<\n\x0cpoi_settings\x18# \x01(\x0b\x32&.pogoprotos.settings.PoiGlobalSettings\x12\x44\n\x10pokemon_settings\x18$ \x01(\x0b\x32*.pogoprotos.settings.PokemonGlobalSettings\x12\x42\n\x0f\x61vatar_settings\x18% \x01(\x0b\x32).pogoprotos.settings.AvatarGlobalSettings\x12G\n\x15\x65volution_v2_settings\x18& \x01(\x0b\x32(.pogoprotos.settings.EvolutionV2Settings\x12:\n\x0ekoala_settings\x18( \x01(\x0b\x32\".pogoprotos.settings.KoalaSettingsb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_event__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_festival__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_fort__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_gps__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_inventory__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_level__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_map__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_news__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_notification__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_passcode__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_sfida__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_translation__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_client__performance__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_news__global__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_telemetry__global__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_login__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_quest__global__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_social__client__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_trading__global__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_upsight__logging__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_beluga__global__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_pokecoin__purchase__display__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_helpshift__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_combat__global__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_third__move__global__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_combat__challenge__global__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_poi__global__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_background__mode__global__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_probe__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_pokemon__global__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_ar__photo__global__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_avatar__global__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_evolution__v2__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_koala__settings__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GLOBALSETTINGS = _descriptor.Descriptor(
  name='GlobalSettings',
  full_name='pogoprotos.settings.GlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_settings', full_name='pogoprotos.settings.GlobalSettings.fort_settings', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_settings', full_name='pogoprotos.settings.GlobalSettings.map_settings', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_settings', full_name='pogoprotos.settings.GlobalSettings.level_settings', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_settings', full_name='pogoprotos.settings.GlobalSettings.inventory_settings', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minimum_client_version', full_name='pogoprotos.settings.GlobalSettings.minimum_client_version', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gps_settings', full_name='pogoprotos.settings.GlobalSettings.gps_settings', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='festival_settings', full_name='pogoprotos.settings.GlobalSettings.festival_settings', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_settings', full_name='pogoprotos.settings.GlobalSettings.event_settings', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_pokemon_types', full_name='pogoprotos.settings.GlobalSettings.max_pokemon_types', index=8,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sfida_settings', full_name='pogoprotos.settings.GlobalSettings.sfida_settings', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='news_settings', full_name='pogoprotos.settings.GlobalSettings.news_settings', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='translation_settings', full_name='pogoprotos.settings.GlobalSettings.translation_settings', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passcode_settings', full_name='pogoprotos.settings.GlobalSettings.passcode_settings', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notification_settings', full_name='pogoprotos.settings.GlobalSettings.notification_settings', index=13,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_app_blacklist', full_name='pogoprotos.settings.GlobalSettings.client_app_blacklist', index=14,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_perf_settings', full_name='pogoprotos.settings.GlobalSettings.client_perf_settings', index=15,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='news_global_settings', full_name='pogoprotos.settings.GlobalSettings.news_global_settings', index=16,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_global_settings', full_name='pogoprotos.settings.GlobalSettings.quest_global_settings', index=17,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beluga_global_settings', full_name='pogoprotos.settings.GlobalSettings.beluga_global_settings', index=18,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='telemetry_global_settings', full_name='pogoprotos.settings.GlobalSettings.telemetry_global_settings', index=19,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='login_settings', full_name='pogoprotos.settings.GlobalSettings.login_settings', index=20,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='social_settings', full_name='pogoprotos.settings.GlobalSettings.social_settings', index=21,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trading_global_settings', full_name='pogoprotos.settings.GlobalSettings.trading_global_settings', index=22,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_allowed_pokemon_ids', full_name='pogoprotos.settings.GlobalSettings.additional_allowed_pokemon_ids', index=23,
      number=25, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upsight_logging_settings', full_name='pogoprotos.settings.GlobalSettings.upsight_logging_settings', index=24,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_global_settings', full_name='pogoprotos.settings.GlobalSettings.combat_global_settings', index=25,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='third_move_settings', full_name='pogoprotos.settings.GlobalSettings.third_move_settings', index=26,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_challenge_global_settings', full_name='pogoprotos.settings.GlobalSettings.combat_challenge_global_settings', index=27,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bgmode_global_settings', full_name='pogoprotos.settings.GlobalSettings.bgmode_global_settings', index=28,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='probe_settings', full_name='pogoprotos.settings.GlobalSettings.probe_settings', index=29,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='purchased_settings', full_name='pogoprotos.settings.GlobalSettings.purchased_settings', index=30,
      number=32, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='helpshift_settings', full_name='pogoprotos.settings.GlobalSettings.helpshift_settings', index=31,
      number=33, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_photo_settings', full_name='pogoprotos.settings.GlobalSettings.ar_photo_settings', index=32,
      number=34, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='poi_settings', full_name='pogoprotos.settings.GlobalSettings.poi_settings', index=33,
      number=35, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_settings', full_name='pogoprotos.settings.GlobalSettings.pokemon_settings', index=34,
      number=36, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_settings', full_name='pogoprotos.settings.GlobalSettings.avatar_settings', index=35,
      number=37, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolution_v2_settings', full_name='pogoprotos.settings.GlobalSettings.evolution_v2_settings', index=36,
      number=38, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='koala_settings', full_name='pogoprotos.settings.GlobalSettings.koala_settings', index=37,
      number=40, type=11, cpp_type=10, label=1,
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
  serialized_start=1737,
  serialized_end=4268,
)

_GLOBALSETTINGS.fields_by_name['fort_settings'].message_type = pogoprotos_dot_settings_dot_fort__settings__pb2._FORTSETTINGS
_GLOBALSETTINGS.fields_by_name['map_settings'].message_type = pogoprotos_dot_settings_dot_map__settings__pb2._MAPSETTINGS
_GLOBALSETTINGS.fields_by_name['level_settings'].message_type = pogoprotos_dot_settings_dot_level__settings__pb2._LEVELSETTINGS
_GLOBALSETTINGS.fields_by_name['inventory_settings'].message_type = pogoprotos_dot_settings_dot_inventory__settings__pb2._INVENTORYSETTINGS
_GLOBALSETTINGS.fields_by_name['gps_settings'].message_type = pogoprotos_dot_settings_dot_gps__settings__pb2._GPSSETTINGS
_GLOBALSETTINGS.fields_by_name['festival_settings'].message_type = pogoprotos_dot_settings_dot_festival__settings__pb2._FESTIVALSETTINGS
_GLOBALSETTINGS.fields_by_name['event_settings'].message_type = pogoprotos_dot_settings_dot_event__settings__pb2._EVENTSETTINGS
_GLOBALSETTINGS.fields_by_name['sfida_settings'].message_type = pogoprotos_dot_settings_dot_sfida__settings__pb2._SFIDASETTINGS
_GLOBALSETTINGS.fields_by_name['news_settings'].message_type = pogoprotos_dot_settings_dot_news__settings__pb2._NEWSSETTINGS
_GLOBALSETTINGS.fields_by_name['translation_settings'].message_type = pogoprotos_dot_settings_dot_translation__settings__pb2._TRANSLATIONSETTINGS
_GLOBALSETTINGS.fields_by_name['passcode_settings'].message_type = pogoprotos_dot_settings_dot_passcode__settings__pb2._PASSCODESETTINGS
_GLOBALSETTINGS.fields_by_name['notification_settings'].message_type = pogoprotos_dot_settings_dot_notification__settings__pb2._NOTIFICATIONSETTINGS
_GLOBALSETTINGS.fields_by_name['client_perf_settings'].message_type = pogoprotos_dot_settings_dot_client__performance__settings__pb2._CLIENTPERFORMANCESETTINGS
_GLOBALSETTINGS.fields_by_name['news_global_settings'].message_type = pogoprotos_dot_settings_dot_news__global__settings__pb2._NEWSGLOBALSETTINGS
_GLOBALSETTINGS.fields_by_name['quest_global_settings'].message_type = pogoprotos_dot_settings_dot_quest__global__settings__pb2._QUESTGLOBALSETTINGS
_GLOBALSETTINGS.fields_by_name['beluga_global_settings'].message_type = pogoprotos_dot_settings_dot_beluga__global__settings__pb2._BELUGAGLOBALSETTINGS
_GLOBALSETTINGS.fields_by_name['telemetry_global_settings'].message_type = pogoprotos_dot_settings_dot_telemetry__global__settings__pb2._TELEMETRYGLOBALSETTINGS
_GLOBALSETTINGS.fields_by_name['login_settings'].message_type = pogoprotos_dot_settings_dot_login__settings__pb2._LOGINSETTINGS
_GLOBALSETTINGS.fields_by_name['social_settings'].message_type = pogoprotos_dot_settings_dot_social__client__settings__pb2._SOCIALCLIENTSETTINGS
_GLOBALSETTINGS.fields_by_name['trading_global_settings'].message_type = pogoprotos_dot_settings_dot_trading__global__settings__pb2._TRADINGGLOBALSETTINGS
_GLOBALSETTINGS.fields_by_name['additional_allowed_pokemon_ids'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_GLOBALSETTINGS.fields_by_name['upsight_logging_settings'].message_type = pogoprotos_dot_settings_dot_upsight__logging__settings__pb2._UPSIGHTLOGGINGSETTINGS
_GLOBALSETTINGS.fields_by_name['combat_global_settings'].message_type = pogoprotos_dot_settings_dot_combat__global__settings__pb2._COMBATGLOBALSETTINGS
_GLOBALSETTINGS.fields_by_name['third_move_settings'].message_type = pogoprotos_dot_settings_dot_third__move__global__settings__pb2._THIRDMOVEGLOBALSETTINGS
_GLOBALSETTINGS.fields_by_name['combat_challenge_global_settings'].message_type = pogoprotos_dot_settings_dot_combat__challenge__global__settings__pb2._COMBATCHALLENGEGLOBALSETTINGS
_GLOBALSETTINGS.fields_by_name['bgmode_global_settings'].message_type = pogoprotos_dot_settings_dot_background__mode__global__settings__pb2._BACKGROUNDMODEGLOBALSETTINGS
_GLOBALSETTINGS.fields_by_name['probe_settings'].message_type = pogoprotos_dot_settings_dot_probe__settings__pb2._PROBESETTINGS
_GLOBALSETTINGS.fields_by_name['purchased_settings'].message_type = pogoprotos_dot_settings_dot_pokecoin__purchase__display__settings__pb2._POKECOINPURCHASEDISPLAYSETTINGS
_GLOBALSETTINGS.fields_by_name['helpshift_settings'].message_type = pogoprotos_dot_settings_dot_helpshift__settings__pb2._HELPSHIFTSETTINGS
_GLOBALSETTINGS.fields_by_name['ar_photo_settings'].message_type = pogoprotos_dot_settings_dot_ar__photo__global__settings__pb2._ARPHOTOGLOBALSETTINGS
_GLOBALSETTINGS.fields_by_name['poi_settings'].message_type = pogoprotos_dot_settings_dot_poi__global__settings__pb2._POIGLOBALSETTINGS
_GLOBALSETTINGS.fields_by_name['pokemon_settings'].message_type = pogoprotos_dot_settings_dot_pokemon__global__settings__pb2._POKEMONGLOBALSETTINGS
_GLOBALSETTINGS.fields_by_name['avatar_settings'].message_type = pogoprotos_dot_settings_dot_avatar__global__settings__pb2._AVATARGLOBALSETTINGS
_GLOBALSETTINGS.fields_by_name['evolution_v2_settings'].message_type = pogoprotos_dot_settings_dot_evolution__v2__settings__pb2._EVOLUTIONV2SETTINGS
_GLOBALSETTINGS.fields_by_name['koala_settings'].message_type = pogoprotos_dot_settings_dot_koala__settings__pb2._KOALASETTINGS
DESCRIPTOR.message_types_by_name['GlobalSettings'] = _GLOBALSETTINGS

GlobalSettings = _reflection.GeneratedProtocolMessageType('GlobalSettings', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALSETTINGS,
  __module__ = 'pogoprotos.settings.global_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.GlobalSettings)
  ))
_sym_db.RegisterMessage(GlobalSettings)


# @@protoc_insertion_point(module_scope)
