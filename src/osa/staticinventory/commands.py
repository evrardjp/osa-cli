""" Tools for static inventories """
import click


@click.command('convert',
               short_help='Converts openstack_inventory.json -> yaml files')
def convert():
    """ Converts openstack_inventory.json to a static inventory structure"""
    pass