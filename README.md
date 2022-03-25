# taxservice

Exploring python-based event streaming with [faust-streaming](https://github.com/faust-streaming/faust).

### Install

pip install -r requirements.txt

### Run

faust -A app.main worker -l info

### What it does

The apache kafka streams getting started setup creates a kafka cluster with
various topics for a wordcount application, including streams-plaintext-input
and streams-wordcount-output. This app just repurposes that
streams-plaintext-input topic to read from. The eventual idea is that "sales"
will be recorded to the topic, and this app will calculate a sales tax for each
sale and produce that to a different tax topic.
