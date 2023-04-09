#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- encoding:UTF-8 -*-
# coding=utf-8
# coding:utf-8

import codecs
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication,
                             QLabel, QHBoxLayout, QVBoxLayout, QLineEdit,
                             QSystemTrayIcon, QMenu, QComboBox, QDialog, QMenuBar, QFileDialog,
                             QTextEdit, QListWidget, QPlainTextEdit)
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QAction, QIcon, QColor
import PyQt6.QtGui
import webbrowser
import os
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import sys
import subprocess
import shutil
import html2text
import jieba
import glob
import datetime
import csv
from transformers import GPT2Tokenizer
import openai
import time
import markdown2
import signal
import pyperclip
import urllib3
import logging
import httpx
import asyncio
import re