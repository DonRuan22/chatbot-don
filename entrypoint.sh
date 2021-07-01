#!/bin/bash
ls
#rasa run actions
rasa run run --credentials credentials.yml --enable-api --cors “*” --debug