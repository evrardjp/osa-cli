""" Loads subcommands """
import os
import sys
import click

from .staticinventory import commands as staticinventorycli
from .dynamicinventory import commands as dynamicinventorycli


@click.group()
def entrypoint():
    """ OpenStack-Ansible CLI tools """
    pass


@entrypoint.group()
def static_inventory():
    """ Tools for generating a static inventory """
    pass


@entrypoint.group()
def dynamic_inventory():
    """ Tools for manipulating the dynamic inventory """
    pass

static_inventory.add_command(staticinventorycli.convert)
dynamic_inventory.add_command(dynamicinventorycli.generate)
