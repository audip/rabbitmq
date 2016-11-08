## RabbitMQ self-learning through examples

### Installation

- Download and install rabbitmq `brew install rabbitmq`

### Running the system

- `rabbitmq-server` to run it from /usr/local/sbin, if not in PATH then, `export PATH=$PATH:/usr/local/sbin`

### Lessons

1. Basic example: run rabbitmq-server, then create send.py and receive.py to use RabbitMQ as a basic queue.
2. Work queue: run server, then set up worker.py to listen to messages and publish tasks through new_task.py
