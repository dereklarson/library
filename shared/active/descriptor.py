from loaddata import example
from bento.bento import Bento


def generate(repobase):
    series_page = {
        "banks": {
            "axis_controls": {
                "args": {"use": "xy"},
                "position": [0, 0],
                "type": "axis_controls",
            },
            "graph": {"args": {}, "position": [2, 0], "type": "graph"},
            "filterset": {
                "args": {"columns": ["region"]},
                "position": [1, 0],
                "type": "filters",
            },
            "fit_controls": {"args": {}, "position": [0, 5], "type": "fit_controls"},
        },
        "layout": {"width": 12, "height": 8},
        "connections": {
            "axis_controls": {"graph": ["figure"]},
            "filterset": {"graph": ["figure"]},
            "fit_controls": {"graph": ["figure"]},
        },
    }

    descriptor = {
        "name": "mars",
        "title": "Mars Dashboard",
        "pages": {"series": series_page},
        "data": {"location": repobase, "calls": {"dataname": example.load},},
    }

    bento = Bento(descriptor)
    return bento
