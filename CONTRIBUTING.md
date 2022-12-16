# Contributing

To make contributions to this charm, you'll need a working [development setup](https://juju.is/docs/sdk/dev-setup).

You can use the environments created by `tox` for development:

```shell
cd src/
tox --notest -e unit
source .tox/unit/bin/activate
```

## Testing

This project uses `tox` for managing test environments. There are some pre-configured environments
that can be used for linting and formatting code when you're preparing contributions to the charm:

```shell
make reformat           # update your code according to linting rules
make lint               # code style
make unittests          # unit tests
make functional         # integration tests
make test               # runs lint, unit and integration tests
```

## Build the charm

Build the charm in this git repository using:

```shell
make build
```

<!-- You may want to include any contribution/style guidelines in this document>
