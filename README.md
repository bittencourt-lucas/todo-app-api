# To-Do App API

The API for a To-Do App, meant to be a study of Python's [FastAPI](https://fastapi.tiangolo.com/), application of software engineering principles such as SOLID and Clean Architecture, and training automatized testing and TDD.

## Dependencies

This project was built using the following:

- Python==3.10.9
- FastAPI==0.94.1
- uvicorn==0.21.1
- python-dotenv==1.0.0
- SQLAlchemy==2.0.6
- alembic==1.10.2

## Running the Project

### Preparing the environment

> 🚧 The instructions are meant to be used with a bash/zsh shell. If you are using a different shell, refer to: https://docs.python.org/3/library/venv.html

To create the environment, run `python3 venv venv`, and to activate it run `source venv/bin/activate`.

To install all the project's requirements, run `pip install -r /path/to/requirements.txt`.

To execute the project's migrations, run `alembic upgrade head`.

### Running the environment locally

First, follow the instructions presented in the `Preparing the environment` section.

After that, run `uvicorn src.shared.main:app --reload --port=8080`.

### Deploying the environment

> 🚧 The instructions are meant to be used with Google Cloud Platform's App Engine. If you are using a different cloud provider, check the instructions specific to that provider.

First, follow the instructions presented in the `Preparing the environment` section.

Once you are done with that, you just need to run `gcloud app deploy`.
