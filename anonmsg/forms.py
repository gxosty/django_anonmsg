from django import forms


class CreateMessageForm(forms.Form):
	text_message = forms.CharField(widget=forms.Textarea)
	passphrase = forms.CharField(max_length=64)


class ReadMessageForm(forms.Form):
	message_id = forms.CharField(max_length=64)
	passphrase = forms.CharField(max_length=64)
