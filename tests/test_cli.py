# This maps to cli/main.py
import os
import pytest
from click.testing import CliRunner
import osa.cli


# Testing fixtures
@pytest.fixture
def clickrunner():
    """ Initialize a cli runner function """
    return CliRunner()


# Testing tools
class Command(object):
    def __init__(self, entrypoint=None,
                 valid_args=None, invalid_args=None,
                 valid_subcmds=None, invalid_subcmds=None):
        self.entrypoint = entrypoint
        self.valid_args = valid_args
        self.invalid_args = invalid_args
        self.valid_subcmds = valid_subcmds
        self.invalid_subcmds = invalid_subcmds


maincli = Command(entrypoint=osa.cli.entrypoint,
                  valid_args=[
                      ['--debug'],
                  ],
                  invalid_args=[
                      ['--oadir', './oa'],
                  ],
                  valid_subcmds=[
                      'static_inventory',
                      'dynamic_inventory',
                  ],
                  invalid_subcmds=['babar'])
staticinventorycli = Command(valid_args=[
                                 ["--oadir", './oa'],
                                 ["--workdir", './work']
                             ],
                             invalid_args=[
                                 ['--debug']
                             ],
                             valid_subcmds=[
                                 'generate'
                             ],
                             invalid_subcmds=[
                                 'invert'
                             ])


# Tests definition
def test_import():
    """ Tests imports """
    assert True


def test_usage(clickrunner):
    """ Tests main cli can load and showing usage """
    result = clickrunner.invoke(maincli.entrypoint)
    assert result.exit_code == 0
    assert "Usage" in result.output
    for valid_subcmd in maincli.valid_subcmds:
        assert valid_subcmd in result.output
    for invalid_subcmd in maincli.invalid_subcmds:
        assert invalid_subcmd not in result.output


def test_validargs(clickrunner):
    """ Tests valid parameters with no subcommands """
    for args in maincli.valid_args:
        result = clickrunner.invoke(maincli.entrypoint, args)
        assert result.exit_code == 2
        assert "Missing command" in result.output


def test_invalidargs(clickrunner):
    """ Test invalid parameters with no subcommands """
    for args in maincli.invalid_args:
        result = clickrunner.invoke(maincli.entrypoint, args)
        assert result.exit_code == 2
        assert "no such option" in result.output


# static inventory
def test_usage_staticinventory(clickrunner):
    """ Test staticinventory cli can load and show its usage """
    result = clickrunner.invoke(maincli.entrypoint, ['static_inventory'])
    assert result.exit_code == 0
    assert "Usage" in result.output
    for valid_subcmd in staticinventorycli.valid_subcmds:
        assert valid_subcmd in result.output
    for invalid_subcmd in staticinventorycli.invalid_subcmds:
        assert invalid_subcmd not in result.output


def test_debug_staticinventory(clickrunner):
    """ Test that debug mode works in static_inventory """
    result = clickrunner.invoke(
        osa.cli.entrypoint, ['--debug', 'static_inventory', '--help'])
    assert result.exit_code == 0
    assert "Debug is on" in result.output