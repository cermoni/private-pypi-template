# My library

<img src="https://static.wixstatic.com/media/26c7a3_6b28209865cf4d25beb60e25d7ee4f85~mv2.png/v1/fill/w_328,h_100,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Logo%20with%20slogan.png"/>

**My Library** is a project designed to optimize scheduling and resource allocation for public transportation systems. 

*Python version **'3.10.12'** is preferred because stable PyArmor version supports python <3.11*

## Table of Contents

- [Getting Started](#getting-started)
  - [Installing Poetry](#installing-poetry)
  - [Setting Up the Project](#setting-up-the-project)
- [Running the Project](#running-the-project)
  - [Running Functions](#running-functions)
- [Development](#development)
  - [Linting the Code](#linting-the-code)
  - [Running Tests](#running-tests)
  - [Running Tests with Coverage Report](#running-tests-with-coverage-report)
- [Building the Project](#building-the-project)
- [Continuous Integration and Deployment](#continuous-integration-and-deployment)
  - [Linting and Testing](#linting-and-testing)
  - [Publishing Releases](#publishing-releases)
- [Installing Released Package](#installing-released-package)
- [Documentation](#documentation)

## Getting Started

### Installing Poetry

First, ensure that you have [Poetry](https://python-poetry.org/docs/#installation) installed on your machine. Poetry is a tool for dependency management and packaging in Python. It will handle the creation of a virtual environment and the installation of all necessary dependencies.

To install Poetry, run the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Setting Up the Project

Once Poetry is installed, you can set up the project by running:

```bash
poetry install
```

This command will create a virtual environment (if not already created) and install all dependencies listed in the `pyproject.toml` file.

To activate the virtual environment, use:

```bash
poetry shell
```

Now, you are ready to start working on the project!

## Commands

| Command                     | Description                                                |
|-----------------------------|------------------------------------------------------------|
| `poetry install`            | Installs the project dependencies.                         |
| `poetry shell`              | Activates the virtual environment.                         |
| `poetry run lint`           | Runs the linter (`flake8`) to check code quality.          |
| `poetry run pytest`           | Runs the tests using `pytest`.                            |
| `poetry run pytest --cov=my_library --cov-report=term-missing` | Runs tests with coverage report. |
| `sh ./scripts/build.sh`          | Obfuscates the code, builds the package, and creates a release under dist folder. |

## Development

### Running Functions

To run a function from commandline, you can use the following:

```bash
poetry run python -m my_library.base
```

This command runs the `base.py` module.

### Linting the Code

To ensure code quality, you can lint the codebase using `flake8`. This checks the code for stylistic errors and potential bugs.

Run the linter with:

```bash
poetry run lint
```

This will run `flake8` on the codebase and report any issues.

### Running Tests

To run the tests, use the following command:

```bash
poetry run test
```

This will execute all tests using `pytest` to ensure that everything is functioning correctly.

### Running Tests with Coverage Report

To generate a coverage report along with running the tests, use:

```bash
poetry run pytest --cov=my_library --cov-report=term-missing
```

This command will provide a detailed report of the test coverage, showing which parts of the codebase are covered by tests and which parts are not.

## Building the Project

*Build command is intended to run using github actions. When there is a new version with following `v*.*.*` pattern it will trigger build command and upload new release to github artifact*
To build the project, obfuscate the code, and package it, you can use the following command:

```bash
sh scripts/build.sh
```

This command will:
1. Obfuscate the code using `PyArmor`.
2. Build the package using Poetry.
3. Clean up the obfuscated code directory.
4. Add release files to `dist` directory.

## Continuous Integration and Deployment

### Linting and Testing

This project uses GitHub Actions to automatically lint and test the codebase whenever changes are pushed to the `main` branch or any branch matching the pattern `feature/*`.

#### Workflow: `linter_and_test.yaml`

The `linter_and_test.yaml` workflow is triggered on the following events:

- Pushing to the `main` branch.
- Pushing to any branch matching `feature/*`.
- Opening a pull request to the `main` branch.

**Jobs in this workflow:**

1. **Lint Code**:
   - Runs `flake8` to lint the code.

2. **Run Tests**:
   - Runs after the linting job.
   - Runs tests with `pytest` and generates a coverage report.

To see the results of this workflow, navigate to the "Actions" tab in your GitHub repository.

### Publishing Releases

This project also automates the process of publishing releases to GitHub when a new version tag is pushed.

#### Example Triggering Release

```bash
# Example version trigger
git add .
git commit -m "Commit for v0.0.1"
git push origin main

# Create a new tag for the release
git tag v0.0.1

# Push the commit and the tag to the remote repository
git push origin v0.0.1
```

#### Workflow: `release.yaml`

The `release.yaml` workflow is triggered when a new tag following the pattern `v*.*.*` is pushed. This workflow handles the versioning, building, and publishing of the package.

**Jobs in this workflow:**

1. **Build and Publish**:
   - Checks out the code.
   - Sets up Python 3.10.
   - Updates the version in `pyproject.toml` based on the tag.
   - Installs dependencies using Poetry.
   - Runs the `build.sh` script to obfuscate and build the package.
   - Creates a GitHub release with the new version tag.
   - Uploads the built package as a release asset.

To create a new release, simply  push a new tag following the pattern `v*.*.*`, and this workflow will handle the rest.

## Installing Released Package

package_name: my_library
version: 0.0.1

`https://github.com/{user_id}/{package_name}/releases/download/v{version}/my_library-{version}-py3-none-any.whl`

In order to install:
`pip install https://github.com/{user_id}/{package_name}/releases/download/v{version}/my_library-{version}-py3-none-any.whl`

## Documentation

### Viewing the Documentation

The project uses [MkDocs](https://www.mkdocs.org/) to manage and serve the documentation. To view the documentation locally, follow these steps:

1. **Install MkDocs**:
   If you haven't already installed MkDocs, you can do so by running:

   ```bash
   pip install mkdocs
   ```
2. **Run the MkDocs Server**: 
    Start the MkDocs development server by running the following command in the project root:

    ```bash
    mkdocs serve
    ```
    This will start the server on http://127.0.0.1:8000/. Open this address in your web browser to view the documentation.
    
3. **Build the Documentation**: 
  If you want to generate a static site version of the documentation, run:

    ```bash
    mkdocs build
    ```
    This will create a site/ directory with the static files.


## Private-PyPI

### Install Packages

The structure of the command to install the package is as follows:

```bash
pip install \
  --index-url http://{PYPI_USERNAME}:{PYPI_PASSWORD}@{PYPI_IP_ADDRESS}:{PYPI_PORT}/simple/ \
  --trusted-host {PYPI_IP_ADDRESS} \
  {PACKAGE}=={VERSION}

```

### Install With requirement.txt

You can fetch the package from the private PyPI by adding the following lines to the requirements.txt:

```bash
--index-url http://{PYPI_USERNAME}:{PYPI_PASSWORD}@{PYPI_IP_ADDRESS}:{PYPI_PORT}/simple/
--trusted-host {PYPI_IP_ADDRESS}
my-library=={VERSION}
```

### Manuel Upload Library Files

Install twine for upload:

```bash
pip install twine
```

Upload to private PyPI with twine lib:

```bash
twine upload \
  --repository-url {PYPI_IP_ADDRESS}:{PYPI_PORT} \
  -u {PYPI_USERNAME} \
  -p {PYPI_PASSWORD} \
  {.whl FILE PATH}
```

