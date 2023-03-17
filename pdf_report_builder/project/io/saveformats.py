from enum import Enum

class saveformats(Enum):
    JSON_V01 = 1

FILE_EXTENSIONS = {
    "REPORTPRJ": saveformats.JSON_V01
}