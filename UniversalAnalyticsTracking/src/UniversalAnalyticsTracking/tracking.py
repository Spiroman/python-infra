import os
import requests



def track_event(category, action, label=None, value=0, cid='coview', metrics=None):
    '''
    Posts an event to the GA API, requeries the GA_TRACKING_ID environment variable to be set to the Universal Analytics property tracking id
    Each metric in the UA property is indexed, so when unsure about what metric corresponds to which index, 
    look it up in GA under custom defenitons
    
    Parameters:
        category    (str):The event category, for example category=Room
        action      (str):The event action, for example action=Closed
        label       (str):Event metadata
        value       (int):A numerical value of the event
        cid         (str):Client ID
        metrics     (dict):If provided need to be a dictionary containing key value pairs like so "cm{integer}" : {integer}.
    '''
    GA_TRACKING_ID = os.environ['GA_TRACKING_ID']
    data = {
        'v': '1',  # API Version.
        'tid': GA_TRACKING_ID,  # Tracking ID / Property ID.
        # Anonymous Client Identifier. Ideally, this should be a UUID that
        # is associated with particular user, device, or browser instance.
        'cid': cid, # Client ID. Currently doesnt not matter to our case, but is a mandatory field for valid calls
        't': 'event',  # Event hit type.
        'ec': category,  # Event category.
        'ea': action,  # Event action.
        'el': label,  # Event label.
        'ev': value,  # Event value, must be an integer
        'ua': ''
    }

    # Add all metrics to post data if present
    if(metrics):
        for metric in metrics:
            data[metric] = metrics[metric]

    requests.post('https://www.google-analytics.com/collect', data=data)