#!/bin/bash
pip install rasa
rasa run -p ${PORT} --cors "*"