function anonmsg_password_message(text, is_success = false) {
	let pmsg = $('#anonmsg_pmsg')

	if (!text) {
		pmsg.removeClass('d-block')
		pmsg.addClass('d-none')
		return
	}

	pmsg.html(text)

	if (is_success) {
		pmsg.removeClass('alert-danger')
		pmsg.addClass('alert-success')
	} else {
		pmsg.removeClass('alert-success')
		pmsg.addClass('alert-danger')
	}

	pmsg.removeClass('d-none')
	pmsg.addClass('d-block')
}

function anonmsg_create_message_submit() {
	let pp1 = $('#anonmsg_passphrase1')
	let pp2 = $('#anonmsg_passphrase2')

	if (!pp1.val() || !pp2.val()) {
		return false
	}

	if (pp1.val().length < 8) {
		anonmsg_password_message("Password cannot have less than 8 characters", false)
		return false
	}

	if (pp1.val() != pp2.val()) {
		anonmsg_password_message("Passwords don't match", false)
		return false
	}

	anonmsg_password_message('', true)
	return true
}