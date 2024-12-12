import pytest

from data.delivery_attributes import Dimensions, Workload
from data.error_messages import ValidateErrorMessages
from functional.delivery_calculate import calculate_delivery_price


class TestDeliveryCalculate:
    @pytest.mark.parametrize(
        'distance, dimensions, is_fragile, workload, result',
        (
                (0, Dimensions.small, True, Workload.standard, 450),
                (1, Dimensions.big, True, Workload.increased, 660),
                (0, Dimensions.big, False, Workload.very_high, 400),
                (2, Dimensions.small, True, Workload.standard, 500),
                (5, Dimensions.big, True, Workload.increased, 720),
                (9, Dimensions.big, False, Workload.very_high, 480),
                (10, Dimensions.small, True, Workload.standard, 600),
                (15, Dimensions.big, True, Workload.increased, 840),
                (25, Dimensions.small, False, Workload.high, 420),
                (29, Dimensions.big, False, Workload.very_high, 640),
                (30, Dimensions.big, True, Workload.increased, 960),
                (70, Dimensions.small, False, Workload.high, 560),
                (100, Dimensions.big, False, Workload.very_high, 800),
        )
    )
    def test_delivery_calculate_positive(self, distance, dimensions, is_fragile, workload, result):
        delivery_price = calculate_delivery_price(distance, dimensions, is_fragile, workload)

        assert delivery_price == result, \
            f"Некорректный расчет стоимости доставки при параметрах \n" \
            f"distance: {distance}, \n" \
            f"dimensions: {dimensions}, \n" \
            f"is_fragile: {is_fragile}, \n" \
            f"workload: {workload}. \n"

    @pytest.mark.parametrize(
        'distance, dimensions, is_fragile, workload, error_message',
        (
                (31, Dimensions.small, True, Workload.standard, ValidateErrorMessages.fragile_distance_error),
                ("qwerty", 1, 1, 1, [
                    ValidateErrorMessages.distance_error,
                    ValidateErrorMessages.dimensions_error,
                    ValidateErrorMessages.fragile_error,
                    ValidateErrorMessages.workload_error]
                 ),
                (-1, "qwerty", False, "qwerty", [
                    ValidateErrorMessages.distance_error,
                    ValidateErrorMessages.dimensions_error,
                    ValidateErrorMessages.workload_error]
                 )
        )
    )
    def test_delivery_calculate_negative(self, distance, dimensions, is_fragile, workload, error_message):
        calculate_result = calculate_delivery_price(distance, dimensions, is_fragile, workload)

        assert calculate_result == error_message, \
            f"Некорректная работа валидации при параметрах \n" \
            f"distance: {distance}, \n" \
            f"dimensions: {dimensions}, \n" \
            f"is_fragile: {is_fragile}, \n" \
            f"workload: {workload}. \n"
