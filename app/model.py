from pickleshare import PickleShareDB
from flask import Flask, url_for, render_template, flash, redirect, request, session
app = Flask(__name__)

def login_BD(username, password):
    db = PickleShareDB('miBD')

    if username in db.keys() and db[username] and password == db[username]["pass"]:
        session['logged'] = True
        session['username'] = username
        return "Credenciales correctas"
    else:
        return "Credenciales incorrectas"

def registrar_BD(username, password):
    db = PickleShareDB('miBD')
    if username in db.keys():
        return "Incorrecto"
    else:
        session['logged'] = True
        session['username'] = username
        db[username] = {'pass': password}
        return "Correcto"
        

def editar_BD(username, password):
    db = PickleShareDB('miBD')
    if username in db.keys():
        del db[username]
    registrar_BD(username, password)

def misDatosBD(username):
    db = PickleShareDB('miBD')
    return db[username]