import unittest
from datetime import date

from hotel.booking import periods_overlap


class BookingPeriodTests(unittest.TestCase):
    def test_shared_night(self) -> None:
        self.assertTrue(
            periods_overlap(
                date(2026, 12, 10),
                date(2026, 12, 12),
                date(2026, 12, 11),
                date(2026, 12, 13),
            )
        )

    def test_arrival_on_departure_day(self) -> None:
        self.assertFalse(
            periods_overlap(
                date(2026, 12, 10),
                date(2026, 12, 12),
                date(2026, 12, 12),
                date(2026, 12, 13),
            )
        )

    def test_empty_period(self) -> None:
        day = date(2026, 12, 10)
        with self.assertRaises(ValueError):
            periods_overlap(day, day, day, date(2026, 12, 12))
