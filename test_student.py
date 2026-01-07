from student import calculate_grade, compute_average


def test_grade_s():
    avg = 95
    assert calculate_grade(avg) == "S"


def test_grade_a():
    avg = 85
    assert calculate_grade(avg) == "A"


def test_grade_b():
    avg = 70
    assert calculate_grade(avg) == "B"


def test_grade_c():
    avg = 55
    assert calculate_grade(avg) == "C"


def test_grade_d():
    avg = 45
    assert calculate_grade(avg) == "D"


def test_grade_f():
    avg = 30
    assert calculate_grade(avg) == "F"


def test_average_calculation():
    marks = [85, 90, 88]
    average = compute_average(marks)
    assert round(average, 2) == 87.67
