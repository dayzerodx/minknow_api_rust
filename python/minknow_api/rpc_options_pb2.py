# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: minknow_api/rpc_options.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dminknow_api/rpc_options.proto\x12\x0bminknow_api\x1a google/protobuf/descriptor.proto:5\n\x0crpc_required\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\x08:3\n\nrpc_unwrap\x12\x1d.google.protobuf.FieldOptions\x18\xd2\x86\x03 \x01(\x08:6\n\x0c\x65xperimental\x12\x1e.google.protobuf.MethodOptions\x18\xd3\x86\x03 \x01(\x08\x42&\n\x1c\x63om.nanoporetech.minknow_api\xa2\x02\x05MKAPIb\x06proto3')


RPC_REQUIRED_FIELD_NUMBER = 50001
rpc_required = DESCRIPTOR.extensions_by_name['rpc_required']
RPC_UNWRAP_FIELD_NUMBER = 50002
rpc_unwrap = DESCRIPTOR.extensions_by_name['rpc_unwrap']
EXPERIMENTAL_FIELD_NUMBER = 50003
experimental = DESCRIPTOR.extensions_by_name['experimental']

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(rpc_required)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(rpc_unwrap)
  google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(experimental)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.nanoporetech.minknow_api\242\002\005MKAPI'
# @@protoc_insertion_point(module_scope)
