# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/set_favorite_pokemon_message.proto

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
  name='pogoprotos/networking/requests/messages/set_favorite_pokemon_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nJpogoprotos/networking/requests/messages/set_favorite_pokemon_message.proto\x12\'pogoprotos.networking.requests.messages\"D\n\x19SetFavoritePokemonMessage\x12\x12\n\npokemon_id\x18\x01 \x01(\x03\x12\x13\n\x0bis_favorite\x18\x02 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SETFAVORITEPOKEMONMESSAGE = _descriptor.Descriptor(
  name='SetFavoritePokemonMessage',
  full_name='pogoprotos.networking.requests.messages.SetFavoritePokemonMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.networking.requests.messages.SetFavoritePokemonMessage.pokemon_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_favorite', full_name='pogoprotos.networking.requests.messages.SetFavoritePokemonMessage.is_favorite', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=119,
  serialized_end=187,
)

DESCRIPTOR.message_types_by_name['SetFavoritePokemonMessage'] = _SETFAVORITEPOKEMONMESSAGE

SetFavoritePokemonMessage = _reflection.GeneratedProtocolMessageType('SetFavoritePokemonMessage', (_message.Message,), dict(
  DESCRIPTOR = _SETFAVORITEPOKEMONMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.set_favorite_pokemon_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.SetFavoritePokemonMessage)
  ))
_sym_db.RegisterMessage(SetFavoritePokemonMessage)


# @@protoc_insertion_point(module_scope)
