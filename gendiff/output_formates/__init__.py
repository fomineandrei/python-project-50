from gendiff.output_formates.stylish import stylish
from gendiff.output_formates.plain import plain
from gendiff.output_formates.json_formate import json


# Возможные форматы вывода диффа файлов
OUTPUT_FORMATES = {
    'stylish': stylish,
    'plain': plain,
    'json': json
}


__all__ = (
    'OUTPUT_FORMATES'
)
