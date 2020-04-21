from typing import Any, Optional

class Error(Exception): ...
class SchemaError(Error): ...

class Invalid(Error):
    path: Any = ...
    error_message: Any = ...
    error_type: Any = ...
    def __init__(self, message: Any, path: Optional[Any] = ..., error_message: Optional[Any] = ..., error_type: Optional[Any] = ...) -> None: ...
    @property
    def msg(self): ...
    def prepend(self, path: Any) -> None: ...

class MultipleInvalid(Invalid):
    errors: Any = ...
    def __init__(self, errors: Optional[Any] = ...) -> None: ...
    @property
    def msg(self): ...
    @property
    def path(self): ...
    @property
    def error_message(self): ...
    def add(self, error: Any) -> None: ...
    def prepend(self, path: Any) -> None: ...

class RequiredFieldInvalid(Invalid): ...
class ObjectInvalid(Invalid): ...
class DictInvalid(Invalid): ...
class ExclusiveInvalid(Invalid): ...
class InclusiveInvalid(Invalid): ...
class SequenceTypeInvalid(Invalid): ...
class TypeInvalid(Invalid): ...
class ValueInvalid(Invalid): ...
class ContainsInvalid(Invalid): ...
class ScalarInvalid(Invalid): ...
class CoerceInvalid(Invalid): ...
class AnyInvalid(Invalid): ...
class AllInvalid(Invalid): ...
class MatchInvalid(Invalid): ...
class RangeInvalid(Invalid): ...
class TrueInvalid(Invalid): ...
class FalseInvalid(Invalid): ...
class BooleanInvalid(Invalid): ...
class UrlInvalid(Invalid): ...
class EmailInvalid(Invalid): ...
class FileInvalid(Invalid): ...
class DirInvalid(Invalid): ...
class PathInvalid(Invalid): ...
class LiteralInvalid(Invalid): ...
class LengthInvalid(Invalid): ...
class DatetimeInvalid(Invalid): ...
class DateInvalid(Invalid): ...
class InInvalid(Invalid): ...
class NotInInvalid(Invalid): ...
class ExactSequenceInvalid(Invalid): ...
class NotEnoughValid(Invalid): ...
class TooManyValid(Invalid): ...
