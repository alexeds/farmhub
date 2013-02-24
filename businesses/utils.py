import simplejson
import urllib


def geocode_api(**kwargs):
    GEOCODE_BASE_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
    kwargs['sensor'] = kwargs.get('sensor', 'false')
    url = '%s?%s' % (GEOCODE_BASE_URL, urllib.urlencode(kwargs))
    return simplejson.load(urllib.urlopen(url))

def get_coordinates(address):
    result = geocode_api(address=address)

    if result['status'] == 'OK':
        return result['results'][0]['geometry']['business'].values()
    
    return (None, None)