# To-Do App API

The API for a To-Do App, meant to be a study of Python's FastAPI, application of software engineering principles such as SOLID and Clean Architecture, and training automatized testing and TDD.

## Dependencies

This project was built using the following:

- Python 3.10.9
- FastAPI 0.94.1

## Running the Project

### Preparing the environment

> 🚧 The instructions are meant to be used with a bash/zsh shell. If you are using a different shell, refer to: https://docs.python.org/3/library/venv.html

To create the environment, run `python3 venv venv`, and to activate it run `source venv/bin/activate`.

To install [FastAPI](https://fastapi.tiangolo.com/), run `pip install fastapi`.

To install the Asynchronous Server Gateway Interface (ASGI), run `pip install "uvicorn[standard]"`.

### Running the environment locally

First, follow the instructions presented in the `Preparing the environment` section.

After that, run `uvicorn src.shared.main:app --reload --port=8080`.

### Deploying the environment

> 🚧 The instructions are meant to be used with Google Cloud Platform's App Engine. If you are using a different cloud provider, check the instructions specific to that provider.

First, follow the instructions presented in the `Preparing the environment` section.

After that, run `pip install gunicorn`.

Finally, you just need to run `gcloud app deploy`.
