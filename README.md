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

##### Install with docker 

1. Clone the repository:
    ```bash
    git clone http://giturl
    cd wol-loadbal
    ```

2. Build the Docker image:
    ```bash
    docker build -t wol-web .
    ```

3. Run the Docker container:
    ```bash
    docker run -d -p 80:80 wol-web
    ```

4. Open your web browser and navigate to `http://localhost:80`


##### Install with docker-compose

1. Clone the repository:
    ```bash
    git clone http://giturl
    cd wol-loadbal
    ```

2. Create a `docker-compose.yml` file with the following content:
    ```yaml
    services:
      wol-web:
        build: .
        image: wol-web
        ports:
          - "80:80"
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

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [ping3](https://github.com/kyan001/ping3)
- [Tailwind CSS](https://tailwindcss.com/)
