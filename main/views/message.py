# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify
from flask import request
from hl7tojson import parser

blueprint = Blueprint('article', __name__)


@blueprint.route('/messages', methods=['POST'])
def get_message():
    data = request.get_json()
    message = data['message']
    message = message.replace('\n', '\r').encode('utf-8')
    try:
        parsed_data = parser.parse(message)
    except Exception as e:
        return jsonify({
            'error': e.message
        }), 400
    return jsonify(parsed_data)
