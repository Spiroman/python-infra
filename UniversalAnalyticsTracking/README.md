### How to use

------

This simple file is just a wrapper for Google Analytics' (GA) API.
It requires that an environment variable called GA_TRACKING_ID will be set to the Universal Analytics (UA) tacking ID. Said ID can ben be found in GA under Admin->Desired property(UA)->Tracking info->Tracking code.

When calling the `track_event`  function, the only mandatory fields are `category` and `action`. 
They describe the nature of the tracked event. For example, `category` could be set to *Room* and `action` could be set to *Closed*.

The optional metrics parameter needs to be a dictionary containing key value pairs of the following form: `"cm{integer}" : {integer}` where the key is the index of the relevant metric and the value is the metrics int value. See metric reference [here](https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters#cm_)

To find which metrics are available and their index go to Admin -> Desired property(UA) -> Custom Definitions -> Custom Metrics

The other optional parameters are self explanatory, `value` is an integer value for the event itself, `label` is additional metadata attached to the event, and `cid` is the client id (either user id or client id to be a valid call to GA's API, left it as a parameter to be defined just in case) default is *"coview"*. 

Example usage:

```
from UniversalAnalyticsTracking import tracking 

tracking.track_event(
    category='Room', 
    action='Closed', 
    label='Sports',
    value=1,
    metrics={"cm1" : 42, "cm2" : 55, "cm12" : 3})
```

### Useful links

------

Measurement Protocol for UA - https://developers.google.com/analytics/devguides/collection/protocol/v1

Google's Example - https://cloud.google.com/appengine/docs/flexible/python/integrating-with-analytics

Parameters reference - https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters

