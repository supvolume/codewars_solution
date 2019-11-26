""" solution for Human readable duration format challenge
convert seconds to year, day, hour, minute and second
in readable format"""

def format_duration(seconds):
    if seconds == 0:
        return 'now'
    else:
        duration = {'year':0,'day':0,'hour':0,'minute':0,'second':0}
        
        # second
        duration['second'] = seconds % 60
        if seconds >= 60:
            
            # minute
            minute = seconds // 60
            duration['minute'] = minute % 60
            if minute >= 60:
                
                # hour
                hour =  minute // 60
                duration['hour'] = hour % 24
                if hour >= 24:
                    
                    # day
                    day = hour // 24
                    duration['day'] = day % 365
                    if day >= 365:
                        
                        # year
                        year = day // 365
                        duration['year'] = year

    # format
    duration_list = []
    for k,v in duration.items():
        if v == 1:
            duration_list.append(str(v)+' ' + k)
        elif v != 0:
            duration_list.append(str(v)+' ' + k+'s')

    if len(duration_list) == 1:
        return duration_list[0]
    elif len(duration_list) == 2:
        return ' and '.join(duration_list)
    else:
        return ', '.join(duration_list[:-1]) + ' and ' + duration_list[-1]


