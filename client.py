# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 22:25:20 2018

@author: Leila
"""

#In this exercise we will create an HTTP server to which we can upload a
#graph and in which we can get the degrees of separation between two nodes
#in the graph.

#1. Create a route in the server to which the user can upload a graph using
#JSON and using the POST http method. 

#The JSON data should be passed as part of the request body, not in the URL.

#2. Create a route to get the degrees of separation between two nodes in
#the previously uploaded graph.

#localhost:5000/degrees_of_separation/<origin>/<destination>.

#You can use any code we want from the exercises we’ve done in class
#related to graphs.

#%%

import requests


graph1 = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": [],
    "f": []
}

def upload_graph(graph):  
    url = "http://127.0.0.1:5000/upload-graph"    
    data = graph
    response = requests.post(url.format(""), json=data)     
    return response.json()

upload_graph(graph1)

def get_degrees_of_separation(start, end, graph): 
    url = "http://127.0.0.1:5000/degrees-of-separation/" + start + "/" + end 
    data = graph
    response = requests.post(url, json=data)
    return response.json()

get_degrees_of_separation("a","e",graph1)

