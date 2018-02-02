""" Tests all the functions of dynamic inventory cli plugin """
import errno
import os
import pytest
import click


try:
    import osa.cli
    import osa.defaults
except ImportError:
    print("Module import error")


# Testing fixtures
@pytest.fixture
def clickrunner():
    """ Initialize a cli runner function with a standard env"""
    for folder in [osa.defaults.oadir,
                   osa.defaults.userdir,
                   osa.defaults.workdir]:
        try:
            os.makedirs(folder)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    return click.testing.CliRunner()


def test_debug(clickrunner):
    """ Test that debug mode shows the folders """
    result = clickrunner.invoke(
        osa.cli.entrypoint, ['--debug', 'dynamic_inventory', 'generate'])
    print(result.output)
    assert "OpenStack-Ansible folder is" in result.output
    assert osa.defaults.oadir in result.output
    assert "User overrides folder is" in result.output
    assert osa.defaults.userdir in result.output
    assert "Work folder is" in result.output
    assert osa.defaults.workdir in result.output
    assert result.exit_code == 0


def test_hostlist(clickrunner):
    """ Test invoking host_list cli """
    result = clickrunner.invoke(
        osa.cli.entrypoint, ['--debug', 'dynamic_inventory', 'host_list'])
    print(result.output)
    assert result.exit_code == 0


def test_grouplist(clickrunner):
    """ Test invoking group_list cli """
    result = clickrunner.invoke(
        osa.cli.entrypoint, ['--debug', 'dynamic_inventory', 'group_list'])
    print(result.output)
    assert result.exit_code == 0


def test_view(clickrunner):
    """ Test invoking view cli """
    result = clickrunner.invoke(
        osa.cli.entrypoint, ['--debug', 'dynamic_inventory', 'view'])
    print(result.output)
    assert result.exit_code == 0


def test_replacehostip(clickrunner):
    """ Test invoking replace_host_ip cli """
    result = clickrunner.invoke(
        osa.cli.entrypoint, ['--debug', 'dynamic_inventory', 'replace_host_ip'])
    print(result.output)
    assert result.exit_code == 0
