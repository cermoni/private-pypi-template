import os
import sys
import marshal

# Load environment variables from `.env` file if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # Ignore if `python-dotenv` is not installed

# Enable/Disable debug mode (True = show, False = hide)
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

# Enable development mode if the environment variable is set
DEV_MODE = os.getenv("DEV_MODE", "False").lower() == "true"

if DEV_MODE:
    # Development mode: Directly import the original Python files
    from .base import main

    def run_algorithm(my_library_input, loop_routes):
        return main(my_library_input, loop_routes)

else:
    # Production mode: Load obfuscated `.marshal` files
    package_dir = os.path.dirname(__file__)

    # **Find all `.marshal` files**
    marshal_files = {
        f.replace(".marshal", ""): os.path.join(package_dir, f)
        for f in os.listdir(package_dir) if f.endswith(".marshal")
    }

    if not marshal_files:
        raise ImportError(f"Obfuscated Python files not found in {package_dir}")

    def load_marshal_module(module_name, file_path):
        try:
            if DEBUG_MODE:
                print(f"Loading module: {module_name} from {file_path}")  

            with open(file_path, "rb") as f:
                bytecode = f.read()
                code = marshal.loads(bytecode)

            # **Define the module name**
            full_module_name = f"my_library.{module_name}"

            # **If already loaded, skip**
            if full_module_name in sys.modules:
                if DEBUG_MODE:
                    print(f"Module {full_module_name} already loaded.")
                return sys.modules[full_module_name]

            # **Create an empty module**
            module = type(sys)(full_module_name)
            module.__file__ = file_path
            module.__package__ = "my_library" if "." not in module_name else ".".join(full_module_name.split(".")[:-1])
            module.__name__ = full_module_name  

            # **Execute the bytecode**
            exec(code, module.__dict__)

            # **Register the module**
            sys.modules[full_module_name] = module

            if DEBUG_MODE:
                print(f"Successfully loaded {full_module_name}.")
            return module

        except Exception as e:
            raise ImportError(f"Failed to load {module_name}: {e}")

    # **Load modules in correct order (fix dependencies)**
    DEPENDENCIES = ["route_merger", "kpi_calculator", "timetable_optimizer", "base"]

    for module_name in DEPENDENCIES:
        if module_name in marshal_files:
            load_marshal_module(module_name, marshal_files[module_name])

    # **Check loaded modules**
    if DEBUG_MODE:
        print("Loaded modules:", [mod for mod in sys.modules.keys() if "my_library" in mod])

    # **Retrieve `main` function from `base.marshal`**
    if "my_library.base" in sys.modules and hasattr(sys.modules["my_library.base"], "main"):
        if DEBUG_MODE:
            print("Main function found in base module.")
        main = sys.modules["my_library.base"].main
    else:
        raise ImportError("The compiled module does not contain a 'main' function.")

    def run_algorithm(my_library_input, loop_routes):
        return main(my_library_input, loop_routes)
