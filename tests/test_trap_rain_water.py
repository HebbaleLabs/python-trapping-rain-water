import unittest
from parameterized import parameterized
from trap_rain_water import do_trap_rain_water


class TrapRainWaterTest(unittest.TestCase):

    @parameterized.expand([
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([3, 0, 0, 2, 0, 4], 10),
        ([2, 0, 2], 2),
        ([1, 4, 2, 5, 0, 6, 2, 3, 4], 10),
        ([0, 4, 5, 1, 0, 0], 0),
        ([7, 0, 4, 2, 5, 0, 6, 4, 0, 5], 25),
        ([1, 0, 2, 2, 4, 0, 1, 5, 2, 1, 6, 1], 15),
        ([4, 2, 3, 5, 2, 3, 4, 5], 9),
    ])
    def test_trap_rain_water(self, input_value, expected_result):
        self.longMessage = True
        actual = do_trap_rain_water(input_value)
        message = 'For input {0}, expected value = {1}, and actual value = {2}'.format(input_value, expected_result, actual)
        self.assertEqual(expected_result, actual, message)
