# -*- coding: utf-8 -*-



__all__ = [
    "MLAlchemyError",
    "InvalidOperatorError",
    "InvalidComparatorError",
    "QuerySyntaxError",
    "InvalidTableError",
    "InvalidFieldError"
]


class MLAlchemyError(Exception):
    pass


class InvalidOperatorError(MLAlchemyError):
    pass


class InvalidComparatorError(MLAlchemyError):
    pass


class QuerySyntaxError(MLAlchemyError):
    pass


class InvalidTableError(MLAlchemyError):
    pass


class InvalidFieldError(MLAlchemyError):
    pass
