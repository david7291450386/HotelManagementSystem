from datetime import date


def periods_overlap(start: date, end: date, other_start: date, other_end: date) -> bool:
    """Проверяет пересечение двух периодов проживания по занятым ночам."""
    if start >= end or other_start >= other_end:
        raise ValueError("Дата выезда должна быть позже даты заезда")
    return start < other_end and other_start < end
