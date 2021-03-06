""" Tools for dynamic inventories """
import click
import osa.utils as utils


# The dynamic inventory gets the default folder locations
# as options. This makes the folder locations available
# for all its sub commands
# @osa.cli.entrypoint.group()
@click.group()
@utils.pass_folder_locations
def dynamic_inventory(ctx, **kwargs):
    """ Tools for manipulating the dynamic inventory """
    ctx.obj = utils.OSAContext(debug=ctx.obj['debug'], **kwargs)
    if ctx.obj.debug:
        click.echo("OpenStack-Ansible folder is %s" % ctx.obj.oadir)
        click.echo("User overrides folder is %s" % ctx.obj.userdir)
        click.echo("Work folder is %s" % ctx.obj.workdir)


@dynamic_inventory.command()
def generate():
    """ Generates openstack_inventory.json """
    pass


@dynamic_inventory.command()
def host_list():
    """ Lists all hosts """
    pass


@dynamic_inventory.command()
def group_list():
    """ Lists all groups """
    pass


@dynamic_inventory.command()
def view():
    """ Lists hosts with their groups """
    pass


@dynamic_inventory.command()
def replace_host_ip():
    """ Edit host IP """
    pass

@dynamic_inventory.command()
def convert():
    """ Convert inventory.json to inventory.yaml """
    pass
