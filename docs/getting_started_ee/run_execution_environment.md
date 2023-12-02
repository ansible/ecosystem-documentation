# Running your EE

You can run your EE on the command line against `localhost` or a remote target using `ansible-navigator`.

> There are other tools besides `ansible-navigator` you can run EEs with.

## Run against localhost

1.  Create a `test_localhost.yml` playbook.

    ``` yaml
    cat > test_localhost.yml<<EOF
    - name: Gather and print local facts
      hosts: localhost
      become: true
      gather_facts: true
      tasks:

      - name: Print facts
        ansible.builtin.debug:
          var: ansible_facts
    EOF
    ```

2.  Run the playbook inside the `postgresql_ee` EE.

    ``` bash
    ansible-navigator run test_localhost.yml --execution-environment-image postgresql_ee --mode stdout --pull-policy missing --container-options='--user=0'
    ```

You may notice the facts being gathered are about the container and not the developer machine.
This is because the ansible playbook was run inside the container.

## Run against a remote target

Before you start, ensure you have the following:

  * At least one IP address or resolvable hostname for a remote target.
  * Valid credentials for the remote host.
  * A user with `sudo` permissions on the remote host.

Execute a playbook inside the `postgresql_ee` EE against a remote host machine as in the following example:

1. Create a directory for inventory files.

    ``` yaml
    mkdir inventory
    ```

2. Create the `hosts.yml` inventory file in the `inventory` directory.

    ``` yaml
    cat > inventory/hosts.yml<<EOF
    all:
      hosts:
        192.168.0.2  # Replace with the IP of your target host
    EOF
    ```

3. Create a `test_remote.yml` playbook.

    ``` yaml
    cat > test_remote.yml<<EOF
    - name: Gather and print facts
      hosts: all
      become: true
      gather_facts: true
      tasks:

      - name: Print facts
        ansible.builtin.debug:
          var: ansible_facts
    EOF
    ```

4. Run the playbook inside the `postgresql_ee` EE.

    Replace `student` with the appropriate username.
    Some arguments in the command can be optional depending on your target host authentication method.

    ``` bash
    ansible-navigator run test_remote.yml -i inventory --execution-environment-image postgresql_ee:latest --mode stdout --pull-policy missing --enable-prompts -u student -k -K
    ```

## See also

- [Execution Environment Definition](https://ansible-builder.readthedocs.io/en/stable/definition/) provides information about the about Execution Environment definition file and available options.
- [Ansible Builder CLI usage](https://ansible-builder.readthedocs.io/en/stable/usage/)
- [Ansible Navigator documentation](https://ansible-navigator.readthedocs.io/)
- [Running a local container registry for EEs](https://forum.ansible.com/t/running-local-container-registry-for-execution-environments/206)
