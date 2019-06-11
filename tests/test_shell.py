from .main import run_data


def test_python_main():
    if not run_data("FAKE DATA") == None:
        raise AssertionError()  # pragma: no cover
