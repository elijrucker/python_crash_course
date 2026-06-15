#!/bin/bash
docker run -it --rm \
  -v ~/.gitconfig:/root/.gitconfig:ro \
  -v ~/workspace/python_crash_course:/workspace \
  python-crash-course "$@"
