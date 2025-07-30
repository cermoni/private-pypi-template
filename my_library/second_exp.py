from typing import Dict, Any

class SecondExampleClass:
    def __init__(self, input: Dict[str, Any], debug=False):
        self.input = input
        self.debug = debug

    def example_process(self):
        return {"routes_lenght": len(self.input['routes']['vehicles'])}

if __name__ == "__main__":
    example_input = {
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

    example_class = SecondExampleClass(example_input)
    example_output = example_class.example_process()
    print(example_output)
