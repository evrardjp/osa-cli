""" Series of utilities for the CLI """
import os
import errno
import click
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
