# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/complete_quest_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.quests import client_quest_pb2 as pogoprotos_dot_data_dot_quests_dot_client__quest__pb2
from pogoprotos.data.quests import quest_stamp_pb2 as pogoprotos_dot_data_dot_quests_dot_quest__stamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/complete_quest_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n=pogoprotos/networking/responses/complete_quest_response.proto\x12\x1fpogoprotos.networking.responses\x1a)pogoprotos/data/quests/client_quest.proto\x1a(pogoprotos/data/quests/quest_stamp.proto\"\xd6\x04\n\x15\x43ompleteQuestResponse\x12M\n\x06status\x18\x01 \x01(\x0e\x32=.pogoprotos.networking.responses.CompleteQuestResponse.Status\x12\x32\n\x05quest\x18\x02 \x01(\x0b\x32#.pogoprotos.data.quests.ClientQuest\x12\x31\n\x05stamp\x18\x03 \x03(\x0b\x32\".pogoprotos.data.quests.QuestStamp\"\x86\x03\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x19\n\x15\x45RROR_QUEST_NOT_FOUND\x10\x02\x12!\n\x1d\x45RROR_QUEST_STILL_IN_PROGRESS\x10\x03\x12!\n\x1d\x45RROR_QUEST_ALREADY_COMPLETED\x10\x04\x12\x1c\n\x18\x45RROR_SUBQUEST_NOT_FOUND\x10\x05\x12$\n ERROR_SUBQUEST_STILL_IN_PROGRESS\x10\x06\x12$\n ERROR_SUBQUEST_ALREADY_COMPLETED\x10\x07\x12%\n!ERROR_MULTIPART_STILL_IN_PROGRESS\x10\x08\x12%\n!ERROR_MULTIPART_ALREADY_COMPLETED\x10\t\x12\x31\n-ERROR_REDEEM_COMPLETED_QUEST_STAMP_CARD_FIRST\x10\n\x12\x18\n\x14\x45RROR_INVENTORY_FULL\x10\x0b\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_quests_dot_client__quest__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_quest__stamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_COMPLETEQUESTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.CompleteQuestResponse.Status',
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
      name='ERROR_QUEST_NOT_FOUND', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_QUEST_STILL_IN_PROGRESS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_QUEST_ALREADY_COMPLETED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_SUBQUEST_NOT_FOUND', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_SUBQUEST_STILL_IN_PROGRESS', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_SUBQUEST_ALREADY_COMPLETED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_MULTIPART_STILL_IN_PROGRESS', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_MULTIPART_ALREADY_COMPLETED', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_REDEEM_COMPLETED_QUEST_STAMP_CARD_FIRST', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVENTORY_FULL', index=11, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=392,
  serialized_end=782,
)
_sym_db.RegisterEnumDescriptor(_COMPLETEQUESTRESPONSE_STATUS)


_COMPLETEQUESTRESPONSE = _descriptor.Descriptor(
  name='CompleteQuestResponse',
  full_name='pogoprotos.networking.responses.CompleteQuestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.CompleteQuestResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest', full_name='pogoprotos.networking.responses.CompleteQuestResponse.quest', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamp', full_name='pogoprotos.networking.responses.CompleteQuestResponse.stamp', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMPLETEQUESTRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=782,
)

_COMPLETEQUESTRESPONSE.fields_by_name['status'].enum_type = _COMPLETEQUESTRESPONSE_STATUS
_COMPLETEQUESTRESPONSE.fields_by_name['quest'].message_type = pogoprotos_dot_data_dot_quests_dot_client__quest__pb2._CLIENTQUEST
_COMPLETEQUESTRESPONSE.fields_by_name['stamp'].message_type = pogoprotos_dot_data_dot_quests_dot_quest__stamp__pb2._QUESTSTAMP
_COMPLETEQUESTRESPONSE_STATUS.containing_type = _COMPLETEQUESTRESPONSE
DESCRIPTOR.message_types_by_name['CompleteQuestResponse'] = _COMPLETEQUESTRESPONSE

CompleteQuestResponse = _reflection.GeneratedProtocolMessageType('CompleteQuestResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMPLETEQUESTRESPONSE,
  __module__ = 'pogoprotos.networking.responses.complete_quest_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.CompleteQuestResponse)
  ))
_sym_db.RegisterMessage(CompleteQuestResponse)


# @@protoc_insertion_point(module_scope)
