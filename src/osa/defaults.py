""" utilities used for the cli tool """
import os
import click


default_path_vars = dict(exists=True, file_okay=False,
                         dir_okay=True, resolve_path=True)
folder_defaults = {
    'oa': {
        'paramtxt': '--oadir',
        'helptxt': 'OpenStack-Ansible folder location',
        'pathparams': {},
        'folder': (os.environ.get('OPENSTACK_ANSIBLE_FOLDER') or
                   '/opt/openstack-ansible'),
    },
    'user': {
        'paramtxt': '--userdir',
        'helptxt': 'openstack_deploy folder location',
        'pathparams': {'writable': True},
        'folder': (os.environ.get('OPENSTACK_DEPLOY_FOLDER') or
                   '/etc/openstack_deploy'),
    },
    'work': {
        'paramtxt': '--workdir',
        'helptxt': 'Work directory',
        'pathparams': {'writable': True},
        'folder': (os.environ.get('OPENSTACK_WORK_FOLDER') or
                   '/tmp/osa'),
    }
}


def merge_dicts(x, y):
    """ Merge two dicts together, returns a new dict """
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


def pass_folder_locations(func):
    """ Decorates the function by passing previous context as first arg
        and standard folder locations as kwargs """

    for details in folder_defaults.values():
        temp = merge_dicts(default_path_vars, details['pathparams'])
        func = click.option(details['paramtxt'],
                            type=click.Path(**temp),
                            help=details['helptxt'],
                            default=details['folder'],
                            show_default=True)(func)
    func = click.pass_context(func)
    return func


class OSAContext(object):
    def __init__(self, **kwargs):
        self.debug = kwargs['debug']
        self.oadir = kwargs['oadir']
        self.userdir = kwargs['userdir']
        self.workdir = kwargs['workdir']
