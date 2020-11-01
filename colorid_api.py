 


def colorid_function_return_colordic():
    """returns the colors dictionary"""

    hex_colors = []
    color_id_api_event = {
            "1": {
            "name": "לבנדר",
            "background": "#a4bdfc",
            "foreground": "#1d1d1d"
            },
            "2": {
            "name": "מרווה",
            "background": "#7ae7bf",
            "foreground": "#1d1d1d"
            },
            "3": {
            "name": "ענבים",
            "background": "#dbadff",
            "foreground": "#1d1d1d"
            },
            "4": {
            "name": "פלמינגו",
            "background": "#ff887c",
            "foreground": "#1d1d1d"
            },
            "5": {
            "name": "בננה",
            "background": "#fbd75b",
            "foreground": "#1d1d1d"
            },
            "6": {
            "name": "מנדרינה",
            "background": "#ffb878",
            "foreground": "#1d1d1d"
            },
            "7": {
            "name": "טווס",
            "background": "#46d6db",
            "foreground": "#1d1d1d"
            },
            "8": {
            "name": "גרפיט",
            "background": "#e1e1e1",
            "foreground": "#1d1d1d"
            },
            "9": {
            "name": "אוכמניות",
            "background": "#5484ed",
            "foreground": "#1d1d1d"
            },
            "10": {
            "name": "ריחן",
            "background": "#51b749",
            "foreground": "#1d1d1d"
            },
            "11": {
            "name": "עגבניה",
            "background": "#dc2127",
            "foreground": "#1d1d1d"
            }
        }
    """for i in color_id_api_event:
        hex_colors.append(color_id_api_event[i])
"""
    return (color_id_api_event)

colorid_function_return_colordic()

def function_return_colorid(hex_color):
    """returns the background hex colors"""
    
    color_id_api_event = {
            "1": {
            "background": "#a4bdfc",
            "foreground": "#1d1d1d"
            },
            "2": {
            "background": "#7ae7bf",
            "foreground": "#1d1d1d"
            },
            "3": {
            "background": "#dbadff",
            "foreground": "#1d1d1d"
            },
            "4": {
            "background": "#ff887c",
            "foreground": "#1d1d1d"
            },
            "5": {
            "background": "#fbd75b",
            "foreground": "#1d1d1d"
            },
            "6": {
            "background": "#ffb878",
            "foreground": "#1d1d1d"
            },
            "7": {
            "background": "#46d6db",
            "foreground": "#1d1d1d"
            },
            "8": {
            "background": "#e1e1e1",
            "foreground": "#1d1d1d"
            },
            "9": {
            "background": "#5484ed",
            "foreground": "#1d1d1d"
            },
            "10": {
            "background": "#51b749",
            "foreground": "#1d1d1d"
            },
            "11": {
            "background": "#dc2127",
            "foreground": "#1d1d1d"
            }
        }
    for i in color_id_api_event:
        if color_id_api_event[i]['background'] == hex_color:
            return (i)