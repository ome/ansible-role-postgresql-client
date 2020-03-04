import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def get_version(hostname):
    ver_lookup = {
        "postgresql96": "9.6",
        "postgresql10": "10",
        "postgresql11": "11",
        "postgresql12": "12",
    }
    return ver_lookup[hostname]


def test_psql_version(host):
    ver = get_version(host.backend.get_hostname())
    out = host.check_output('psql --version')
    assert out.startswith('psql (PostgreSQL) {}.'.format(ver))
