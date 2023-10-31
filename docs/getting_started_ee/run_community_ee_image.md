# Running Ansible with the community EE image

You can run ansible without the need to build a custom EE using
community images.
Use the `community-ee-minimal` image that includes only `ansible-core` or the `community-ee-base` image that also includes several base collections.

Run the following command to see the collections included in the `community-ee-base` image:

``` bash
ansible-navigator collections --execution-environment-image ghcr.io/ansible-community/community-ee-base:latest
```

Run the following Ansible ad-hoc command against localhost inside the `community-ee-minimal` container:

``` bash
ansible-navigator exec "ansible localhost -m setup" --execution-environment-image ghcr.io/ansible-community/community-ee-minimal:latest --mode stdout
```

Now, create a simple test playbook and run it against localhost inside the container:

``` yaml
cat > test_localhost.yml<<EOF
- name: Gather and print local facts
  hosts: localhost
  become: yes
  gather_facts: yes
  tasks:

  - name: Print facts
    ansible.builtin.debug:
      var: ansible_facts
EOF
```

``` bash
ansible-navigator run test_localhost.yml --execution-environment-image ghcr.io/ansible-community/community-ee-minimal:latest --mode stdout
```

Want to discuss the community EE images and other EE-related topics? Join the [forum group](https://forum.ansible.com/g/ExecutionEnvs)!

## See also

- [Building your first EE](build_execution_environment.md)
- [Running your EE](run_execution_environment.md)
- [Ansible Navigator documentation](https://ansible-navigator.readthedocs.io/)
