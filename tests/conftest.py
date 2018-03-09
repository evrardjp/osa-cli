""" Global testing fixtures """
import pytest
import click
import osa.defaults
import osa.utils


@pytest.fixture(scope="session")
def clickrunner():
    """ Initialize a cli runner function with a standard env"""
    osa.utils.mktestdir(osa.defaults.folder_defaults)
    return click.testing.CliRunner()