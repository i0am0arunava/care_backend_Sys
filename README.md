# Care Backend

<p align="center">
  <a href="https://ohc.network">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./care/static/images/logos/light-logo.svg">
      <img alt="care logo" src="./care/static/images/logos/black-logo.svg"  width="300">
    </picture>
  </a>
</p>



This is the backend for care. an open source platform for managing patients, health workers, and hospitals.

## Features

Care backend makes the following features possible:

- Realtime Analytics of Beds, ICUs, Ventilators, Oxygen and other resources in hospitals
- Facility Management with Inventory Monitoring
- Integrated Tele-medicine & Triage
- Patient Management and Consultation History
- Realtime video feed and vitals monitoring of patients
- Clinical Data Visualizations.

## Getting Started

### Docs and Guides

You can find the docs at https://care-be-docs.ohc.network

### Staging Deployments

Dev and staging instances for testing are automatically deployed on every commit to the `develop` and `staging` branches.
The staging instances are available at:

- https://careapi.ohc.network
- https://careapi-staging.ohc.network

### Self hosting

#### Compose

docker compose is the easiest way to get started with care.
put the required environment variables in a `.env` file and run:

```bash
make up
```

to load seed data for testing run:

```bash
make load-fixtures
```

Stops and removes the containers without affecting the volumes:

```bash
make down
```

Stops and removes the containers and their volumes:

```bash
make teardown
```

#### Docker

Prebuilt docker images for server deployments are available
on [ghcr](https://github.com/ohcnetwork/care/pkgs/container/care)

For backup and restore use [this](/docs/databases/backup.rst) documentation.

## Contributing

We welcome contributions from everyone. Please read our [contributing guidelines](./CONTRIBUTING.md) to get started.
