# TMT - MTA Subway Monitor

A professional microservice to monitor real-time MTA (NYC Subway) data for active trains on a specified subway line.

## Features

- Monitors the number of active trains on a specified subway line (default: L train).
- Logs data every 30 seconds.
- Configurable via environment variable `SUBWAY_LINE`.
- Production-ready with Docker and Kubernetes support.

## Prerequisites

- Python 3.11+
- Docker (for containerization)
- Kubernetes (for deployment)

## Installation

1. Clone or download the project files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Local Run

Set the environment variable for the subway line (optional, defaults to 'L'):

```bash
export SUBWAY_LINE=L
python main.py
```

### Docker

Build the image:

```bash
docker build -t tmt-monitor .
```

Run the container:

```bash
docker run -e SUBWAY_LINE=L tmt-monitor
```

### Kubernetes

Apply the deployment:

```bash
kubectl apply -f k8s-deployment.yaml
```

Note: Update the image name in `k8s-deployment.yaml` to your actual Docker image.

## Configuration

- `SUBWAY_LINE`: Environment variable to specify the subway line to monitor (e.g., 'L', 'A', '1').

## Troubleshooting

- **No data logged**: Check internet connection and MTA API availability.
- **Import errors**: Ensure `nyct-gtfs` is installed correctly.
- **Kubernetes issues**: Verify cluster access and image availability.

## Dependencies

- nyct-gtfs: Library for accessing MTA GTFS data.