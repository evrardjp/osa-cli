""" Tools for static inventories """
import click


@click.command('generate',
               short_help='Converts openstack_inventory.json -> yaml files')
@click.pass_obj
def generate(osactx):
    """ Converts openstack_inventory.json to a static inventory structure"""
    click.echo(osactx.oadir)