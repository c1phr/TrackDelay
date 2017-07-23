from track_delay import TrackDelay

def start_handler(event, context):
    print("Starting with event: " + str(event))
    td = TrackDelay()
    td.run()