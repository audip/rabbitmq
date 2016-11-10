## RabbitMQ self-learning through examples

### Installation

- Download and install rabbitmq `brew install rabbitmq`

### Running the system

- `rabbitmq-server` to run it from /usr/local/sbin, if not in PATH then, `export PATH=$PATH:/usr/local/sbin`

### Lessons

1. Basic example: run rabbitmq-server, then create send.py and receive.py to use RabbitMQ as a basic queue.
2. Work queue: run server, then set up worker.py to listen to messages and publish tasks through new_task.py.
3. Publish/subscribe: run server, then emit_log.py to publish messages and receive_logs.py to print them out.
4. Routing: run server, then emit_logs_direct.py to publish error logs and one consumer prints it to screen, another consumer save error messages to disk.
  
## License

    Copyright 2016 Aditya Purandare

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
