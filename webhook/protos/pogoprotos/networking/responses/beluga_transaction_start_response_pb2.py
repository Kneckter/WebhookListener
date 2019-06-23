# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/beluga_transaction_start_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.beluga import beluga_ble_transfer_prep_pb2 as pogoprotos_dot_data_dot_beluga_dot_beluga__ble__transfer__prep__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/beluga_transaction_start_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nGpogoprotos/networking/responses/beluga_transaction_start_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x35pogoprotos/data/beluga/beluga_ble_transfer_prep.proto\"\xf2\x03\n\x1e\x42\x65lugaTransactionStartResponse\x12V\n\x06status\x18\x01 \x01(\x0e\x32\x46.pogoprotos.networking.responses.BelugaTransactionStartResponse.Status\x12K\n\x14\x62\x65luga_transfer_prep\x18\x02 \x01(\x0b\x32-.pogoprotos.data.beluga.BelugaBleTransferPrep\x12\x18\n\x10server_signature\x18\x03 \x01(\x0c\"\x90\x02\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x12\x1c\n\x18\x45RROR_INVALID_POKEMON_ID\x10\x03\x12\x1a\n\x16\x45RROR_POKEMON_DEPLOYED\x10\x04\x12\x18\n\x14\x45RROR_POKEMON_IS_EGG\x10\x05\x12\x1a\n\x16\x45RROR_POKEMON_IS_BUDDY\x10\x06\x12\x1d\n\x19\x45RROR_POKEMON_NOT_ALLOWED\x10\x07\x12\x17\n\x13\x45RROR_INVALID_NONCE\x10\x08\x12\x1a\n\x16\x45RROR_TOO_MANY_POKEMON\x10\t\x12\x1e\n\x1a\x45RROR_NO_POKEMON_SPECIFIED\x10\nb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_beluga_dot_beluga__ble__transfer__prep__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_BELUGATRANSACTIONSTARTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.BelugaTransactionStartResponse.Status',
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
      name='FAILED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_POKEMON_ID', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_DEPLOYED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_IS_EGG', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_IS_BUDDY', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_NOT_ALLOWED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_NONCE', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_TOO_MANY_POKEMON', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NO_POKEMON_SPECIFIED', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=390,
  serialized_end=662,
)
_sym_db.RegisterEnumDescriptor(_BELUGATRANSACTIONSTARTRESPONSE_STATUS)


_BELUGATRANSACTIONSTARTRESPONSE = _descriptor.Descriptor(
  name='BelugaTransactionStartResponse',
  full_name='pogoprotos.networking.responses.BelugaTransactionStartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.BelugaTransactionStartResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beluga_transfer_prep', full_name='pogoprotos.networking.responses.BelugaTransactionStartResponse.beluga_transfer_prep', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_signature', full_name='pogoprotos.networking.responses.BelugaTransactionStartResponse.server_signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BELUGATRANSACTIONSTARTRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=662,
)

_BELUGATRANSACTIONSTARTRESPONSE.fields_by_name['status'].enum_type = _BELUGATRANSACTIONSTARTRESPONSE_STATUS
_BELUGATRANSACTIONSTARTRESPONSE.fields_by_name['beluga_transfer_prep'].message_type = pogoprotos_dot_data_dot_beluga_dot_beluga__ble__transfer__prep__pb2._BELUGABLETRANSFERPREP
_BELUGATRANSACTIONSTARTRESPONSE_STATUS.containing_type = _BELUGATRANSACTIONSTARTRESPONSE
DESCRIPTOR.message_types_by_name['BelugaTransactionStartResponse'] = _BELUGATRANSACTIONSTARTRESPONSE

BelugaTransactionStartResponse = _reflection.GeneratedProtocolMessageType('BelugaTransactionStartResponse', (_message.Message,), dict(
  DESCRIPTOR = _BELUGATRANSACTIONSTARTRESPONSE,
  __module__ = 'pogoprotos.networking.responses.beluga_transaction_start_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.BelugaTransactionStartResponse)
  ))
_sym_db.RegisterMessage(BelugaTransactionStartResponse)


# @@protoc_insertion_point(module_scope)
