# Wake-on-LAN Web

Simple web app that allows you to manage and monitor the status of machines on your network. It provides functionalities to add, delete, check the status, and send Wake-on-LAN (WOL) packets to machines.

## Implemented Features

#### Manage hosts 
- **Add Machine**: Add a new machine with its IP address and MAC address.
- **Delete Machine**: Remove a machine from the list.

#### Host Actions
- **Check Status**: Check if a machine is up or down useful for checking when 
- **Spin Up Machine**: Send a WOL packet to spin up a machine.

## Installation

##### Install with docker-compose

1. Clone the repository:
    ```bash
    git clone https://github.com/seancorrgs/wol-webui.git
    cd wol-webui
    ```

2. Create a `docker-compose.yml` file with the following content (an example is provided):

    ```yaml
    services:
        wol-web:
            # build: . ## If you would like to build the image from source
            image: seancorrgs/wol-webui:latest
            network_mode: host
            environment:
                - LISTEN_PORT=8002
            volumes:
                - ./dockerdata/machines.json:/app/src/machines.json
    ```

3. Run the Docker Compose:
    ```bash
    docker compose up -d
    ```

4. Open your web browser and navigate to `http://localhost:80`.

## Conf Files

- `machines.json`: A JSON file to store machine details and their statuses. (Created after first run)

## Usage

### Adding a Machine

1. Fill in the "Machine Name", "IP Address", and "MAC Address" fields.
2. Click the "Add Host" button.

### Deleting a Machine

1. Click the "Delete" button next to the machine you want to remove.

### Checking Machine Status

1. Click the "Check" button next to the machine to check its status.

### Spinning Up a Machine

1. Click the "Spin up" button next to the machine to send a WOL packet.

### Running backups



## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [ping3](https://github.com/kyan001/ping3)
- [Tailwind CSS](https://tailwindcss.com/)
