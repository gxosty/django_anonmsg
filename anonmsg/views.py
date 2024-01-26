import re

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404

from .models import AnonMessage
from .forms import CreateMessageForm, ReadMessageForm


UUID4_PATTERN = re.compile("([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})")


def _format_message_id(message_id):
	found = UUID4_PATTERN.search(message_id)

	if not found:
		return None

	return found[1]


def index(request):
	return render(request, 'anonmsg/index.html')


def create_message_redirect_index(request):
	return redirect("index")


def create_message(request):
	if request.method == "POST":
		form = CreateMessageForm(request.POST)

		if not form.is_valid():
			messages.error(request, "Invalid Form")
			return create_message_redirect_index(request)

		am = AnonMessage.objects.create(text_message = request.POST["text_message"], passphrase = request.POST["passphrase"])
		am.save()
		print("AnonMessage created!")

		request.session["message_uuid"] = str(am.id)

		return redirect("message_info")

	return create_message_redirect_index(request)


def read_message(request):
	if request.method == "POST":
		form = ReadMessageForm(request.POST)

		if not form.is_valid():
			messages.error(request, "Invalid URL/ID or Passphrase")
			return redirect("index")

		message_id = _format_message_id(request.POST["message_id"])

		if message_id is None:
			messages.error(request, "An Internal error occurred")
			return redirect("index")

		am = None

		try:
			am = AnonMessage.objects.get(id=message_id, passphrase=request.POST["passphrase"])
		except AnonMessage.DoesNotExist:
			messages.error(request, "Doesn't exist")
			return redirect("index")

		request.session["message_uuid"] = message_id
		return redirect("show_message")

	return redirect("index")


def message_info(request):
	message_uuid = request.session.get("message_uuid", None)
	request.session["message_uuid"] = None

	if not message_uuid:
		raise Http404('Message not found')

	return render(request, 'anonmsg/message_info.html', {"message_uuid" : message_uuid})


def show_message(request):
	message_uuid = request.session.get("message_uuid", None)
	request.session["message_uuid"] = None

	if not message_uuid:
		raise Http404('Message not found')

	am = AnonMessage.objects.get(id = message_uuid)
	message_text = str(am.text_message)
	am.delete()

	return render(request, 'anonmsg/message_show.html', {"message_text" : am.text_message})