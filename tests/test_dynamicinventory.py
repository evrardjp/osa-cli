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
    for foldertype in osa.defaults.folder_defaults.values():
        print("Creating {}".format(foldertype))
        try:
            os.makedirs(foldertype['folder'])
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    return click.testing.CliRunner()


def test_debug(clickrunner):
    """ Test that debug mode shows the default folders """
    result = clickrunner.invoke(
        osa.cli.entrypoint, ['--debug', 'dynamic_inventory', 'generate'])
    print(result.output)
    assert "OpenStack-Ansible folder is" in result.output
    assert "User overrides folder is" in result.output
    assert "Work folder is" in result.output
    for foldertype in osa.defaults.folder_defaults.values():
        assert foldertype['folder'] in result.output
    assert result.exit_code == 0
    # TODO test overrides


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
