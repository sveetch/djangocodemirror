"""
Some fixture methods
"""
import os
import pytest

class FixturesStorageParameters(object):
    """Mixin containing some basic settings"""
    def __init__(self):
        # Base fixture datas directory
        self.tests_dir = 'project_test/tests'
        self.fixtures_dir = 'data_fixtures'

        self.tests_path = os.path.normpath(
            os.path.join(
                os.path.abspath(os.path.dirname(autobreadcrumbs.__file__)),
                '..',
                self.tests_dir,
            )
        )
        self.fixtures_path = os.path.join(
            self.tests_dir,
            self.fixtures_dir
        )


@pytest.fixture(scope='session')
def temp_builds_dir(tmpdir_factory):
    """Prepare a temporary build directory"""
    fn = tmpdir_factory.mktemp('builds')
    return fn


@pytest.fixture(scope="module")
def storageparameters():
    """Initialize and return parameters storage object (mostly paths) for
       fixtures (scope at module level)"""
    return FixturesStorageParameters()
