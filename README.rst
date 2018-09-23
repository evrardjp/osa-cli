This is a CLI tool that will be used for multiple OSA commands

It can be extended with your own commands by adding them to the proper entry point (osa_cli.plugins).
This CLI has the following default plugins (WIP):
- Tools to display/manipulate dynamic inventory
- Tools to generate a OSA static inventory based on some current inventory (auto assignment of groups)

It is expected to evolve over time with the following:
- Have a CLI for upgrades:
  This would basically load a file containing the information about the plays to run, which are branch specific.
  The CLI would be in charge of running said plays with a little twist: It would at the same time load a strategy plugin to keep track of what was successfully upgraded.
  This CLI would be able to report the status of the upgrade (by reading the markers), and clean the upgrade markers should a step be manually retried.
- Have a CLI for parallel runs:
  This basically loads the current plays of setup-everything, but with a specific strategy plugin which would keep semaphores for certain tasks, like apt which requires locks.
  This would allow a parallel processing of those plays without hitting failures. This CLI should have a specific set of rules of what to run in parallel, and what to not
  run in parallel.

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
