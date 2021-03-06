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

@static_inventory.command()
@click.pass_obj
def generate(global_ctx):
    """ Dumbly assigns nodes in groups based on name patterns"""
    pass
    # name_patterns = {
    #     'keystone': '.*keystone.*'
    #     'nova': '.*nova.*'
    #     'controller': ['.*infra.*','.*controller.*']
    # }
    # types = list(name_patterns.keys())
    # nodes = set()
    # with open(filename, 'r') as node_file:
    #     for node in node_file.read():
    #         nodes.add(node)
    # compile list of regexps
    # iterate across regexps (because it's like a priority list)
    #   if host match regexp, remove host from unassigned set,
    #     and add it to the appropriate groupname.
    #   if host doesn't match, continue to next host.
    # when all regexp are done, check if they are still hosts in
    # the unassigned set.
    # If there are, move those nodes to 'unassigned' group.
    # Else be happy

    # This can also be fully replaced with an ansible play:
    # loading the current inventory grouping hosts by names,
    # and templating the new group results into a new inventory.
    # Easier to read.

