""" Tests all the functions of dynamic inventory cli plugin """
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
        osa.cli.entrypoint, ['--debug', 'dynamic_inventory', 'generate'])
    assert result.exit_code == 0
    assert "OpenStack-Ansible folder is" in result.output
    assert osa.defaults.oadir in result.output
    assert "User overrides folder is" in result.output
    assert osa.defaults.userdir in result.output
    assert "Work folder is" in result.output
    assert osa.defaults.workdir in result.output


def test_hostlist(clickrunner):
    """ Test invoking host_list cli """
    result = clickrunner.invoke(
        osa.cli.entrypoint, ['--debug', 'dynamic_inventory', 'host_list'])
    assert result.exit_code == 0


def test_grouplist(clickrunner):
    """ Test invoking group_list cli """
    result = clickrunner.invoke(
        osa.cli.entrypoint, ['--debug', 'dynamic_inventory', 'group_list'])
    assert result.exit_code == 0


def test_view(clickrunner):
    """ Test invoking view cli """
    result = clickrunner.invoke(
        osa.cli.entrypoint, ['--debug', 'dynamic_inventory', 'view'])
    assert result.exit_code == 0


def test_replacehostip(clickrunner):
    """ Test invoking replace_host_ip cli """
    result = clickrunner.invoke(
        osa.cli.entrypoint, ['--debug', 'dynamic_inventory', 'replace_host_ip'])
    assert result.exit_code == 0