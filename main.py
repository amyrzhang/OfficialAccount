# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
from menu import Menu

urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    #content = Menu()
    #content.create()
    app = web.application(urls, globals())
    app.run()
