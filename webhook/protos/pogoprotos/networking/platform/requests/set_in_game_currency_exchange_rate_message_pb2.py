# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/requests/set_in_game_currency_exchange_rate_message.proto

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
  name='pogoprotos/networking/platform/requests/set_in_game_currency_exchange_rate_message.proto',
  package='pogoprotos.networking.platform.requests',
  syntax='proto3',
  serialized_pb=_b('\nXpogoprotos/networking/platform/requests/set_in_game_currency_exchange_rate_message.proto\x12\'pogoprotos.networking.platform.requests\"\x87\x01\n$SetInGameCurrencyExchangeRateMessage\x12\x18\n\x10in_game_currency\x18\x01 \x01(\t\x12\x15\n\rfiat_currency\x18\x02 \x01(\t\x12.\n&fiat_currency_cost_e6_per_in_game_unit\x18\x03 \x01(\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SETINGAMECURRENCYEXCHANGERATEMESSAGE = _descriptor.Descriptor(
  name='SetInGameCurrencyExchangeRateMessage',
  full_name='pogoprotos.networking.platform.requests.SetInGameCurrencyExchangeRateMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='in_game_currency', full_name='pogoprotos.networking.platform.requests.SetInGameCurrencyExchangeRateMessage.in_game_currency', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fiat_currency', full_name='pogoprotos.networking.platform.requests.SetInGameCurrencyExchangeRateMessage.fiat_currency', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fiat_currency_cost_e6_per_in_game_unit', full_name='pogoprotos.networking.platform.requests.SetInGameCurrencyExchangeRateMessage.fiat_currency_cost_e6_per_in_game_unit', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=134,
  serialized_end=269,
)

DESCRIPTOR.message_types_by_name['SetInGameCurrencyExchangeRateMessage'] = _SETINGAMECURRENCYEXCHANGERATEMESSAGE

SetInGameCurrencyExchangeRateMessage = _reflection.GeneratedProtocolMessageType('SetInGameCurrencyExchangeRateMessage', (_message.Message,), dict(
  DESCRIPTOR = _SETINGAMECURRENCYEXCHANGERATEMESSAGE,
  __module__ = 'pogoprotos.networking.platform.requests.set_in_game_currency_exchange_rate_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.requests.SetInGameCurrencyExchangeRateMessage)
  ))
_sym_db.RegisterMessage(SetInGameCurrencyExchangeRateMessage)


# @@protoc_insertion_point(module_scope)
