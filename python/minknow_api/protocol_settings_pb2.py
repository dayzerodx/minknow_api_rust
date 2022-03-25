# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: minknow_api/protocol_settings.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from minknow_api import analysis_configuration_pb2 as minknow__api_dot_analysis__configuration__pb2
from minknow_api import rpc_options_pb2 as minknow__api_dot_rpc__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#minknow_api/protocol_settings.proto\x12\x1dminknow_api.protocol_settings\x1a(minknow_api/analysis_configuration.proto\x1a\x1dminknow_api/rpc_options.proto\"\x85\x02\n\x1cProtocolIdentifierComponents\x12V\n\x08location\x18\x01 \x01(\x0e\x32\x44.minknow_api.protocol_settings.ProtocolIdentifierComponents.Location\x12\x17\n\x0f\x65xperiment_type\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x1e\n\x16\x66low_cell_product_code\x18\x04 \x01(\t\x12\x0b\n\x03kit\x18\x05 \x01(\t\"9\n\x08Location\x12\x07\n\x03\x41NY\x10\x00\x12\x12\n\x0eSYSTEM_SCRIPTS\x10\x01\x12\x10\n\x0cUSER_SCRIPTS\x10\x02\"\xca\r\n\x0fProtocolSetting\x12I\n\x08\x63\x61tegory\x18\x01 \x01(\x0e\x32\x37.minknow_api.protocol_settings.ProtocolSetting.Category\x12\x18\n\nidentifier\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01\x12\x1a\n\x0c\x64isplay_name\x18\x03 \x01(\tB\x04\x88\xb5\x18\x01\x12\x0c\n\x04help\x18\x10 \x01(\t\x12\x41\n\x04unit\x18\x05 \x01(\x0e\x32\x33.minknow_api.protocol_settings.ProtocolSetting.Unit\x12Z\n\rdefault_value\x18\x06 \x01(\x0b\x32\x43.minknow_api.protocol_settings.ProtocolSetting.ProtocolSettingValue\x12N\n\x0b\x63onstraints\x18\x07 \x03(\x0b\x32\x39.minknow_api.protocol_settings.ProtocolSetting.Constraint\x12O\n\x0c\x64\x65pendencies\x18\x08 \x03(\x0b\x32\x39.minknow_api.protocol_settings.ProtocolSetting.Dependency\x12M\n\nvisibility\x18\t \x01(\x0e\x32\x39.minknow_api.protocol_settings.ProtocolSetting.Visibility\x12\x0f\n\x07\x63hoices\x18\x11 \x03(\t\x1a\x84\x03\n\x14ProtocolSettingValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x15\n\x0b\x66loat_value\x18\x02 \x01(\x01H\x00\x12\x17\n\rinteger_value\x18\x03 \x01(\x03H\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12\x66\n\x0e\x63hannels_value\x18\x05 \x01(\x0b\x32L.minknow_api.analysis_configuration.WriterConfiguration.ChannelConfigurationH\x00\x12m\n\x12multi_string_value\x18\x06 \x01(\x0b\x32O.minknow_api.protocol_settings.ProtocolSetting.ProtocolSettingValue.MultiStringH\x00\x1a\x1d\n\x0bMultiString\x12\x0e\n\x06values\x18\x01 \x03(\tB\x18\n\x16protocol_setting_value\x1a\xb9\x02\n\nConstraint\x12V\n\tcondition\x18\x01 \x01(\x0e\x32\x43.minknow_api.protocol_settings.ProtocolSetting.Constraint.Condition\x12R\n\x05value\x18\x02 \x01(\x0b\x32\x43.minknow_api.protocol_settings.ProtocolSetting.ProtocolSettingValue\"\x7f\n\tCondition\x12\t\n\x05\x45QUAL\x10\x00\x12\r\n\tNOT_EQUAL\x10\x01\x12\t\n\x05GT_EQ\x10\x02\x12\x06\n\x02GT\x10\x03\x12\t\n\x05LT_EQ\x10\x04\x12\x06\n\x02LT\x10\x05\x12\x06\n\x02IN\x10\x06\x12\n\n\x06NOT_IN\x10\x07\x12\r\n\tENDS_WITH\x10\x08\x12\x0f\n\x0bSTARTS_WITH\x10\t\x1ap\n\nDependency\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12N\n\x0b\x63onstraints\x18\x02 \x03(\x0b\x32\x39.minknow_api.protocol_settings.ProtocolSetting.Constraint\"C\n\x08\x43\x61tegory\x12\t\n\x05OTHER\x10\x00\x12\x0f\n\x0bRUN_OPTIONS\x10\x01\x12\x0f\n\x0b\x42\x41SECALLING\x10\x02\x12\n\n\x06OUTPUT\x10\x03\"\xcc\x01\n\x04Unit\x12\x0c\n\x08UNITLESS\x10\x00\x12\x0f\n\x0bUTF8_STRING\x10\x01\x12\x10\n\x0c\x41SCII_STRING\x10\x02\x12\x08\n\x04PATH\x10\x03\x12\x07\n\x03URL\x10\x04\x12\x12\n\x0ePRIVATE_STRING\x10\x05\x12\n\n\x06\x43HOICE\x10\x06\x12\x10\n\x0cMULTI_CHOICE\x10\x07\x12\n\n\x06SECOND\x10\x08\x12\x08\n\x04HOUR\x10\t\x12\x08\n\x04\x42\x41SE\x10\n\x12\t\n\x05KBASE\x10\x0b\x12\t\n\x05MBASE\x10\x0c\x12\t\n\x05GBASE\x10\r\x12\r\n\tMILLIVOLT\x10\x0e\"?\n\nVisibility\x12\x0c\n\x08\x45\x44ITABLE\x10\x00\x12\n\n\x06HIDDEN\x10\x01\x12\t\n\x05\x46IXED\x10\x02\x12\x0c\n\x08REQUIRED\x10\x03\x42&\n\x1c\x63om.nanoporetech.minknow_api\xa2\x02\x05MKAPIb\x06proto3')



_PROTOCOLIDENTIFIERCOMPONENTS = DESCRIPTOR.message_types_by_name['ProtocolIdentifierComponents']
_PROTOCOLSETTING = DESCRIPTOR.message_types_by_name['ProtocolSetting']
_PROTOCOLSETTING_PROTOCOLSETTINGVALUE = _PROTOCOLSETTING.nested_types_by_name['ProtocolSettingValue']
_PROTOCOLSETTING_PROTOCOLSETTINGVALUE_MULTISTRING = _PROTOCOLSETTING_PROTOCOLSETTINGVALUE.nested_types_by_name['MultiString']
_PROTOCOLSETTING_CONSTRAINT = _PROTOCOLSETTING.nested_types_by_name['Constraint']
_PROTOCOLSETTING_DEPENDENCY = _PROTOCOLSETTING.nested_types_by_name['Dependency']
_PROTOCOLIDENTIFIERCOMPONENTS_LOCATION = _PROTOCOLIDENTIFIERCOMPONENTS.enum_types_by_name['Location']
_PROTOCOLSETTING_CONSTRAINT_CONDITION = _PROTOCOLSETTING_CONSTRAINT.enum_types_by_name['Condition']
_PROTOCOLSETTING_CATEGORY = _PROTOCOLSETTING.enum_types_by_name['Category']
_PROTOCOLSETTING_UNIT = _PROTOCOLSETTING.enum_types_by_name['Unit']
_PROTOCOLSETTING_VISIBILITY = _PROTOCOLSETTING.enum_types_by_name['Visibility']
ProtocolIdentifierComponents = _reflection.GeneratedProtocolMessageType('ProtocolIdentifierComponents', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCOLIDENTIFIERCOMPONENTS,
  '__module__' : 'minknow_api.protocol_settings_pb2'
  ,
  '__doc__': """Attributes:
      location:
          If not specified, will default to "ANY"
      experiment_type:
          one of "custom", "sequencing", "control", "ctc", "platform qc"
          or "flowcell_plugin"
      name:
          Name (or path) of the protocol, without the .toml extension
          eg: "sequencing/sequencing_MIN106_DNA" this is relative to the
          system or user protocol directory
      flow_cell_product_code:
          eg: "FLO-MIN106"
      kit:
          eg: "SQK-RPB004"
  """,
  # @@protoc_insertion_point(class_scope:minknow_api.protocol_settings.ProtocolIdentifierComponents)
  })
_sym_db.RegisterMessage(ProtocolIdentifierComponents)

ProtocolSetting = _reflection.GeneratedProtocolMessageType('ProtocolSetting', (_message.Message,), {

  'ProtocolSettingValue' : _reflection.GeneratedProtocolMessageType('ProtocolSettingValue', (_message.Message,), {

    'MultiString' : _reflection.GeneratedProtocolMessageType('MultiString', (_message.Message,), {
      'DESCRIPTOR' : _PROTOCOLSETTING_PROTOCOLSETTINGVALUE_MULTISTRING,
      '__module__' : 'minknow_api.protocol_settings_pb2'
      # @@protoc_insertion_point(class_scope:minknow_api.protocol_settings.ProtocolSetting.ProtocolSettingValue.MultiString)
      })
    ,
    'DESCRIPTOR' : _PROTOCOLSETTING_PROTOCOLSETTINGVALUE,
    '__module__' : 'minknow_api.protocol_settings_pb2'
    # @@protoc_insertion_point(class_scope:minknow_api.protocol_settings.ProtocolSetting.ProtocolSettingValue)
    })
  ,

  'Constraint' : _reflection.GeneratedProtocolMessageType('Constraint', (_message.Message,), {
    'DESCRIPTOR' : _PROTOCOLSETTING_CONSTRAINT,
    '__module__' : 'minknow_api.protocol_settings_pb2'
    # @@protoc_insertion_point(class_scope:minknow_api.protocol_settings.ProtocolSetting.Constraint)
    })
  ,

  'Dependency' : _reflection.GeneratedProtocolMessageType('Dependency', (_message.Message,), {
    'DESCRIPTOR' : _PROTOCOLSETTING_DEPENDENCY,
    '__module__' : 'minknow_api.protocol_settings_pb2'
    # @@protoc_insertion_point(class_scope:minknow_api.protocol_settings.ProtocolSetting.Dependency)
    })
  ,
  'DESCRIPTOR' : _PROTOCOLSETTING,
  '__module__' : 'minknow_api.protocol_settings_pb2'
  ,
  '__doc__': """Attributes:
      identifier:
          Identifier is the unique primary-key for referring to
          protocol-settings, dependencies refer to other settings via
          their identifier.
      help:
          Optional additional help text for a setting that may be shown
          to the user if required.
      constraints:
          All constraints must be met if this setting is to be
          considered valid
      dependencies:
          If any of the dependencies matches it's constraints, this
          setting should adopt the level of visibility specified in
          "visibility". If none of the dependencies match their
          constraints, then "visibility" should be ignored and the
          option should be hidden from the user.  Some dependencies may
          be specified multiple times, but with mutually exclusive
          constraints, for example if the setting controls data
          compression level, where there is a compression_algorithm
          setting specified by a string that can have the values "X",
          "Y" or "None". The setting may be dependent on
          compression_algorithm equals "X" or compression_algorithm
          equals "Y". If the compression_algorithm is "None" then none
          of the dependency constraints will be met and the setting
          should be hidden. A typical arrangement of fields in this case
          would be: Dependency {   identifier: "compression_algorithm",
          Constraint {     condition : EQUAL,     value: "X"   } }
          Dependency {   identifier: "compression_algorithm",
          Constraint {     condition : EQUAL,     value: "Y"   } } When
          a dependency is specified with multiple constraints they must
          all be met before the dependency is considered satisfied, for
          example some other setting may be dependent on
          compression_level being in a range (0,10] :  Dependency {
          identifier: "compression_level",   Constraint {     condition
          : GT,     value: 0   },   Constraint {     condition : LT_EQ,
          value: 10   } }
      visibility:
          If any of the dependencies match their constraints, this level
          of visibility should be adopted. It should also be adopted if
          no dependencies are specified.
      choices:
          when unit is CHOICE, this defines the acceptable choices.
  """,
  # @@protoc_insertion_point(class_scope:minknow_api.protocol_settings.ProtocolSetting)
  })
_sym_db.RegisterMessage(ProtocolSetting)
_sym_db.RegisterMessage(ProtocolSetting.ProtocolSettingValue)
_sym_db.RegisterMessage(ProtocolSetting.ProtocolSettingValue.MultiString)
_sym_db.RegisterMessage(ProtocolSetting.Constraint)
_sym_db.RegisterMessage(ProtocolSetting.Dependency)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.nanoporetech.minknow_api\242\002\005MKAPI'
  _PROTOCOLSETTING.fields_by_name['identifier']._options = None
  _PROTOCOLSETTING.fields_by_name['identifier']._serialized_options = b'\210\265\030\001'
  _PROTOCOLSETTING.fields_by_name['display_name']._options = None
  _PROTOCOLSETTING.fields_by_name['display_name']._serialized_options = b'\210\265\030\001'
  _PROTOCOLIDENTIFIERCOMPONENTS._serialized_start=144
  _PROTOCOLIDENTIFIERCOMPONENTS._serialized_end=405
  _PROTOCOLIDENTIFIERCOMPONENTS_LOCATION._serialized_start=348
  _PROTOCOLIDENTIFIERCOMPONENTS_LOCATION._serialized_end=405
  _PROTOCOLSETTING._serialized_start=408
  _PROTOCOLSETTING._serialized_end=2146
  _PROTOCOLSETTING_PROTOCOLSETTINGVALUE._serialized_start=987
  _PROTOCOLSETTING_PROTOCOLSETTINGVALUE._serialized_end=1375
  _PROTOCOLSETTING_PROTOCOLSETTINGVALUE_MULTISTRING._serialized_start=1320
  _PROTOCOLSETTING_PROTOCOLSETTINGVALUE_MULTISTRING._serialized_end=1349
  _PROTOCOLSETTING_CONSTRAINT._serialized_start=1378
  _PROTOCOLSETTING_CONSTRAINT._serialized_end=1691
  _PROTOCOLSETTING_CONSTRAINT_CONDITION._serialized_start=1564
  _PROTOCOLSETTING_CONSTRAINT_CONDITION._serialized_end=1691
  _PROTOCOLSETTING_DEPENDENCY._serialized_start=1693
  _PROTOCOLSETTING_DEPENDENCY._serialized_end=1805
  _PROTOCOLSETTING_CATEGORY._serialized_start=1807
  _PROTOCOLSETTING_CATEGORY._serialized_end=1874
  _PROTOCOLSETTING_UNIT._serialized_start=1877
  _PROTOCOLSETTING_UNIT._serialized_end=2081
  _PROTOCOLSETTING_VISIBILITY._serialized_start=2083
  _PROTOCOLSETTING_VISIBILITY._serialized_end=2146
# @@protoc_insertion_point(module_scope)
