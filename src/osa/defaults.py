""" Default assumptions for the cli """
import os


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
