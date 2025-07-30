from .first_exp import FirstExampleClass
from .second_exp import SecondExampleClass


def main(first_data, second_data, start_date, end_date):
    first_class = FirstExampleClass(first_data, start_date, end_date)
    first_output = first_class.example_process()

    second_class = SecondExampleClass(second_data)
    second_output = second_class.example_process()

    return first_output == second_output

if __name__ == "__main__":

    first_input = {
        'routes': [ "1-A", "2-A", "3-A"]
    }

    second_input = {
        'routes': [
            {
                'id': '000600_1', 
                'direction': 'inbound', 
                'vehicles': [
                    {'start_time': 6, 'departure': 1, 'vehicle_type': 'Otobüs (8,5m)'},
                    {'start_time': 7, 'departure': 5, 'vehicle_type': 'Otobüs (12m)'},
                    {'start_time': 8, 'departure': 6, 'vehicle_type': 'Otobüs (12m)'}
                ]
            }
        ]
    }

    # Run the main function
    result = main(
        first_data=first_input,
        second_data=second_input,
        start_date="2025-07-30",
        end_date="2025-07-31"
    )
    print(result)
