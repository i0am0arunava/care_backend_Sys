# Care Backend

<p align="center">
  <a href="https://ohc.network">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./care/static/images/logos/light-logo.svg">
      <img alt="care logo" src="./care/static/images/logos/black-logo.svg"  width="300">
    </picture>
  </a>
</p>

Note: Frontend Available Here :  https://github.com/i0am0arunava/care_fe

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



### Staging Deployments



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
## Here are some screenshot attached

![Screenshot from 2025-07-05 01-49-39](https://github.com/user-attachments/assets/d90fe0b4-ed74-4172-94e0-a41dc5dcdf58)




![Screenshot from 2025-07-05 01-45-18](https://github.com/user-attachments/assets/da8177c9-3094-4e8e-ba6f-074795b70de0)

![Screenshot from 2025-07-05 01-44-42](https://github.com/user-attachments/assets/f1ac5f7f-e90d-4e11-8008-3dd0ca0b76ce)



![Screenshot from 2025-07-05 01-39-01](https://github.com/user-attachments/assets/8bb4a77c-26b2-4df5-b543-8c927c54d705)



![Screenshot from 2025-07-05 01-39-42](https://github.com/user-attachments/assets/cfd2c934-1792-48db-a891-ce02a027da03)









## Contributing

We welcome contributions from everyone. Please read our [contributing guidelines](./CONTRIBUTING.md) to get started.
