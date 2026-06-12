# Python Crash Course

Coursework and exercises from *Python Crash Course* by Eric Matthes, serving as a Python syntax primer and containerized development practice environment.

## Prerequisites

- Docker installed and running
- SSH access to the host server

## Setup

Build the image:
```bash
docker build -t python-crash-course .
```

Run the container:
```bash
./run.sh
```

## Structure

Directory architecture mirrors the book itself. `part1/` contains exercises from Chapters 1–11. `part2/` contains the three projects from the second half of the book.
