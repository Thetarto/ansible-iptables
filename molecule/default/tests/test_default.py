import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_iptables_is_present(host):
    iptables = host.package(iptables)

    assert iptables.is_installed

def test_iptables_service_is_started(host):
    service = host.service(iptables)

    assert service.is_running
    assert service.is_enabled
