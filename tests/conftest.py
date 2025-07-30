import pytest

@pytest.fixture
def timetable_optimization_input():
    return {
        "peak_load": 100,
        "regular_load": 80,
        "vehicle_types": [
            {
                "vehicle_type": "Otobüs (12m)",
                "capacity": {
                    "capacity": 99,
                    "number_of_seats": 28
                }
            },
            {
                "vehicle_type": "Otobüs (8,5m)",
                "capacity": {
                    "capacity": 77,
                    "number_of_seats": 26
                }
            },
            {
                "vehicle_type": "Minibüs",
                "capacity": {
                    "capacity": 14,
                    "number_of_seats": 14
                }
            }
        ],
        "input_params": {
            "route_info": [
                {
                    "end_hour": 9,
                    "free_flow_duration": 107,
                    "kilometer": 24.88,
                    "route_id": "000600_1",
                    "direction": "inbound",
                    "start_hour": 5,
                    "trip_periods": [
                        {
                            "duration": 107,
                            "end_hour": 6,
                            "load": 0,
                            "start_hour": 5
                        },
                        {
                            "duration": 107,
                            "end_hour": 7,
                            "load": 44,
                            "start_hour": 6
                        },
                        {
                            "duration": 107,
                            "end_hour": 8,
                            "load": 332,
                            "start_hour": 7
                        },
                        {
                            "duration": 107,
                            "end_hour": 9,
                            "load": 525,
                            "peak": True,
                            "start_hour": 8
                        }
                    ]
                },
                {
                    "end_hour": 9,
                    "free_flow_duration": 150,
                    "kilometer": 35.46,
                    "route_id": "000800_1",
                    "direction": "outbound",
                    "start_hour": 5,
                    "trip_periods": [
                        {
                            "duration": 150,
                            "end_hour": 6,
                            "load": 2,
                            "start_hour": 5
                        },
                        {
                            "duration": 150,
                            "end_hour": 7,
                            "load": 87,
                            "start_hour": 6
                        },
                        {
                            "duration": 150,
                            "end_hour": 8,
                            "load": 329,
                            "start_hour": 7
                        },
                        {
                            "duration": 150,
                            "end_hour": 9,
                            "load": 470,
                            "peak": True,
                            "start_hour": 8
                        }
                    ]
                }
            ]
        }
    }

@pytest.fixture
def timetable_optimization_output(request):
    # Access loop_routes value from the param
    loop_routes = request.param

    optimized_output = {
        'routes': [
            {
                'id': '000600_1',
                'direction': 'inbound',
                'vehicles': [
                    None,
                    {'start_time': 6, 'departure': 1, 'vehicle_type': 'Otobüs (8,5m)'},
                    {'start_time': 7, 'departure': 5, 'vehicle_type': 'Otobüs (12m)'},
                    {'start_time': 8, 'departure': 6, 'vehicle_type': 'Otobüs (12m)'}
                ]
            },
            {
                'id': '000800_1',
                'direction': 'outbound',
                'vehicles': [
                    {'start_time': 5, 'departure': 1, 'vehicle_type': 'Minibüs'},
                    {'start_time': 6, 'departure': 2, 'vehicle_type': 'Otobüs (8,5m)'},
                    {'start_time': 7, 'departure': 5, 'vehicle_type': 'Otobüs (12m)'},
                    {'start_time': 8, 'departure': 5, 'vehicle_type': 'Otobüs (12m)'}
                ]
            }
        ]
    }

    # Return different output if loop_routes is True
    if loop_routes:
        return {'routes': [{'id': '000600_1', 'vehicles': [{'start_time': 6, 'departure': 1, 'vehicle_type': 'Otobüs (8,5m)', 'frequency': 3600.0, 'frequency_level_of_service': 'E', 'load_level_of_service': 'D+', 'load_level_of_service_value': 0.5714285714285714, 'kilometer_traveled': 24.88}, {'start_time': 7, 'departure': 5, 'vehicle_type': 'Otobüs (12m)', 'frequency': 720.0, 'frequency_level_of_service': 'B', 'load_level_of_service': 'D+', 'load_level_of_service_value': 0.6707070707070707, 'kilometer_traveled': 124.39999999999999}, {'start_time': 8, 'departure': 6, 'vehicle_type': 'Otobüs (12m)', 'frequency': 600.0, 'frequency_level_of_service': 'B', 'load_level_of_service': 'E+', 'load_level_of_service_value': 0.8838383838383839, 'kilometer_traveled': 149.28}], 'time_table': ['06:00', '07:00', '07:12', '07:24', '07:36', '07:48', '08:00', '08:10', '08:20', '08:30', '08:40', '08:50'], 'average_load_service_level': 'D', 'average_load_service_level_value': 0.7086580086580087, 'average_frequency_service_level': 'C', 'average_frequency_service_level_value': 4.0, 'kilometer_traveled': 298.56}, {'id': '000800_1', 'vehicles': [{'start_time': 5, 'departure': 1, 'vehicle_type': 'Minibüs', 'frequency': 3600.0, 'frequency_level_of_service': 'E', 'load_level_of_service': 'A', 'load_level_of_service_value': 0.14285714285714285, 'kilometer_traveled': 35.46}, {'start_time': 6, 'departure': 2, 'vehicle_type': 'Otobüs (8,5m)', 'frequency': 1800.0, 'frequency_level_of_service': 'D', 'load_level_of_service': 'D+', 'load_level_of_service_value': 0.564935064935065, 'kilometer_traveled': 70.92}, {'start_time': 7, 'departure': 5, 'vehicle_type': 'Otobüs (12m)', 'frequency': 720.0, 'frequency_level_of_service': 'B', 'load_level_of_service': 'D+', 'load_level_of_service_value': 0.6646464646464646, 'kilometer_traveled': 177.3}, {'start_time': 8, 'departure': 5, 'vehicle_type': 'Otobüs (12m)', 'frequency': 720.0, 'frequency_level_of_service': 'B', 'load_level_of_service': 'E', 'load_level_of_service_value': 0.9494949494949495, 'kilometer_traveled': 177.3}], 'time_table': ['05:00', '06:00', '06:30', '07:00', '07:12', '07:24', '07:36', '07:48', '08:00', '08:12', '08:24', '08:36', '08:48'], 'average_load_service_level': 'D+', 'average_load_service_level_value': 0.5804834054834055, 'average_frequency_service_level': 'C', 'average_frequency_service_level_value': 3.25, 'kilometer_traveled': 460.98}]}
    return optimized_output

@pytest.fixture
def route_merger_input():
    return {
        'routes': [
            {'id': '000600_1', 'direction': 'inbound', 'vehicles': [
                None,
                {'start_time': 6, 'departure': 1, 'vehicle_type': 'Otobüs (8,5m)'},
                {'start_time': 7, 'departure': 5, 'vehicle_type': 'Otobüs (12m)'},
                {'start_time': 8, 'departure': 6, 'vehicle_type': 'Otobüs (12m)'}
            ]},
            {'id': '000600_1', 'direction': 'outbound', 'vehicles': [
                {'start_time': 5, 'departure': 1, 'vehicle_type': 'Minibüs'},
                {'start_time': 6, 'departure': 4, 'vehicle_type': 'Otobüs (12m)'},
                {'start_time': 7, 'departure': 2, 'vehicle_type': 'Otobüs (12m)'},
                {'start_time': 8, 'departure': 1, 'vehicle_type': 'Otobüs (12m)'}
            ]}
        ]
    }

@pytest.fixture
def route_merger_output(request):
    generate_timetable = request.param
    if not generate_timetable:
        return {'routes': [{'id': '000600_1', 'vehicles': [{'start_time': 6, 'departure': 4, 'vehicle_type': 'Otobüs (12m)'}, {'start_time': 7, 'departure': 5, 'vehicle_type': 'Otobüs (12m)'}, {'start_time': 8, 'departure': 6, 'vehicle_type': 'Otobüs (12m)'}, {'start_time': 5, 'departure': 1, 'vehicle_type': 'Minibüs'}]}]}
    return {'routes': [{'id': '000600_1', 'vehicles': [{'start_time': 6, 'departure': 4, 'vehicle_type': 'Otobüs (12m)'}, {'start_time': 7, 'departure': 5, 'vehicle_type': 'Otobüs (12m)'}, {'start_time': 8, 'departure': 6, 'vehicle_type': 'Otobüs (12m)'}, {'start_time': 5, 'departure': 1, 'vehicle_type': 'Minibüs'}], 'time_table': ['05:00', '06:00', '06:15', '06:30', '06:45', '07:00', '07:12', '07:24', '07:36', '07:48', '08:00', '08:10', '08:20', '08:30', '08:40', '08:50']}]}

@pytest.fixture
def timetable_input_basic():
    return{
        "peak_load": 100,
        "regular_load": 80,
        "vehicle_types": [
            {"vehicle_type": "Otobüs (12m)", "capacity": {"capacity": 99, "number_of_seats": 28}},
        ]
    }

@pytest.fixture
def route_merger_output():
    return {
        "routes": [
            {
                "id": "000600_1",
                "vehicles": [{"start_time": 6, "departure": 4, "vehicle_type": "Otobüs (12m)"}]
            }
        ]
    }