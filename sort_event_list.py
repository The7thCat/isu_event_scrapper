from datetime import datetime

def sort_event_list(list_of_events):
    events_from_list = []
    for _ in list_of_events:
        # Filter junior events out
        if 'JUNIOR' in _['event_name'] or 'JGP' in _['event_name']:
            continue
        else:
            events_from_list.append(_)
            date_str = str(_['event_date'])
            start_date_str, end_date_str = date_str.split(' - ')
            year = end_date_str.split(', ')[-1]
            start_date = datetime.strptime(f"{start_date_str} {year}", '%d %b %Y')
            _['start_date'] = start_date
    sorted_list = sorted(events_from_list, key=lambda x: x['start_date'])
    sorted_list_of_events = []
    for x in sorted_list:
        x.pop('start_date', None)
        sorted_list_of_events.append(x)
    return sorted_list_of_events
