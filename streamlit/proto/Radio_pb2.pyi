"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
*!
Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import streamlit.proto.LabelVisibilityMessage_pb2
import sys
import typing

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Radio(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    DEFAULT_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    HELP_FIELD_NUMBER: builtins.int
    FORM_ID_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    SET_VALUE_FIELD_NUMBER: builtins.int
    DISABLED_FIELD_NUMBER: builtins.int
    HORIZONTAL_FIELD_NUMBER: builtins.int
    LABEL_VISIBILITY_FIELD_NUMBER: builtins.int
    CAPTIONS_FIELD_NUMBER: builtins.int
    id: builtins.str
    label: builtins.str
    default: builtins.int
    @property
    def options(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    help: builtins.str
    form_id: builtins.str
    value: builtins.int
    set_value: builtins.bool
    disabled: builtins.bool
    horizontal: builtins.bool
    @property
    def label_visibility(self) -> streamlit.proto.LabelVisibilityMessage_pb2.LabelVisibilityMessage: ...
    @property
    def captions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        label: builtins.str = ...,
        default: builtins.int | None = ...,
        options: collections.abc.Iterable[builtins.str] | None = ...,
        help: builtins.str = ...,
        form_id: builtins.str = ...,
        value: builtins.int | None = ...,
        set_value: builtins.bool = ...,
        disabled: builtins.bool = ...,
        horizontal: builtins.bool = ...,
        label_visibility: streamlit.proto.LabelVisibilityMessage_pb2.LabelVisibilityMessage | None = ...,
        captions: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_default", b"_default", "_value", b"_value", "default", b"default", "label_visibility", b"label_visibility", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_default", b"_default", "_value", b"_value", "captions", b"captions", "default", b"default", "disabled", b"disabled", "form_id", b"form_id", "help", b"help", "horizontal", b"horizontal", "id", b"id", "label", b"label", "label_visibility", b"label_visibility", "options", b"options", "set_value", b"set_value", "value", b"value"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_default", b"_default"]) -> typing_extensions.Literal["default"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_value", b"_value"]) -> typing_extensions.Literal["value"] | None: ...

global___Radio = Radio
