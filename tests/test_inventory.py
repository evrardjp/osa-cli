import json
import os
import pytest
import osa.utils


inventories = [
    'empty-inventory.json',
    'pike-aio-inventory.json',
]

expected_amount_of_hosts = [0, 24]
expected_amount_of_groups = [1, 257]


def test_load_no_inventory():
    """ Ensure inventory can be loaded with no json
    """
    osa.utils.Inventory()


@pytest.mark.parametrize("inventory", inventories)
def test_load_inventory(inventory):
    """ Ensure a series of inventories can load
    """
    with open(os.path.join(os.path.dirname(__file__), inventory)) as fdesc:
        fcon = fdesc.read()
        osa.utils.Inventory(json.loads(fcon))


@pytest.mark.parametrize("inventory, amountofhosts, amountofgroups",
                         zip(inventories,
                             expected_amount_of_hosts,
                             expected_amount_of_groups,
                             ))
def test_inventory_size(inventory, amountofhosts, amountofgroups):
    """ Ensure the inventories are at the right size
    """
    with open(os.path.join(os.path.dirname(__file__), inventory)) as fdesc:
        fcon = fdesc.read()

    inventory = osa.utils.Inventory(json.loads(fcon))
    assert len(inventory.hosts) == amountofhosts
    assert len(inventory.groups) == amountofgroups


def test_cleanup_group():
    """ Ensure only the valid group data is accepted in group"""
    with open(os.path.join(os.path.dirname(__file__),
              'unclean-inventory1.json')) as fd:
        fc = json.loads(fd.read())
    cleaninventory = osa.utils.Inventory(fc)
    assert cleaninventory.groups['machin'].get('extraunusedkey') is None


malformed_inventories = [
    # _meta has no hostvars
    ('malformed-inventory1.json', UserWarning),
    # No _meta key
    ('malformed-inventory2.json', KeyError),
    # No groups, not even all.
    ('malformed-inventory3.json', UserWarning),    
]


@pytest.mark.parametrize("inventory, failurereason", malformed_inventories)
def test_malformed_inventory(inventory, failurereason):
    """ Ensure malformed inventory throw exceptions """
    with open(os.path.join(os.path.dirname(__file__), inventory)) as fdesc:
        fcon = fdesc.read()
    with pytest.raises(failurereason):
        osa.utils.Inventory(json.loads(fcon))


def test_serialize_inventory():
    """
    Ensure the inventory has a structure matching
    Ansible expectations
    """
    craftedinventory = osa.utils.Inventory()
    craftedinventory.add_host("bidule")
    craftedinventory.add_group("all", json.loads('{"children": ["bidule"] }'))
    output = craftedinventory.serialize_inventory()
    expected_output = json.loads('{"_meta": {"hostvars": {"bidule": {}}}, "all": {"children": ["bidule"]}}')
    assert expected_output == output


def test_add_host():
    """
    Ensure adding hosts adds a proper node
    """
    with open(os.path.join(os.path.dirname(__file__),
              inventories[1])) as fd:
        pike_inventory = osa.utils.Inventory(json.loads(fd.read()))
    pike_inventory.add_host('aio2')
    assert len(pike_inventory.hosts) == expected_amount_of_hosts[1]+1
    assert 'aio2' in \
        pike_inventory.serialize_inventory()['_meta']['hostvars'].keys()

