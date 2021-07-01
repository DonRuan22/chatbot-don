#!/bin/bash
ls
#rasa run actions
rasa run --cors "*" --enable-api --credentials credentials.yml --debug