# Topgrade Watcher

This repository automatically tracks the latest version of the [Topgrade](https://github.com/topgrade-rs/topgrade) utility and updates the `topgrade.spec` file and trigger [Fedora Copr Topgrade](https://copr.fedorainfracloud.org/coprs/lilay/topgrade) build.

Copr repo: https://copr.fedorainfracloud.org/coprs/lilay/topgrade

## How it Works

A GitHub Actions workflow runs twice daily to:

1.  Check for the latest release of `topgrade-rs/topgrade`.
2.  If a new version is found, it updates the `Version:` tag in the `topgrade.spec` file.
3.  The changes are then automatically committed and pushed to this repository.
4.  Trigger Fedora Copr build via webhook.

## Purpose

This repository is intended to be used as a source for a Copr build, allowing for automated builds of the latest version of Topgrade for RPM-based distributions.
