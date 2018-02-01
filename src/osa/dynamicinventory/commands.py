""" Tools for dynamic inventories """
import click


@click.command()
def generate():
    """ Generates /etc/openstack_deploy/openstack_inventory.json """
    pass


@click.command()
def host_list():
    """ Lists all hosts """
    pass


@click.command()
def group_list():
    """ Lists all groups """
    pass


@click.command()
def view():
    """ Lists hosts with their groups """
    pass


@click.command()
def replace_host_ip():
    """ Edit host IP """
    pass
