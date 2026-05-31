from enum import StrEnum


class Environment(StrEnum):
    DEVELOPMENT = "development"
    TESTING = "testing"
    PRODUCTION = "production"


class LogLevel(StrEnum):
    INFO = "info"
    DEBUG = "debug"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"
