""" utilities used for the cli tool """
import os
import click

debug = False
oadir = os.environ.get('OPENSTACK_ANSIBLE_FOLDER') or '/opt/openstack-ansible'
userdir = os.environ.get('OPENSTACK_DEPLOY_FOLDER') or '/etc/openstack_deploy'
workdir = os.environ.get('OPENSTACK_WORK_FOLDER') or '/tmp/osa'

_folder_options = [
    click.option('--oadir',
                 type=click.Path(exists=True, file_okay=False,
                                 dir_okay=True, resolve_path=True),
                 help='OpenStack-Ansible folder location',
                 default=oadir,
                 show_default=True),
    click.option('--userdir',
                 type=click.Path(file_okay=False, dir_okay=True,
                                 writable=True, resolve_path=True),
                 help='openstack_deploy folder location',
                 default=userdir,
                 show_default=True),
    click.option('--workdir',
                 type=click.Path(file_okay=False, dir_okay=True,
                                 writable=True, resolve_path=True),
                 help='Work directory',
                 default=workdir,
                 show_default=True),
]


def folder_options(func):
    """ Decorate the function with the standard folder options """
    for option in reversed(_folder_options):
        func = option(func)
    return func


class OSAContext(object):
    def __init__(self, debug=debug,
                 oadir=oadir,
                 userdir=userdir,
                 workdir=workdir):
        self.debug = debug
        self.oadir = oadir
        self.userdir = userdir
        self.workdir = os.path.abspath(workdir)