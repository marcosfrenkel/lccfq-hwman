# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: hwman/grpc/protobufs/health.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'hwman/grpc/protobufs/health.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!hwman/grpc/protobufs/health.proto\"\x17\n\x04Ping\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x0cPingResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x0f\n\rHealthRequest\"P\n\x18InstrumentServerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x12\n\nis_running\x18\x03 \x01(\x08\x32\xc2\x03\n\x06Health\x12 \n\x08TestPing\x12\x05.Ping\x1a\r.PingResponse\x12\x42\n\x15StartInstrumentServer\x12\x0e.HealthRequest\x1a\x19.InstrumentServerResponse\x12\x41\n\x14StopInstrumentServer\x12\x0e.HealthRequest\x1a\x19.InstrumentServerResponse\x12\x46\n\x19GetInstrumentServerStatus\x12\x0e.HealthRequest\x1a\x19.InstrumentServerResponse\x12@\n\x13StartPyroNameserver\x12\x0e.HealthRequest\x1a\x19.InstrumentServerResponse\x12?\n\x12StopPyroNameserver\x12\x0e.HealthRequest\x1a\x19.InstrumentServerResponse\x12\x44\n\x17GetPyroNameserverStatus\x12\x0e.HealthRequest\x1a\x19.InstrumentServerResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hwman.grpc.protobufs.health_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PING']._serialized_start=37
  _globals['_PING']._serialized_end=60
  _globals['_PINGRESPONSE']._serialized_start=62
  _globals['_PINGRESPONSE']._serialized_end=93
  _globals['_HEALTHREQUEST']._serialized_start=95
  _globals['_HEALTHREQUEST']._serialized_end=110
  _globals['_INSTRUMENTSERVERRESPONSE']._serialized_start=112
  _globals['_INSTRUMENTSERVERRESPONSE']._serialized_end=192
  _globals['_HEALTH']._serialized_start=195
  _globals['_HEALTH']._serialized_end=645
# @@protoc_insertion_point(module_scope)
