Postgresql Client
=================

[![Actions Status](https://github.com/ome/ansible-role-postgresql-client/workflows/Molecule/badge.svg)](https://github.com/ome/ansible-role-postgresql-client/actions)
[![Ansible Role](https://img.shields.io/ansible/role/47052.svg)](https://galaxy.ansible.com/ome/postgresql-client/)

Install PostgreSQL clients from the upstream distribution.

If you wish to use your distributions packages do not use this role.


Role Variables
--------------

Required:
- `postgresql_version`: The PostgreSQL major version, e.g. `10`, `11`, `12`, `13`, `14`

Optional:
- `postgresql_package_version`: The PostgreSQL full version, ignored on Ubuntu, e.g. `12.11`


Example Playbook
----------------

    # Simple example relying on the default Postgres PUBLIC privileges
    # which allow access to all users
    - hosts: localhost
      roles:
      - role: ome.postgresql_client
        postgresql_version: "12"


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
