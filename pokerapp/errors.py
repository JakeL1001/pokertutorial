from flask import render_template
from pokerapp import pokerpack, db
import logging

@pokerpack.errorhandler(404)
def not_found_error(error): #Directs 404 errors to purpose built page
    pokerpack.logger.setLevel(logging.INFO)
    pokerpack.logger.info("Error, page not found")
    return render_template('404.html'), 404

@pokerpack.errorhandler(500)
def internal_error(error): #Directs 500 errors to purpose built page
    pokerpack.logger.setLevel(logging.INFO)
    pokerpack.logger.info("Error, 500, critical error")
    db.session.rollback()
    return render_template('500.html'), 500