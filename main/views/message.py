# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify
from hl7tojson import parser
from flask import request

blueprint = Blueprint('article', __name__)


@blueprint.route('/messages', methods=['POST'])
def get_message():
    message = request.get_json()
    return jsonify(parser.parse(message))
