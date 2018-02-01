""" Loads subcommands """
import os
import sys
import click

import osa.defaults
import osa.dynamicinventory.commands
import osa.staticinventory.commands

# Default context has only debug.
@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def entrypoint(ctx, debug):
    """ OpenStack-Ansible CLI tools """
    ctx.obj = dict(debug=debug)
    if debug:
        click.echo('Debug is on')

# Define the folder options only for the subcommands
# that need them. This way some plugins which don't
# require some folders won't bother us asking for
# those folders existence.
@entrypoint.group()
@osa.defaults.folder_options
@click.pass_context
def static_inventory(ctx, **kwargs):
    """ Tools for generating a static inventory """
    ctx.obj = osa.defaults.OSAContext(debug=ctx.obj['debug'], **kwargs)
    if ctx.obj.debug:
        click.echo("OpenStack-Ansible folder is %s" % ctx.obj.oadir)
        click.echo("User overrides folder is %s" % ctx.obj.userdir)
        click.echo("Work folder is %s" % ctx.obj.workdir)


# The dynamic inventory gets the default folder locations
# as options. This makes the folder locations available
# for all its sub commands
@entrypoint.group()
@osa.defaults.folder_options
@click.pass_context
def dynamic_inventory(ctx, **kwargs):
    """ Tools for manipulating the dynamic inventory """
    ctx.obj = osa.defaults.OSAContext(debug=ctx.obj['debug'], **kwargs)
    if ctx.obj.debug:
        click.echo("OpenStack-Ansible folder is %s" % ctx.obj.oadir)
        click.echo("User overrides folder is %s" % ctx.obj.userdir)
        click.echo("Work folder is %s" % ctx.obj.workdir)


# Wire up core features (subcommands)
_static_inventory_subcommands = [
    osa.staticinventory.commands.generate,
]
_dynamic_inventory_subcommands = [
    osa.dynamicinventory.commands.generate,
    osa.dynamicinventory.commands.host_list,
    osa.dynamicinventory.commands.group_list,
    osa.dynamicinventory.commands.view,
    osa.dynamicinventory.commands.replace_host_ip,
]
for subcommand in _static_inventory_subcommands:
    static_inventory.add_command(subcommand)
for subcommand in _dynamic_inventory_subcommands:
    dynamic_inventory.add_command(subcommand)


# Allowing up plugins for releases, bugtriage
# @entrypoint.command()
# @click.pass_obj
# def bug(obj):
#     click.echo("Need to implement plugin loading")
#     click.echo(obj['debug'])
# @entrypoint.command()
# @click.pass_obj
# def release(obj):
#     click.echo("Need to implement plugin loading")
#     click.echo(obj['debug'])
