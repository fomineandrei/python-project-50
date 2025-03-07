from gendiff.output_formates.stylish import stylish
from gendiff.output_formates.plane import plane
from gendiff.output_formates.json_formate import json


OUTPUT_FORMATES = {
    'stylish': stylish,
    'plane': plane,
    'json': json
}


__all__ = (
    'OUTPUT_FORMATES'
)
