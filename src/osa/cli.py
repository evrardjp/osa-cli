""" Loads subcommands """
import pkg_resources
import click
from click_plugins import with_plugins


@with_plugins(pkg_resources.iter_entry_points('osa_cli.plugins'))
@click.group()
@click.option('--debug/--no-debug', default=False)
# pass_context will allow the modification of the ctx object
# so that plugins can receive it, should they care...
# The only global context object is debug.
@click.pass_context
def entrypoint(ctx, debug):
    """ OpenStack-Ansible CLI tools """
    ctx.obj = dict(debug=debug)
    if debug:
        click.echo('Debug is on')
