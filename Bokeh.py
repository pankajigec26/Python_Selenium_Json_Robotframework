import xml.etree.ElementTree as ET
import pandas as pd
import datetime
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge


date=datetime.datetime.now().date()
date=pd.to_datetime(date)


def robot_output_xml_parsing(xml):
    xml_data=open(xml).read()
    root= ET.XML(xml_data)
    generated=root.attrib.get('generated')
    for child in root.iter('statistics'):
            for subchild in child:
                for sub in subchild:
                        fail=sub.get('fail')
                        Pass=sub.get('pass')
                        suite_name=sub.get('name')

    return generated ,fail ,Pass ,suite_name  


def create_csv(xml):
    generated,fail,Pass,suite_name=robot_output_xml_parsing(xml)
    import csv
    import os
    fieldnames = ['suite_name','fail','Pass','Report_datetime']
    if os.path.isfile('./data.csv'):
            with open('data.csv', 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'suite_name': suite_name, 'fail': fail,'Pass':Pass,'Report_datetime':generated})
                
    else:
        with open('data.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'suite_name': suite_name, 'fail': fail,'Pass':Pass,'Report_datetime':generated})
            
    

def data_group_by_date():
    df=pd.read_csv('data.csv')
    g1=df.groupby([ 'Report_datetime']).sum()
    g1=df.groupby('Report_datetime', as_index=False).sum()
    data = g1.to_dict(orient='list')
    dates = g1['Report_datetime'].tolist()
    output_file("dodged_bars.html")
    source = ColumnDataSource(data=data)
    p = figure(x_range=dates, y_range=(0, g1[['fail','Pass']].values.max() + 3), 
           plot_height=250, title="Day wise execution data",toolbar_location=None, tools="")
    p.vbar(x=dodge('Report_datetime', -0.25, range=p.x_range), top='fail', width=0.4, source=source,
       color="#fc8d59", legend=value("fail"))
    p.vbar(x=dodge('Report_datetime',  0.25,  range=p.x_range), top='Pass', width=0.4, source=source,
       color="#718dbf", legend=value("Pass"))
    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"
    show(p)
	
	
def data_for_single_day():
    df=pd.read_csv('data.csv')
    g1=df.sort_values(by='Report_datetime',ascending=False).head(1)
    data = g1.to_dict(orient='list')
    dates = g1['Report_datetime'].tolist()
    output_file("dodged_bars1.html")
    source = ColumnDataSource(data=data)
    p1 = figure(x_range=dates, y_range=(0, g1[['fail','Pass']].values.max() + 3), 
           plot_height=250, title="Latest execution data",toolbar_location=None, tools="")
    p1.vbar(x=dodge('Report_datetime', -0.25, range=p1.x_range), top='fail', width=0.4, source=source,
       color="#d53e4f", legend=value("fail"))
    p1.vbar(x=dodge('Report_datetime',  0.25,  range=p1.x_range), top='Pass', width=0.4, source=source,
       color="#99d594", legend=value("Pass"))
    p1.x_range.range_padding = 0.1
    p1.xgrid.grid_line_color = None
    p1.legend.location = "top_left"
    p1.legend.orientation = "horizontal"
    show(p1) 

create_csv('output.xml')
data_group_by_date()
data_for_single_day()

