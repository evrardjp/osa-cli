""" Series of utilities for the CLI """
import os
import errno
import click
import json
import osa.defaults


def merge_dicts(x, y):
    """ Merge two dicts together, returns a new dict """
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


def pass_folder_locations(func):
    """ Decorates the function by passing previous context as first arg
        and standard folder locations as kwargs """
    for details in osa.defaults.folder_defaults.values():
        pathvars = merge_dicts(osa.defaults.default_path_vars,
                               details['pathparams'])
        func = click.option(details['paramtxt'],
                            type=click.Path(**pathvars),
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


def mktestdir(folder_data):
    """ Create test directories based on user data """
    for folderdetail in folder_data.values():
        folder = folderdetail['folder']
        print("Creating {}".format(folder))
        try:
            os.makedirs(folder)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise


class Inventory(object):
    """
    An inventory object represents an ansible inventory.
    It's loaded with the help of its json contents, which
    is expected to be JSON validated beforehand.

    It's not re-using ansible's methods because they fluctuate
    over time, while their interface (inventory structure)
    is relatively stable.

    groups values contains sub-groups, hostnames, and group vars
    hosts values contains hostvars
    """
    def __init__(self, jsoncontent=None):
        self.groups = dict()
        self.hosts = dict()

        if jsoncontent:
            self.load_inventoryjson(jsoncontent)

    def add_host(self, hostname, hostvars={}):
        """ Add host into our hosts dictionary
        when not known already.
        Host vars are abitrary and no validation
        is necessary, because JSON is already valid.
        """
        if not self.hosts.get(hostname):
            self.hosts[hostname] = hostvars

    def add_group(self, groupname, groupinfo):
        """
        Add a group into the inventory.
        This ensures the group can be added and group info
        only contains valid ansible info, for valid
        serialization later.
        """
        groupinfo = self.clean_group_structure(groupinfo)

        if not self.groups.get(groupname):
            self.groups[groupname] = groupinfo

    def clean_group_structure(self, groupinfo):
        valid_info = ['children', 'hosts', 'vars']
        validated_groupinfo = {}
        for info in valid_info:
            if groupinfo.get(info):
                validated_groupinfo[info] = groupinfo[info]
        return validated_groupinfo

    def load_inventoryjson(self, jsoncontent):
        # _meta is the only information outside group data
        hosts_metadata = jsoncontent.pop('_meta')
        if not isinstance(hosts_metadata.get('hostvars'), dict):
            raise UserWarning
        for hostname, hostvars in hosts_metadata['hostvars'].items():
            self.add_host(hostname, hostvars=hostvars)

        # Read the rest of the file.
        # groups are structured in json file as
        # groupname: {"children":[], "hosts": [], "vars": {}}

        # If no content remaining, that's a Black Flag.
        # We should at least have a group there, "all".
        if len(jsoncontent) == 0:
            raise UserWarning
        for groupname, groupinfo in jsoncontent.items():
            # Discover groups and their structure
            # Do not discover children, they will be discovered by
            # looping through the jsoncontent.
            self.add_group(groupname, groupinfo)

            # Auto-add new hosts (hosts with no metadata).
            for hostname in groupinfo.get('hosts', []):
                self.add_host(hostname)

    def serialize_inventory(self):
        """ Generates the inventory.json structure """
        output = dict()
        output['_meta'] = dict()
        output['_meta']['hostvars'] = self.hosts
        output.update(self.groups)
        return output
