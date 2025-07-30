#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

PACKAGE_NAME="my_library"
DIST_DIR="dist"

get_version() {
    grep -oP '(?<=^version = ").*(?="$)' pyproject.toml || echo "0.1.0"
}

obfuscate_python_files() {
    printf "Obfuscating Python files with Marshal...\n"

    find "$PACKAGE_NAME" -type f -name "*.py" ! -name "__init__.py" ! -name "__main__.py" | while read -r file; do
        python -c "import marshal; f=open('$file'); c=marshal.dumps(compile(f.read(), '$file', 'exec')); open('${file%.py}.marshal', 'wb').write(c)"
        rm -f "$file"
    done
}

build_package() {
    local version
    version=$(get_version)

    printf "Configuring package (Version: %s) and building...\n" "$version"

    cat <<EOF > setup.py
from setuptools import setup, find_packages

setup(
    name="my-library",
    version="$version",
    packages=find_packages(exclude=["tests"]),
    package_data={"my_library": ["*.marshal"]},
    include_package_data=True,
)
EOF

    echo -e "include my_library/*.marshal\nprune tests" > MANIFEST.in

    python setup.py sdist bdist_wheel || { printf "Build failed.\n" >&2; return 1; }
}

main() {
    obfuscate_python_files
    build_package
    printf "Build complete. Package is in '%s'.\n" "$DIST_DIR"
}

main "$@"
