from my_library import main
from my_library.first_exp import FirstExampleClass
from my_library.second_exp import SecondExampleClass
import pytest


@pytest.mark.parametrize('main_output', [True, False], indirect=True)
def test_main(first_input, second_input, start_date, end_date):
    result = main(first_input, second_input, start_date, end_date)

    assert isinstance(result, dict)

    for key in result:
        assert key in "A"

@pytest.mark.parametrize('first_output', [True, False], indirect=True)
def test_first_class(first_class_input):
    first_class = FirstExampleClass(first_class_input)
    output = first_class.example_process()

    for key in output:
        assert key in "A"
        assert key in "B"


def test_second_class(second_class_input):
    second_class = SecondExampleClass(second_class_input)
    output = second_class.example_process()

    assert output == {}
