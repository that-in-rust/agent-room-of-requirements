# ELI5: What Does Iggy Do? (And How to Taste It in 5 Minutes)

**Date**: 2026-02-16

---

## Analogy: Iggy Is a Post Office

Without Iggy (chaos):

```
App A ──────┐
App B ──────┼──▶ Database     (everyone writes directly,
App C ──────┤                  things break, things are lost,
Sensor ─────┘                  no replay, no order guarantee)
```

With Iggy (order):

```
App A ───┐                    ┌──▶ Database
App B ───┼──▶ ┌───────┐ ──┬──┼──▶ Analytics
App C ───┤   │ IGGY  │   │  ├──▶ ML Pipeline
Sensor ──┘   │ ■■■■■ │   │  └──▶ Alerts
             │ ■■■■■ │   │
             │(stored│   │  Messages are STORED.
             │  in   │   │  You can REPLAY them.
             │ order)│   │  Multiple consumers can
             └───────┘   │  read the SAME messages
                         │  independently.
                         │
                Like Kafka, but:
                • Written in Rust (fast, tiny)
                • Single binary (~15MB)
                • No JVM, no ZooKeeper
                • Runs on a Raspberry Pi
```

---

## The 3 Concepts You Need

```
┌─────────────────────────────────────────────────┐
│                   IGGY SERVER                    │
│                                                 │
│  Stream: "sensor-data"     ◄── like a database  │
│  ├── Topic: "temperature"  ◄── like a table     │
│  │   ├── Partition 0       ◄── ordered log      │
│  │   │   ├── msg offset=0: {"temp": 22.5}      │
│  │   │   ├── msg offset=1: {"temp": 23.1}      │
│  │   │   └── msg offset=2: {"temp": 21.8}      │
│  │   └── Partition 1 (optional, for parallelism)│
│  └── Topic: "humidity"                          │
│      └── ...                                    │
│                                                 │
│  Stream: "orders"                               │
│  └── Topic: "new-orders"                        │
│      └── ...                                    │
└─────────────────────────────────────────────────┘
```

- **Stream** = namespace (group related topics)
- **Topic** = ordered append-only log of messages
- **Message** = bytes (JSON, binary, protobuf, whatever)

---

## 5-Minute Taste Test

You need: Docker + Python (or just 2 terminals)

### Terminal 1 — Start Iggy server

```bash
docker run -d --name iggy -p 8090:8090 iggyrs/iggy:latest
```

That's it. Server running. No config files, no ZooKeeper, no 47-step setup. One container.

### Terminal 2 — Produce messages (Python)

```bash
pip install apache-iggy loguru
python examples/python/getting-started/producer.py
```

What happens:

```
┌──────────────┐         ┌─────────────┐
│  producer.py  │────────▶│ Iggy :8090  │
│               │  TCP    │             │
│  1. connect   │         │ Stream:     │
│  2. login     │         │ sample-stream│
│  3. create    │         │ Topic:      │
│     stream    │         │ sample-topic│
│  4. create    │         │             │
│     topic     │         │ [50 msgs    │
│  5. send 5    │         │  stored]    │
│     batches   │         │             │
│     x 10 msgs │         │             │
└──────────────┘         └─────────────┘
```

Output:
```
INFO | Creating stream with name sample-stream...
INFO | Creating topic sample-topic in stream sample-stream
INFO | Successfully sent batch of 10 messages. Batch ID: 1
INFO | Successfully sent batch of 10 messages. Batch ID: 2
...
INFO | Sent 5 batches of messages, exiting.
```

### Terminal 3 — Consume messages (Python)

```bash
python examples/python/getting-started/consumer.py
```

What happens:

```
┌─────────────┐         ┌──────────────┐
│ Iggy :8090  │────────▶│ consumer.py   │
│             │  TCP    │               │
│ [50 msgs]   │  poll   │ 1. connect    │
│             │         │ 2. login      │
│ offset 0────┼────────▶│ 3. poll msgs  │
│ offset 1────┼────────▶│ 4. print      │
│ ...         │         │ 5. repeat     │
│ offset 49───┼────────▶│               │
└─────────────┘         └──────────────┘
```

Output:
```
INFO | Handling message at offset: 0 with payload: message-1...
INFO | Handling message at offset: 1 with payload: message-2...
...
INFO | Consumed 5 batches of messages, exiting.
```

### Key Insight: You can run consumer.py AGAIN

The messages are still there. Iggy stores them. Unlike a queue (RabbitMQ) where messages vanish after consumption, Iggy keeps them like a log.

Run consumer.py 10 times → get the same 50 messages 10 times. That's the whole point.

---

## Where MongoDB Fits In

Today (manual, fragile):

```
┌──────────┐     ┌──────┐     ┌─────────┐
│ producer │────▶│ Iggy │     │ MongoDB │
└──────────┘     └──┬───┘     └─────────┘
                    │
                    │  You write custom code
                    │  to read from Iggy and
                    ▼  insert into MongoDB.
                ┌──────────┐
                │ YOUR     │──▶ MongoDB
                │ GLUE CODE│
                │ (fragile)│
                └──────────┘
```

With MongoDB Connector (what we're building):

```
┌──────────┐     ┌──────┐  connector  ┌─────────┐
│ producer │────▶│ Iggy │────────────▶│ MongoDB │
└──────────┘     └──────┘  (automatic) └─────────┘
```

Just a TOML config file. No glue code. The connector runtime handles:
- Batching
- Retries
- Offset tracking
- Error handling
- Crash recovery

---

## So What Should You Build First?

```
┌─────────┐  ┌─────────────┐  ┌──────┐  ┌─────────┐
│ Step 1  │─▶│ Step 2      │─▶│Step 3│─▶│ Step 4  │
│ vanilla │  │ real payload │  │ glue │  │ "aha,   │
│ hello   │  │ JSON sensors │  │ code │  │  THIS is│
│ world   │  │              │  │ py→  │  │  what a │
│         │  │              │  │ mongo│  │connector│
└─────────┘  └─────────────┘  └──────┘  │  does!" │
                                         └─────────┘
```

1. **Step 1**: Run the 5-minute taste test above (docker + producer.py + consumer.py)
2. **Step 2**: Modify producer.py to send JSON sensor data: `{"sensor_id": "s1", "temp": 22.5, "ts": "..."}`
3. **Step 3**: Write a tiny Python script that consumes from Iggy and inserts into MongoDB (this is the "glue code" the connector replaces)
4. **Step 4**: Now you understand EXACTLY what the MongoDBSink connector automates

---

## Data Flow Summary

```
┌──────────┐     ┌──────┐  MongoDBSink  ┌─────────┐
│ producer │────▶│ Iggy │──────────────▶│ MongoDB │
└──────────┘     └──────┘  .consume()   └────┬────┘
                 │      │                    │
                 │      │  MongoDBSource     │ Change
                 │      │◀──────────────────┤ Stream
                 │      │  .poll()           │
                 └──┬───┘               └─────────┘
                    │
                    ▼
             ┌─────────────┐
             │  Downstream  │
             │  Consumer    │
             │  (analytics, │
             │   alerts,    │
             │   ML, etc.)  │
             └─────────────┘
```
