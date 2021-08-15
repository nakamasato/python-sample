# Python Sample

Sample Python app with tests.

## Tests and Directory

There are two main approaches about where to put test codes:

1. Tests outside application code

    > This is problematic if you are using a tool like tox to test your package in a virtual environment, because you want to test the installed version of your package, not the local code from the repository.
    > In this situation, it is strongly suggested to use a src layout where application root package resides in a sub-directory of your root:

    ```
    setup.py
    src/
        mypkg/
            __init__.py
            app.py
            view.py
    tests/
        __init__.py
        foo/
            __init__.py
            test_view.py
        bar/
            __init__.py
            test_view.py
    ```

    Benefits:
    - Your tests can run against an installed version after executing pip install .
    - Your tests can run against the local copy with an editable install after executing pip install --editable ..
    - If you don’t have a setup.py file and are relying on the fact that Python by default puts the current directory in sys.path to import your package, you can execute python -m pytest to execute the tests against the local copy directly, without using pip.

    Drawbacks:
    - if you are using prepend import mode (which is the default)

1. Tests as part of application code


    ```
    setup.py
    mypkg/
        __init__.py
        app.py
        view.py
        test/
            __init__.py
            test_app.py
            test_view.py
            ...
    ```

## Local env

https://docs.python.org/3/library/venv.html

```
python3 -m venv python-sample-env
. ./python-sample-env/bin/activate
```

## Run test

```
make init # install dependency
make test
```

## Reference

- Integration test with Docker: https://pypi.org/project/pytest-docker/
- Good practice: https://docs.pytest.org/en/stable/goodpractices.html#tox
- pytest with tox: https://tox.readthedocs.io/en/latest/example/pytest.html
