import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

@pytest.mark.parametrize('package', [
  'iptables'
])
def test_iptables_is_present(host):
    iptables = host.package(package)

    assert iptables.is_installed

@pytest.mark.parametrize('service', [
  'iptables'
])
def test_iptables_service_is_started(host):
    service = host.service(service)

    assert service.is_running
    assert service.is_enabled
