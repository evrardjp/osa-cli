""" Tests all the functions of dynamic inventory cli plugin """
import osa
import click
import pytest
import itertools


bare_subcommands = [
    'generate',
    'host_list',
    'group_list',
    'view',
    'replace_host_ip',
]
folder_overrides = {
    'oa': {
        'paramtxt': '--oadir',
        'folder': '.tox/tmp/o-a'
    },
    'user': {
        'paramtxt': '--userdir',
        'folder': '.tox/tmp/o_d'
    },
    'work': {
        'paramtxt': '--workdir',
        'folder': '.tox/tmp/work'
    }
}


@pytest.mark.parametrize("param", bare_subcommands)
def test_debug_defaultdirs(clickrunner, param):
    """ Test that debug mode shows the default folders """
    result = clickrunner.invoke(
        osa.cli.entrypoint, ['--debug', 'dynamic_inventory', param])
    print(result.output)
    assert "Debug is on" in result.output
    assert "OpenStack-Ansible folder is" in result.output
    assert "User overrides folder is" in result.output
    assert "Work folder is" in result.output
    for foldertype in osa.defaults.folder_defaults.values():
        assert foldertype['folder'] in result.output
    assert result.exit_code == 0


@pytest.mark.parametrize("param", bare_subcommands)
def test_debug_userdirs(param):
    """ Test that debug mode shows the user defined folders """
    osa.utils.mktestdir(folder_overrides)
    cliargs = ['--debug', 'dynamic_inventory']
    call = []

    # Test all combinations of the 3 parameters.
    for combination in itertools.combinations_with_replacement(
            folder_overrides.keys(), len(folder_overrides)):
        # flatten the combinations to avoid passing x times the same argument
        folderargs = set()
        folderargs.update(combination)
        del call[:]
        call.extend(cliargs)
        for element in folderargs:
            call.append(folder_overrides[element]['paramtxt'])
            call.append(folder_overrides[element]['folder'])
        call.append(param)
        print(folderargs)
        result = click.testing.CliRunner().invoke(
            osa.cli.entrypoint, call)
        assert result.exit_code == 0
        assert "Debug is on" in result.output
        for element in folderargs:
            assert folder_overrides[element]['folder'] in result.output


def test_show_usage():
    """ Test that no subcommand shows the usage """

    osa.utils.mktestdir(folder_overrides)
    result = click.testing.CliRunner().invoke(
        osa.cli.entrypoint, ['dynamic_inventory'])
    assert "Usage:" in result.output
