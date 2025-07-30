from typing import Dict, Any

class FirstExampleClass:
    def __init__(self, input: Dict[str, Any], start_date: str, end_date: str):
        self.input = input
        self.start_date = start_date
        self.end_date = end_date

    def example_process(self):
        return {"routes_lenght": len(self.input['routes'])}

if __name__ == "__main__":
    example_input = {
        'routes': [ "1-A", "2-A", "3-A"]
    }
    example_start_date = "2025-07-30"
    example_end_date = "2025-07-31"

    example_class = FirstExampleClass(example_input)
    example_output = example_class.example_process()
    print(example_output)
