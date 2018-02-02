
Requirements:
- /etc/openstack_deploy folder exists and writable.
  If you want to use another folder, set --userdir in your command line.
  If you don't want to use --userdir, the gating system uses the environment variable OPENSTACK_DEPLOY_FOLDER to switch the default location to a non-root writable location
- /opt/openstack-ansible folder exists and readable.
  If you want to use another folder, set --oadir in your command line.
  If you don't want to use --oadir, the gating system uses the environment variable OPENSTACK_ANSIBLE_FOLDER to switch the default location to a non-root writable location
- /tmp/osa folder exists and writable.
  If you want to use another folder, set --workdir in your command line.
  If you don't want to use --workdir, the gating system uses the environment variable OPENSTACK_WORK_FOLDER to switch the default location to a non-root writable location
