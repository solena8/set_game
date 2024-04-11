# Start server command

uvicorn api:app --reload --app-dir back


# Valid
http://127.0.0.1:8000/cards/1ORH,2OVP,3OMV,1ORP

# Not valid
http://127.0.0.1:8000/cards/1ORH,2OVP,3OMH,1ORP

