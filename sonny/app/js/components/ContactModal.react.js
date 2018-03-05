var React = require('react');
var CMActions = require('../actions/CMActions');

var ContactModal = React.createClass({
	render:function() {
		return(
			<div id="contact_modal" className="modal">
				<form id="contact_form" onSubmit={this._saveContact}>
					<div className="modal-content">
						<h4>Add New Contact</h4>
						<div className="input-field">
							<i className="mdi-action-account-circle prefix"></i>
							<input id="contact_name" type="text" className="validate" />
							<label for="icon_prefix">Name</label>
						</div>
						<div className="input-field">
							<i className="mdi-communication-phone prefix"></i>
							<input id="contact_phone" type="tel" className="validate"/>
							<label for="icon_telephone">Phone</label>
						</div>
						<div className="input-field">
							<i className="mdi-communication-email prefix"></i>
							<input id="contact_email" type="email" className="validate"/>
							<label for="icon_email">Email</label>
						</div>
					</div>
					<input type="submit" className="hidden-btn"/>
				</form>

				<div className="modal-footer">
					<a onClick={this._saveContact} className="modal-action modal-close waves-effect waves-green btn-flat">Press enter or click here</a>
				</div>
			</div>
		);
	},
	// sending new contact to action
	_saveContact: function(e) {
		e.preventDefault();
		var form = $('#contact_form');

		const newContact = ['name', 'phone', 'email'].reduce((contact, key) => {
			contact[key] = form.find(`#contact_${key}`).val();
			return contact;
		}, {});

		const [firstName, lastName] = newContact.name.split(' ');

		fetch('http://localhost:3310/miami/contact', {
			method: 'POST',
			body: JSON.stringify({
				firstName,
				lastName,
				phoneNumbers: [{number: newContact.phone}],
				email: newContact.email
			})
		}).then(() => {
			CMActions.create(newContact);
		});

		this._clearContactForm();
	},
	/*
	 * clearing form for next time
	 */
	_clearContactForm: function() {
		var form = $('#contact_form');

		form.find('#contact_name').val('');
		form.find('#contact_phone').val('');
		form.find('#contact_email').val('');
		$('#contact_modal').closeModal();
	}
});

module.exports = ContactModal;
