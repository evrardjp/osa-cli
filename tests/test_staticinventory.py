""" Tests all the functions of static inventory cli plugin """
import os
import pytest
from click.testing import CliRunner
import osa.cli
import osa.defaults


# Testing fixtures
@pytest.fixture
def clickrunner():
    """ Initialize a cli runner function """
    return CliRunner()


def test_debug(clickrunner):
    """ Test that debug mode shows the folders """
    result = clickrunner.invoke(
        osa.cli.entrypoint, ['--debug', 'static_inventory', 'generate'])
    assert result.exit_code == 0
    assert "OpenStack-Ansible folder is" in result.output
    assert osa.defaults.oadir in result.output
    assert "User overrides folder is" in result.output
    assert osa.defaults.userdir in result.output
    assert "Work folder is" in result.output
    assert osa.defaults.workdir in result.output