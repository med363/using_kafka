docker exec -it kafka kafka-topics --describe --topic orders --bootstrap-server localhost:9092
Topic: orders   TopicId: pO_L822FTZuIz3jmM9dMLQ PartitionCount: 1       ReplicationFactor: 1    Configs: 
        Topic: orders   Partition: 0    Leader: 1       Replicas: 1     Isr: 1  Elr:    LastKnownElr: 
(venv) works@works-VMware-Virtual-Platform:~/Desktop/orders_app$ docker exec -it kafka kafka-topics --describe --topic orders --bootstrap-server localhost:9092
Topic: orders   TopicId: pO_L822FTZuIz3jmM9dMLQ PartitionCount: 1       ReplicationFactor: 1    Configs: 
        Topic: orders   Partition: 0    Leader: 1       Replicas: 1     Isr: 1  Elr:    LastKnownElr: 
(venv) works@works-VMware-Virtual-Platform:~/Desktop/orders_app$ docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092
orders