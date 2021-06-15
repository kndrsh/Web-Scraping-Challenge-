# -*- coding: utf-8 -*-
#Dependicies
from bs4 import BeautifulSoup as bs
import pymongo
import requests
from splinter import Browser
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd



