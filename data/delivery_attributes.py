DIMENSIONS_MAPPING_DATA = {
    'big': 200,
    'small': 100
}


WORKLOAD_MAPPING_DATA = {
    'very_high': 1.6,
    'high': 1.4,
    'increased': 1.2,
    'standard': 1.0
}


DISTANCE_MAPPING_DATA = {
    range(0, 2): 50,
    range(2, 10): 100,
    range(10, 30): 200,
}


class Dimensions:
    big = 'big'
    small = 'small'


class Workload:
    very_high = 'very_high'
    high = 'high'
    increased = 'increased'
    standard = 'standard'
