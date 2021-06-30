#!/bin/bash
ls
#rasa run actions
rasa run -p ${PORT} --cors "*" --enable-api --credentials credentials.yml --debug