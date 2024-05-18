

# What is Fallible
It is an experimental build of Ansible core, enable you to expereince what might become the new Ansible core by playing around with experimental feature that were merged during development cycle. With this we are able to monitors the performance of an experimental feature merged before deploying to production.

Fallible is build to function as the same as Ansible core, but you don't have to do anything important with it. Rather than building ansible from source before you get to expereince a feature that might likely be dropped during production we request you make use of fallible to experience an experimental feature that might possible be merged to production.

Instead of using `Ansible --version` use `Fallible --version`, all command that using ansible are now beign use with fallible.
The development is base on the ansible [core 2.15.0.dev0] and uses cava for build to show details about when it was build and what it contains. This is clearly a different version to the Ansible core version, it is the integration build of numbers of PRs with random bit of core develop.

Here we display the experimental features that were merged with the fallible build for you to play around with, and they are:
- [POC] Add Projection features for registery vars - Option 2: https://github.com/ansible/ansible/pull/72553
- [POC] Support unpackage loop vars: https://github.com/ansible/ansible/pull/74529
- [POC] ASCII Splash: https://github.com/ansible/ansible/pull/77489
- [POC] Add loop_control.lookup: https://githun.com/ansible/ansible/pull/77614

# Why use Fallible
To use fallible, you have to understand it is an experimental build used for expereincing newly build features that has been merged and yet to be deployed to production. We don't advice you use fallible for important things, use it to gain understanding of the merged feature while we monitor the performance before deploying to production.

# Fallible-compat
Is a package once instance provides you with the `ansible` entrypoint and you should be able to call ansible command.

# How to use Fallible


