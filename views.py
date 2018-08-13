#import json
from django.shortcuts import render

# Create your views here.
def home(request):
    column_chart_data = {
        'chart': {
          'type': 'column'
      },
      'title': {
          'text': 'Historic World Population by Region'
      },
      'xAxis': {
          'categories': ['Africa', 'America', 'Asia', 'Europe', 'Oceania']
      },
      'series': [{
          'name': 'Year 1800',
          'data': [107, 31, 635, 203, 2]
      }, {
          'name': 'Year 1900',
          'data': [133, 156, 947, 408, 6]
      }, {
          'name': 'Year 2012',
          'data': [1052, 954, 4250, 740, 38]
      }]
    }

    splain_chart_data = {
        'chart': {
            'type': 'areaspline'
        },
        'title': {
            'text': 'Average fruit consumption during one week'
        },
        'legend': {
            'layout': 'vertical',
            'align': 'left',
            'verticalAlign': 'top',
            'x': 150,
            'y': 100,
            'floating': 'true',
            'borderWidth': 1,
            'backgroundColor': '#FFFFFF'
        },
        'xAxis': {
            'categories': [
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday',
                'Sunday'
            ],
            'plotBands': [{
                'from': 4.5,
                'to': 6.5,
                'color': 'rgba(68, 170, 213, .2)'
            }]
        },
        'yAxis': {
            'title': {
                'text': 'Fruit units'
            }
        },
        'tooltip': {
            'shared': 'true',
            'valueSuffix': ' units'
        },
        'credits': {
            'enabled': 'false'
        },
        'plotOptions': {
            'areaspline': {
                'fillOpacity': 0.5
            }
        },
        'series': [{
            'name': 'John',
            'data': [3, 4, 3, 5, 4, 10, 12]
        }, {
            'name': 'Jane',
            'data': [1, 3, 4, 3, 3, 5, 4]
        }]
    }

    # dump = json.dumps(chart_data)
    
    charts = {
        'column': column_chart_data,
        'splain': splain_chart_data
    }

    return render(request, "index.html", charts)