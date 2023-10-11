# Building your first Execution Environment

We are going to build an EE that represents an Ansible control node containing standard packages such as `ansible-core` and Python in addition to an Ansible collection (`community.postgresql`) and its dependency (the `psycopg2-binary` Python connector).

To build your first EE:

1. Create a project folder on your filesystem.

    ``` bash
    mkdir my_first_ee && cd my_first_ee
    ```

2. Create a `execution-environment.yml` file that specifies dependencies to include in the image.

    ``` yaml
    cat > execution-environment.yml<<EOF
    version: 3

    images:
      base_image:
        name: quay.io/fedora/fedora:latest

    dependencies:
      ansible_core:
        package_pip: ansible-core
      ansible_runner:
        package_pip: ansible-runner
      system:
      - openssh-clients
      - sshpass
      galaxy:
        collections:
        - name: community.postgresql
    EOF
    ```

    > The `psycopg2-binary` Python package is included in the `requirements.txt` file for the collection.
    > For collections that do not include `requirements.txt` files, you need to specify Python dependencies explicitly.
    > See the [Ansible Builder documentation](https://ansible-builder.readthedocs.io/en/stable/definition/) for details.

3. Build a EE container image called `postgresql_ee`.

    If you use docker, add the `--container-runtime docker` argument.

    ``` bash
    ansible-builder build --tag postgresql_ee
    ```

4. List container images to verify that you built it successfully.

    ``` bash
    podman image list

    localhost/postgresql_ee          latest      2e866777269b  6 minutes ago  1.11 GB
    ```

You can verify the image you created by inspecting the `Containerfile` or `Dockerfile` in the `context` directory to view its configuration.

``` bash
less context/Containerfile
```

You can also use Ansible Navigator to view detailed information about the image.

Run the `ansible-navigator` command, type `:images` in the TUI, and then choose `postgresql_ee`.

Proceed to [Running your EE](run_execution_environment.md) and test the EE you just built.
