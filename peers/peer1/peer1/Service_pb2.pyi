from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Credentials(_message.Message):
    __slots__ = ("credentials",)
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    credentials: str
    def __init__(self, credentials: _Optional[str] = ...) -> None: ...

class OperationResponse(_message.Message):
    __slots__ = ("serverResponse",)
    SERVERRESPONSE_FIELD_NUMBER: _ClassVar[int]
    serverResponse: str
    def __init__(self, serverResponse: _Optional[str] = ...) -> None: ...
