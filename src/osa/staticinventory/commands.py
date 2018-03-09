""" Tools for static inventories """
import click
import osa.defaults
import osa.utils as utils

# Define the folder options only for the subcommands
# that need them. This way some plugins which don't
# require some folders won't bother us asking for
# those folders existence.
# The static inventory gets the default folder locations
# as options. This makes the folder locations available
# for all its sub commands
@click.group()
@utils.pass_folder_locations
def static_inventory(ctx, **kwargs):
    """ Tools for generating a static inventory """
    ctx.obj = utils.OSAContext(debug=ctx.obj['debug'], **kwargs)
    if ctx.obj.debug:
        click.echo("OpenStack-Ansible folder is %s" % ctx.obj.oadir)
        click.echo("User overrides folder is %s" % ctx.obj.userdir)
        click.echo("Work folder is %s" % ctx.obj.workdir)


@static_inventory.command('generate',
                          short_help='Converts openstack_inventory.json -> yaml files')
@click.pass_obj
def generate(osactx):
    """ Converts openstack_inventory.json to a static inventory structure"""
    click.echo(osactx.oadir)
