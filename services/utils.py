from . connectors import DeviceServiceConnector


def update_device_status(unique_id, state):
    connector = DeviceServiceConnector()
    connector.state_update(unique_id, state)
