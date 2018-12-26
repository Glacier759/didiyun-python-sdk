# coding: utf-8 
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: compute/v1/snap.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base.v1 import base_pb2 as base_dot_v1_dot_base__pb2
from compute.v1 import common_pb2 as compute_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='compute/v1/snap.proto',
  package='didi.cloud.compute.v1',
  syntax='proto3',
  serialized_options=_b('\n\026com.didiyun.compute.v1P\001Z4github.com/didiyun/didiyun-go-sdk/compute/v1;compute\370\001\001\252\002\027Didi.Dicloud.Compute.V1\312\002\027Didi\\Dicloud\\Compute\\V1'),
  serialized_pb=_b('\n\x15\x63ompute/v1/snap.proto\x12\x15\x64idi.cloud.compute.v1\x1a\x12\x62\x61se/v1/base.proto\x1a\x17\x63ompute/v1/common.proto\"\xb2\x01\n\x13ListSnapshotRequest\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.didi.cloud.base.v1.Header\x12\r\n\x05start\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\x12\x10\n\x08simplify\x18\x04 \x01(\x08\x12?\n\tcondition\x18\x05 \x01(\x0b\x32,.didi.cloud.compute.v1.ListSnapshotCondition\":\n\x15ListSnapshotCondition\x12\x0f\n\x07\x65\x62sUuid\x18\x01 \x01(\t\x12\x10\n\x08snapName\x18\x02 \x01(\t\"o\n\x14ListSnapshotResponse\x12(\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x19.didi.cloud.base.v1.Error\x12-\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x1f.didi.cloud.compute.v1.SnapInfo\"k\n\x1aGetSnapshotTotalCntRequest\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.didi.cloud.base.v1.Header\x12\x0f\n\x07\x65\x62sUuid\x18\x02 \x01(\t\x12\x10\n\x08snapName\x18\x03 \x01(\t\"z\n\x1bGetSnapshotTotalCntResponse\x12(\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x19.didi.cloud.base.v1.Error\x12\x31\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32#.didi.cloud.compute.v1.TotalCntInfo\"w\n\x15\x43reateSnapshotRequest\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.didi.cloud.base.v1.Header\x12\x0f\n\x07\x64\x63\x32Uuid\x18\x02 \x01(\t\x12\x0f\n\x07\x65\x62sUuid\x18\x03 \x01(\t\x12\x10\n\x08snapName\x18\x04 \x01(\t\"m\n\x16\x43reateSnapshotResponse\x12(\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x19.didi.cloud.base.v1.Error\x12)\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x1b.didi.cloud.base.v1.JobInfo\"\xa0\x01\n\x15\x44\x65leteSnapshotRequest\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.didi.cloud.base.v1.Header\x12@\n\x04snap\x18\x02 \x03(\x0b\x32\x32.didi.cloud.compute.v1.DeleteSnapshotRequest.Input\x1a\x19\n\x05Input\x12\x10\n\x08snapUuid\x18\x01 \x01(\t\"m\n\x16\x44\x65leteSnapshotResponse\x12(\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x19.didi.cloud.base.v1.Error\x12)\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x1b.didi.cloud.base.v1.JobInfo\"\xc3\x01\n\x15RevertSnapshotRequest\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.didi.cloud.base.v1.Header\x12@\n\x04snap\x18\x02 \x03(\x0b\x32\x32.didi.cloud.compute.v1.RevertSnapshotRequest.Input\x12\x0f\n\x07stopDc2\x18\x03 \x01(\x08\x12\x10\n\x08startDc2\x18\x04 \x01(\x08\x1a\x19\n\x05Input\x12\x10\n\x08snapUuid\x18\x01 \x01(\t\"m\n\x16RevertSnapshotResponse\x12(\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x19.didi.cloud.base.v1.Error\x12)\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x1b.didi.cloud.base.v1.JobInfo\"\xd9\x01\n\x19\x43hangeSnapshotNameRequest\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.didi.cloud.base.v1.Header\x12\x44\n\x04snap\x18\x02 \x03(\x0b\x32\x36.didi.cloud.compute.v1.ChangeSnapshotNameRequest.Input\x12\x0f\n\x07stopDc2\x18\x03 \x01(\x08\x12\x10\n\x08startDc2\x18\x04 \x01(\x08\x1a\'\n\x05Input\x12\x10\n\x08snapUuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"q\n\x1a\x43hangeSnapshotNameResponse\x12(\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x19.didi.cloud.base.v1.Error\x12)\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x1b.didi.cloud.base.v1.JobInfo2\xc1\x05\n\x04Snap\x12i\n\x0cListSnapshot\x12*.didi.cloud.compute.v1.ListSnapshotRequest\x1a+.didi.cloud.compute.v1.ListSnapshotResponse\"\x00\x12~\n\x13GetSnapshotTotalCnt\x12\x31.didi.cloud.compute.v1.GetSnapshotTotalCntRequest\x1a\x32.didi.cloud.compute.v1.GetSnapshotTotalCntResponse\"\x00\x12o\n\x0e\x43reateSnapshot\x12,.didi.cloud.compute.v1.CreateSnapshotRequest\x1a-.didi.cloud.compute.v1.CreateSnapshotResponse\"\x00\x12o\n\x0e\x44\x65leteSnapshot\x12,.didi.cloud.compute.v1.DeleteSnapshotRequest\x1a-.didi.cloud.compute.v1.DeleteSnapshotResponse\"\x00\x12o\n\x0eRevertSnapshot\x12,.didi.cloud.compute.v1.RevertSnapshotRequest\x1a-.didi.cloud.compute.v1.RevertSnapshotResponse\"\x00\x12{\n\x12\x43hangeSnapshotName\x12\x30.didi.cloud.compute.v1.ChangeSnapshotNameRequest\x1a\x31.didi.cloud.compute.v1.ChangeSnapshotNameResponse\"\x00\x42\x87\x01\n\x16\x63om.didiyun.compute.v1P\x01Z4github.com/didiyun/didiyun-go-sdk/compute/v1;compute\xf8\x01\x01\xaa\x02\x17\x44idi.Dicloud.Compute.V1\xca\x02\x17\x44idi\\Dicloud\\Compute\\V1b\x06proto3')
  ,
  dependencies=[base_dot_v1_dot_base__pb2.DESCRIPTOR,compute_dot_v1_dot_common__pb2.DESCRIPTOR,])




_LISTSNAPSHOTREQUEST = _descriptor.Descriptor(
  name='ListSnapshotRequest',
  full_name='didi.cloud.compute.v1.ListSnapshotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='didi.cloud.compute.v1.ListSnapshotRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='didi.cloud.compute.v1.ListSnapshotRequest.start', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='didi.cloud.compute.v1.ListSnapshotRequest.limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='simplify', full_name='didi.cloud.compute.v1.ListSnapshotRequest.simplify', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='condition', full_name='didi.cloud.compute.v1.ListSnapshotRequest.condition', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=272,
)


_LISTSNAPSHOTCONDITION = _descriptor.Descriptor(
  name='ListSnapshotCondition',
  full_name='didi.cloud.compute.v1.ListSnapshotCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ebsUuid', full_name='didi.cloud.compute.v1.ListSnapshotCondition.ebsUuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snapName', full_name='didi.cloud.compute.v1.ListSnapshotCondition.snapName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=274,
  serialized_end=332,
)


_LISTSNAPSHOTRESPONSE = _descriptor.Descriptor(
  name='ListSnapshotResponse',
  full_name='didi.cloud.compute.v1.ListSnapshotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='didi.cloud.compute.v1.ListSnapshotResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='didi.cloud.compute.v1.ListSnapshotResponse.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=445,
)


_GETSNAPSHOTTOTALCNTREQUEST = _descriptor.Descriptor(
  name='GetSnapshotTotalCntRequest',
  full_name='didi.cloud.compute.v1.GetSnapshotTotalCntRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='didi.cloud.compute.v1.GetSnapshotTotalCntRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ebsUuid', full_name='didi.cloud.compute.v1.GetSnapshotTotalCntRequest.ebsUuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snapName', full_name='didi.cloud.compute.v1.GetSnapshotTotalCntRequest.snapName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=554,
)


_GETSNAPSHOTTOTALCNTRESPONSE = _descriptor.Descriptor(
  name='GetSnapshotTotalCntResponse',
  full_name='didi.cloud.compute.v1.GetSnapshotTotalCntResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='didi.cloud.compute.v1.GetSnapshotTotalCntResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='didi.cloud.compute.v1.GetSnapshotTotalCntResponse.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=556,
  serialized_end=678,
)


_CREATESNAPSHOTREQUEST = _descriptor.Descriptor(
  name='CreateSnapshotRequest',
  full_name='didi.cloud.compute.v1.CreateSnapshotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='didi.cloud.compute.v1.CreateSnapshotRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dc2Uuid', full_name='didi.cloud.compute.v1.CreateSnapshotRequest.dc2Uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ebsUuid', full_name='didi.cloud.compute.v1.CreateSnapshotRequest.ebsUuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snapName', full_name='didi.cloud.compute.v1.CreateSnapshotRequest.snapName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=680,
  serialized_end=799,
)


_CREATESNAPSHOTRESPONSE = _descriptor.Descriptor(
  name='CreateSnapshotResponse',
  full_name='didi.cloud.compute.v1.CreateSnapshotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='didi.cloud.compute.v1.CreateSnapshotResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='didi.cloud.compute.v1.CreateSnapshotResponse.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=801,
  serialized_end=910,
)


_DELETESNAPSHOTREQUEST_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='didi.cloud.compute.v1.DeleteSnapshotRequest.Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapUuid', full_name='didi.cloud.compute.v1.DeleteSnapshotRequest.Input.snapUuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1048,
  serialized_end=1073,
)

_DELETESNAPSHOTREQUEST = _descriptor.Descriptor(
  name='DeleteSnapshotRequest',
  full_name='didi.cloud.compute.v1.DeleteSnapshotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='didi.cloud.compute.v1.DeleteSnapshotRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snap', full_name='didi.cloud.compute.v1.DeleteSnapshotRequest.snap', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DELETESNAPSHOTREQUEST_INPUT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=913,
  serialized_end=1073,
)


_DELETESNAPSHOTRESPONSE = _descriptor.Descriptor(
  name='DeleteSnapshotResponse',
  full_name='didi.cloud.compute.v1.DeleteSnapshotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='didi.cloud.compute.v1.DeleteSnapshotResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='didi.cloud.compute.v1.DeleteSnapshotResponse.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1075,
  serialized_end=1184,
)


_REVERTSNAPSHOTREQUEST_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='didi.cloud.compute.v1.RevertSnapshotRequest.Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapUuid', full_name='didi.cloud.compute.v1.RevertSnapshotRequest.Input.snapUuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1048,
  serialized_end=1073,
)

_REVERTSNAPSHOTREQUEST = _descriptor.Descriptor(
  name='RevertSnapshotRequest',
  full_name='didi.cloud.compute.v1.RevertSnapshotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='didi.cloud.compute.v1.RevertSnapshotRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snap', full_name='didi.cloud.compute.v1.RevertSnapshotRequest.snap', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stopDc2', full_name='didi.cloud.compute.v1.RevertSnapshotRequest.stopDc2', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startDc2', full_name='didi.cloud.compute.v1.RevertSnapshotRequest.startDc2', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REVERTSNAPSHOTREQUEST_INPUT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1187,
  serialized_end=1382,
)


_REVERTSNAPSHOTRESPONSE = _descriptor.Descriptor(
  name='RevertSnapshotResponse',
  full_name='didi.cloud.compute.v1.RevertSnapshotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='didi.cloud.compute.v1.RevertSnapshotResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='didi.cloud.compute.v1.RevertSnapshotResponse.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1384,
  serialized_end=1493,
)


_CHANGESNAPSHOTNAMEREQUEST_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='didi.cloud.compute.v1.ChangeSnapshotNameRequest.Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapUuid', full_name='didi.cloud.compute.v1.ChangeSnapshotNameRequest.Input.snapUuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='didi.cloud.compute.v1.ChangeSnapshotNameRequest.Input.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1674,
  serialized_end=1713,
)

_CHANGESNAPSHOTNAMEREQUEST = _descriptor.Descriptor(
  name='ChangeSnapshotNameRequest',
  full_name='didi.cloud.compute.v1.ChangeSnapshotNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='didi.cloud.compute.v1.ChangeSnapshotNameRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snap', full_name='didi.cloud.compute.v1.ChangeSnapshotNameRequest.snap', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stopDc2', full_name='didi.cloud.compute.v1.ChangeSnapshotNameRequest.stopDc2', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startDc2', full_name='didi.cloud.compute.v1.ChangeSnapshotNameRequest.startDc2', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHANGESNAPSHOTNAMEREQUEST_INPUT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1496,
  serialized_end=1713,
)


_CHANGESNAPSHOTNAMERESPONSE = _descriptor.Descriptor(
  name='ChangeSnapshotNameResponse',
  full_name='didi.cloud.compute.v1.ChangeSnapshotNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='didi.cloud.compute.v1.ChangeSnapshotNameResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='didi.cloud.compute.v1.ChangeSnapshotNameResponse.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1715,
  serialized_end=1828,
)

_LISTSNAPSHOTREQUEST.fields_by_name['header'].message_type = base_dot_v1_dot_base__pb2._HEADER
_LISTSNAPSHOTREQUEST.fields_by_name['condition'].message_type = _LISTSNAPSHOTCONDITION
_LISTSNAPSHOTRESPONSE.fields_by_name['error'].message_type = base_dot_v1_dot_base__pb2._ERROR
_LISTSNAPSHOTRESPONSE.fields_by_name['data'].message_type = compute_dot_v1_dot_common__pb2._SNAPINFO
_GETSNAPSHOTTOTALCNTREQUEST.fields_by_name['header'].message_type = base_dot_v1_dot_base__pb2._HEADER
_GETSNAPSHOTTOTALCNTRESPONSE.fields_by_name['error'].message_type = base_dot_v1_dot_base__pb2._ERROR
_GETSNAPSHOTTOTALCNTRESPONSE.fields_by_name['data'].message_type = compute_dot_v1_dot_common__pb2._TOTALCNTINFO
_CREATESNAPSHOTREQUEST.fields_by_name['header'].message_type = base_dot_v1_dot_base__pb2._HEADER
_CREATESNAPSHOTRESPONSE.fields_by_name['error'].message_type = base_dot_v1_dot_base__pb2._ERROR
_CREATESNAPSHOTRESPONSE.fields_by_name['data'].message_type = base_dot_v1_dot_base__pb2._JOBINFO
_DELETESNAPSHOTREQUEST_INPUT.containing_type = _DELETESNAPSHOTREQUEST
_DELETESNAPSHOTREQUEST.fields_by_name['header'].message_type = base_dot_v1_dot_base__pb2._HEADER
_DELETESNAPSHOTREQUEST.fields_by_name['snap'].message_type = _DELETESNAPSHOTREQUEST_INPUT
_DELETESNAPSHOTRESPONSE.fields_by_name['error'].message_type = base_dot_v1_dot_base__pb2._ERROR
_DELETESNAPSHOTRESPONSE.fields_by_name['data'].message_type = base_dot_v1_dot_base__pb2._JOBINFO
_REVERTSNAPSHOTREQUEST_INPUT.containing_type = _REVERTSNAPSHOTREQUEST
_REVERTSNAPSHOTREQUEST.fields_by_name['header'].message_type = base_dot_v1_dot_base__pb2._HEADER
_REVERTSNAPSHOTREQUEST.fields_by_name['snap'].message_type = _REVERTSNAPSHOTREQUEST_INPUT
_REVERTSNAPSHOTRESPONSE.fields_by_name['error'].message_type = base_dot_v1_dot_base__pb2._ERROR
_REVERTSNAPSHOTRESPONSE.fields_by_name['data'].message_type = base_dot_v1_dot_base__pb2._JOBINFO
_CHANGESNAPSHOTNAMEREQUEST_INPUT.containing_type = _CHANGESNAPSHOTNAMEREQUEST
_CHANGESNAPSHOTNAMEREQUEST.fields_by_name['header'].message_type = base_dot_v1_dot_base__pb2._HEADER
_CHANGESNAPSHOTNAMEREQUEST.fields_by_name['snap'].message_type = _CHANGESNAPSHOTNAMEREQUEST_INPUT
_CHANGESNAPSHOTNAMERESPONSE.fields_by_name['error'].message_type = base_dot_v1_dot_base__pb2._ERROR
_CHANGESNAPSHOTNAMERESPONSE.fields_by_name['data'].message_type = base_dot_v1_dot_base__pb2._JOBINFO
DESCRIPTOR.message_types_by_name['ListSnapshotRequest'] = _LISTSNAPSHOTREQUEST
DESCRIPTOR.message_types_by_name['ListSnapshotCondition'] = _LISTSNAPSHOTCONDITION
DESCRIPTOR.message_types_by_name['ListSnapshotResponse'] = _LISTSNAPSHOTRESPONSE
DESCRIPTOR.message_types_by_name['GetSnapshotTotalCntRequest'] = _GETSNAPSHOTTOTALCNTREQUEST
DESCRIPTOR.message_types_by_name['GetSnapshotTotalCntResponse'] = _GETSNAPSHOTTOTALCNTRESPONSE
DESCRIPTOR.message_types_by_name['CreateSnapshotRequest'] = _CREATESNAPSHOTREQUEST
DESCRIPTOR.message_types_by_name['CreateSnapshotResponse'] = _CREATESNAPSHOTRESPONSE
DESCRIPTOR.message_types_by_name['DeleteSnapshotRequest'] = _DELETESNAPSHOTREQUEST
DESCRIPTOR.message_types_by_name['DeleteSnapshotResponse'] = _DELETESNAPSHOTRESPONSE
DESCRIPTOR.message_types_by_name['RevertSnapshotRequest'] = _REVERTSNAPSHOTREQUEST
DESCRIPTOR.message_types_by_name['RevertSnapshotResponse'] = _REVERTSNAPSHOTRESPONSE
DESCRIPTOR.message_types_by_name['ChangeSnapshotNameRequest'] = _CHANGESNAPSHOTNAMEREQUEST
DESCRIPTOR.message_types_by_name['ChangeSnapshotNameResponse'] = _CHANGESNAPSHOTNAMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListSnapshotRequest = _reflection.GeneratedProtocolMessageType('ListSnapshotRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTSNAPSHOTREQUEST,
  __module__ = 'compute.v1.snap_pb2'
  # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.ListSnapshotRequest)
  ))
_sym_db.RegisterMessage(ListSnapshotRequest)

ListSnapshotCondition = _reflection.GeneratedProtocolMessageType('ListSnapshotCondition', (_message.Message,), dict(
  DESCRIPTOR = _LISTSNAPSHOTCONDITION,
  __module__ = 'compute.v1.snap_pb2'
  # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.ListSnapshotCondition)
  ))
_sym_db.RegisterMessage(ListSnapshotCondition)

ListSnapshotResponse = _reflection.GeneratedProtocolMessageType('ListSnapshotResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTSNAPSHOTRESPONSE,
  __module__ = 'compute.v1.snap_pb2'
  # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.ListSnapshotResponse)
  ))
_sym_db.RegisterMessage(ListSnapshotResponse)

GetSnapshotTotalCntRequest = _reflection.GeneratedProtocolMessageType('GetSnapshotTotalCntRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSNAPSHOTTOTALCNTREQUEST,
  __module__ = 'compute.v1.snap_pb2'
  # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.GetSnapshotTotalCntRequest)
  ))
_sym_db.RegisterMessage(GetSnapshotTotalCntRequest)

GetSnapshotTotalCntResponse = _reflection.GeneratedProtocolMessageType('GetSnapshotTotalCntResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETSNAPSHOTTOTALCNTRESPONSE,
  __module__ = 'compute.v1.snap_pb2'
  # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.GetSnapshotTotalCntResponse)
  ))
_sym_db.RegisterMessage(GetSnapshotTotalCntResponse)

CreateSnapshotRequest = _reflection.GeneratedProtocolMessageType('CreateSnapshotRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATESNAPSHOTREQUEST,
  __module__ = 'compute.v1.snap_pb2'
  # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.CreateSnapshotRequest)
  ))
_sym_db.RegisterMessage(CreateSnapshotRequest)

CreateSnapshotResponse = _reflection.GeneratedProtocolMessageType('CreateSnapshotResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATESNAPSHOTRESPONSE,
  __module__ = 'compute.v1.snap_pb2'
  # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.CreateSnapshotResponse)
  ))
_sym_db.RegisterMessage(CreateSnapshotResponse)

DeleteSnapshotRequest = _reflection.GeneratedProtocolMessageType('DeleteSnapshotRequest', (_message.Message,), dict(

  Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), dict(
    DESCRIPTOR = _DELETESNAPSHOTREQUEST_INPUT,
    __module__ = 'compute.v1.snap_pb2'
    # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.DeleteSnapshotRequest.Input)
    ))
  ,
  DESCRIPTOR = _DELETESNAPSHOTREQUEST,
  __module__ = 'compute.v1.snap_pb2'
  # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.DeleteSnapshotRequest)
  ))
_sym_db.RegisterMessage(DeleteSnapshotRequest)
_sym_db.RegisterMessage(DeleteSnapshotRequest.Input)

DeleteSnapshotResponse = _reflection.GeneratedProtocolMessageType('DeleteSnapshotResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETESNAPSHOTRESPONSE,
  __module__ = 'compute.v1.snap_pb2'
  # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.DeleteSnapshotResponse)
  ))
_sym_db.RegisterMessage(DeleteSnapshotResponse)

RevertSnapshotRequest = _reflection.GeneratedProtocolMessageType('RevertSnapshotRequest', (_message.Message,), dict(

  Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), dict(
    DESCRIPTOR = _REVERTSNAPSHOTREQUEST_INPUT,
    __module__ = 'compute.v1.snap_pb2'
    # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.RevertSnapshotRequest.Input)
    ))
  ,
  DESCRIPTOR = _REVERTSNAPSHOTREQUEST,
  __module__ = 'compute.v1.snap_pb2'
  # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.RevertSnapshotRequest)
  ))
_sym_db.RegisterMessage(RevertSnapshotRequest)
_sym_db.RegisterMessage(RevertSnapshotRequest.Input)

RevertSnapshotResponse = _reflection.GeneratedProtocolMessageType('RevertSnapshotResponse', (_message.Message,), dict(
  DESCRIPTOR = _REVERTSNAPSHOTRESPONSE,
  __module__ = 'compute.v1.snap_pb2'
  # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.RevertSnapshotResponse)
  ))
_sym_db.RegisterMessage(RevertSnapshotResponse)

ChangeSnapshotNameRequest = _reflection.GeneratedProtocolMessageType('ChangeSnapshotNameRequest', (_message.Message,), dict(

  Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), dict(
    DESCRIPTOR = _CHANGESNAPSHOTNAMEREQUEST_INPUT,
    __module__ = 'compute.v1.snap_pb2'
    # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.ChangeSnapshotNameRequest.Input)
    ))
  ,
  DESCRIPTOR = _CHANGESNAPSHOTNAMEREQUEST,
  __module__ = 'compute.v1.snap_pb2'
  # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.ChangeSnapshotNameRequest)
  ))
_sym_db.RegisterMessage(ChangeSnapshotNameRequest)
_sym_db.RegisterMessage(ChangeSnapshotNameRequest.Input)

ChangeSnapshotNameResponse = _reflection.GeneratedProtocolMessageType('ChangeSnapshotNameResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHANGESNAPSHOTNAMERESPONSE,
  __module__ = 'compute.v1.snap_pb2'
  # @@protoc_insertion_point(class_scope:didi.cloud.compute.v1.ChangeSnapshotNameResponse)
  ))
_sym_db.RegisterMessage(ChangeSnapshotNameResponse)


DESCRIPTOR._options = None

_SNAP = _descriptor.ServiceDescriptor(
  name='Snap',
  full_name='didi.cloud.compute.v1.Snap',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1831,
  serialized_end=2536,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListSnapshot',
    full_name='didi.cloud.compute.v1.Snap.ListSnapshot',
    index=0,
    containing_service=None,
    input_type=_LISTSNAPSHOTREQUEST,
    output_type=_LISTSNAPSHOTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSnapshotTotalCnt',
    full_name='didi.cloud.compute.v1.Snap.GetSnapshotTotalCnt',
    index=1,
    containing_service=None,
    input_type=_GETSNAPSHOTTOTALCNTREQUEST,
    output_type=_GETSNAPSHOTTOTALCNTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateSnapshot',
    full_name='didi.cloud.compute.v1.Snap.CreateSnapshot',
    index=2,
    containing_service=None,
    input_type=_CREATESNAPSHOTREQUEST,
    output_type=_CREATESNAPSHOTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteSnapshot',
    full_name='didi.cloud.compute.v1.Snap.DeleteSnapshot',
    index=3,
    containing_service=None,
    input_type=_DELETESNAPSHOTREQUEST,
    output_type=_DELETESNAPSHOTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RevertSnapshot',
    full_name='didi.cloud.compute.v1.Snap.RevertSnapshot',
    index=4,
    containing_service=None,
    input_type=_REVERTSNAPSHOTREQUEST,
    output_type=_REVERTSNAPSHOTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ChangeSnapshotName',
    full_name='didi.cloud.compute.v1.Snap.ChangeSnapshotName',
    index=5,
    containing_service=None,
    input_type=_CHANGESNAPSHOTNAMEREQUEST,
    output_type=_CHANGESNAPSHOTNAMERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SNAP)

DESCRIPTOR.services_by_name['Snap'] = _SNAP

# @@protoc_insertion_point(module_scope)
