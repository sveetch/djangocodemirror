"""
Pytest fixtures
"""
from pathlib import Path

import pytest

import djangocodemirror
from djangocodemirror.manifest import CodeMirrorManifest


class FixturesSettingsTestMixin(object):
    """
    A mixin containing settings about application. This is almost about useful
    paths which may be used in tests.

    Attributes:
        application_path (pathlib.Path): Absolute path to the application directory.
        package_path (pathlib.Path): Absolute path to the package directory.
        tests_dir (pathlib.Path): Directory name which include tests.
        tests_path (pathlib.Path): Absolute path to the tests directory.
        fixtures_dir (pathlib.Path): Directory name which include tests datas.
        fixtures_path (pathlib.Path): Absolute path to the tests datas.
    """
    def __init__(self):
        self.application_path = Path(
            djangocodemirror.__file__
        ).parents[0].resolve()
        self.application_urlpath = ""

        self.package_path = self.application_path.parent

        self.tests_dir = "tests"
        self.tests_path = self.package_path / self.tests_dir

        self.fixtures_dir = "data_fixtures"
        self.fixtures_path = self.tests_path / self.fixtures_dir

    def format(self, content):
        """
        Format given string to include some values related to this application.

        Arguments:
            content (str): Content string to format with possible values.

        Returns:
            str: Given string formatted with possible values.
        """
        return content.format(
            HOMEDIR=Path.home(),
            PACKAGE=str(self.package_path),
            APPLICATION=str(self.application_path),
            TESTS=str(self.tests_path),
            FIXTURES=str(self.fixtures_path),
            VERSION=djangocodemirror.__version__,
        )


@pytest.fixture(scope="function")
def temp_builds_dir(tmp_path):
    """
    Prepare a temporary build directory.

    NOTE: You should use directly the "tmp_path" fixture in your tests.
    """
    return tmp_path


@pytest.fixture(scope="module")
def tests_settings():
    """
    Initialize and return settings for tests.

    Example:
        You may use it in tests like this: ::

            def test_foo(tests_settings):
                print(tests_settings.package_path)
                print(tests_settings.format("Application version: {VERSION}"))
    """
    return FixturesSettingsTestMixin()


@pytest.fixture(scope="function")
def manifesto():
    """
    Return a CodeMirrorManifest instance
    """
    return CodeMirrorManifest()
