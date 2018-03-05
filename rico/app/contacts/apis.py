import ujson
from logging import getLogger

from flask import Blueprint, jsonify, request

from rico.app.contacts.models import Contacts


log = getLogger(__name__)

contact_apis = Blueprint('contact_apis', __name__, url_prefix='/miami/')


@contact_apis.route('contacts', methods=['GET'])
def get_contacts():
    """
    API to load all contacts
    :return json list of contacts to the browser
    """

    response = Contacts().get_all()

    log.debug("Get contacts response: {}".format(response))

    return jsonify(response)


@contact_apis.route('contact', methods=['POST'])
def create_contact():
    """
    API to create a new contacts
    """

    response = Contacts().create(request.get_json(force=True))

    log.debug("Create contact response: {}".format(response))

    return jsonify(response)


@contact_apis.route('contact/<contact_id>', methods=['PUT'])
def update_contact(contact_id):
    """
    API to update a contact
    """

    response = Contacts().update(contact_id, request.get_json(force=True))

    log.debug("Update contact response: {}".format(response))

    return jsonify(response)


@contact_apis.route('contact/<contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    """
    API to delete a contact
    """

    response = Contacts().delete(contact_id)

    log.debug("Update contact response: {}".format(response))

    return jsonify(response)
