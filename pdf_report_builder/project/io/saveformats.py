from enum import Enum

class saveformats(Enum):
    JSON_V01 = 1

FILE_EXTENSIONS = {
    "JSON": saveformats.JSON_V01
}