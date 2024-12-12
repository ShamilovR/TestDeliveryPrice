from data.delivery_attributes import (
    DISTANCE_MAPPING_DATA,
    WORKLOAD_MAPPING_DATA,
    DIMENSIONS_MAPPING_DATA
)
from data.error_messages import ValidateErrorMessages


def validate(
        distance: float,
        dimensions: str,
        is_fragile: bool,
        workload: str
) -> True or list[str]:
    """
    Валидация входных параметров.

    :param distance: Расстояние до пункта назначения.
    :param dimensions: Габариты груза.
    :param is_fragile: Информация о хрупкости.
    :param workload: Загруженность доставки.
    """
    errors = []

    if not isinstance(distance, (float, int)) or distance < 0:
        errors.append(ValidateErrorMessages.distance_error)

    if not isinstance(dimensions, str) or dimensions not in DIMENSIONS_MAPPING_DATA.keys():
        errors.append(ValidateErrorMessages.dimensions_error)

    if not isinstance(is_fragile, bool):
        errors.append(ValidateErrorMessages.fragile_error)

    if not isinstance(workload, str) or workload not in WORKLOAD_MAPPING_DATA.keys():
        errors.append(ValidateErrorMessages.workload_error)

    return errors or True


def map_distance(distance: float) -> int:
    """
    Сопоставление расстояния и стоимости доставки за это расстояние.

    :param distance: Расстояние до пункта назначения.
    """
    for distance_range, price in DISTANCE_MAPPING_DATA.items():
        if distance in distance_range:
            return price
    return 300


def calculate_delivery_price(
        distance: float,
        dimensions: str,
        is_fragile: bool,
        workload: str
) -> float or str:
    """
    Расчет стоимости доставки груза.

    :param distance: Расстояние до пункта назначения.
    :param dimensions: Габариты груза.
    :param is_fragile: Информация о хрупкости.
    :param workload: Загруженность доставки.
    """

    validate_result = validate(distance, dimensions, is_fragile, workload)
    if validate_result is not True:
        return validate_result

    if distance > 30 and is_fragile:
        return ValidateErrorMessages.fragile_distance_error

    delivery_price = 0
    delivery_price += map_distance(distance)
    delivery_price += DIMENSIONS_MAPPING_DATA[dimensions]
    delivery_price = delivery_price + 300 if is_fragile else delivery_price
    delivery_price *= WORKLOAD_MAPPING_DATA[workload]

    return delivery_price if delivery_price > 400 else 400
