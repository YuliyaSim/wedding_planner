import csv
import io
import uuid
from guests.models import Party, Guest
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def import_guests(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        first_row = True
        for row in reader:
            if first_row:
                first_row = False
                continue
            party_name, first_name, last_name, party_type, is_child, category, is_invited, email = row[:8]
            if not party_name:
                print ('skipping row {}'.format(row))
                continue
            party = Party.objects.get_or_create(name=party_name)[0]
            party.type = party_type
            party.category = category
            party.is_invited = _is_true(is_invited)
            if not party.invitation_id:
                party.invitation_id = uuid.uuid4().hex
            party.save()
            if email:
                guest, created = Guest.objects.get_or_create(party=party, email=email)
                guest.first_name = first_name
                guest.last_name = last_name
            else:
                guest = Guest.objects.get_or_create(party=party, first_name=first_name, last_name=last_name)[0]
            guest.is_child = _is_true(is_child)
            guest.save()


def export_guests():
    headers = [
        'party_name', 'first_name', 'last_name', 'party_type',
        'is_child', 'category', 'is_invited', 'is_attending',
        'rehearsal_dinner', 'meal', 'email', 'comments'
    ]
    file = io.StringIO()
    writer = csv.writer(file)
    writer.writerow(headers)
    for party in Party.in_default_order():
        for guest in party.guest_set.all():
            if guest.is_attending:
                writer.writerow([
                    party.name,
                    guest.first_name,
                    guest.last_name,
                    party.type,
                    guest.is_child,
                    party.category,
                    party.is_invited,
                    guest.is_attending,
                    party.rehearsal_dinner,
                    guest.meal,
                    guest.email,
                    party.comments,
                ])
    return file


def _is_true(value):
    value = value or ''
    return value.lower() in ('y', 'yes')



# #@login_required
# def export_guests(request):
#     export = csv_import.export_guests()
#     response = HttpResponse(export.getvalue(), content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename=all-guests.csv'
#     return response


# @login_required
# def dashboard(request):
#     parties_with_pending_invites = Party.objects.filter(
#         is_invited=True, is_attending=None
#     ).order_by('category', 'name')
#     parties_with_unopen_invites = parties_with_pending_invites.filter(invitation_opened=None)
#     parties_with_open_unresponded_invites = parties_with_pending_invites.exclude(invitation_opened=None)
#     attending_guests = Guest.objects.filter(is_attending=True)
#     guests_without_meals = attending_guests.filter(
#         is_child=False
#     ).filter(
#         Q(meal__isnull=True) | Q(meal='')
#     ).order_by(
#         'party__category', 'first_name'
#     )
#     meal_breakdown = attending_guests.exclude(meal=None).values('meal').annotate(count=Count('*'))
#     category_breakdown = attending_guests.values('party__category').annotate(count=Count('*'))
#     return render(request, 'guests/dashboard.html', context={
#         'guests': Guest.objects.filter(is_attending=True).count(),
#         'possible_guests': Guest.objects.filter(party__is_invited=True).exclude(is_attending=False).count(),
#         'not_coming_guests': Guest.objects.filter(is_attending=False).count(),
#         'pending_invites': parties_with_pending_invites.count(),
#         'pending_guests': Guest.objects.filter(party__is_invited=True, is_attending=None).count(),
#         'guests_without_meals': guests_without_meals,
#         'parties_with_unopen_invites': parties_with_unopen_invites,
#         'parties_with_open_unresponded_invites': parties_with_open_unresponded_invites,
#         'unopened_invite_count': parties_with_unopen_invites.count(),
#         'total_invites': Party.objects.filter(is_invited=True).count(),
#         'meal_breakdown': meal_breakdown,
#         'category_breakdown': category_breakdown,
#     })
#
#
# def invitation(request, invite_id):
#     party = guess_party_by_invite_id_or_404(invite_id)
#     if party.invitation_opened is None:
#         # update if this is the first time the invitation was opened
#         party.invitation_opened = datetime.utcnow()
#         party.save()
#     if request.method == 'POST':
#         for response in _parse_invite_params(request.POST):
#             guest = Guest.objects.get(pk=response.guest_pk)
#             assert guest.party == party
#             guest.is_attending = response.is_attending
#             guest.meal = response.meal
#             guest.save()
#         if request.POST.get('comments'):
#             comments = request.POST.get('comments')
#             party.comments = comments if not party.comments else '{}; {}'.format(party.comments, comments)
#         party.is_attending = party.any_guests_attending
#         party.save()
#         return HttpResponseRedirect(reverse('rsvp-confirm', args=[invite_id]))
#     return render(request, template_name='guests/invitation.html', context={
#         'party': party,
#         'meals': MEALS,
#     })
#
#
# InviteResponse = namedtuple('InviteResponse', ['guest_pk', 'is_attending', 'meal'])
#
#
# def _parse_invite_params(params):
#     responses = {}
#     for param, value in params.items():
#         if param.startswith('attending'):
#             pk = int(param.split('-')[-1])
#             response = responses.get(pk, {})
#             response['attending'] = True if value == 'yes' else False
#             responses[pk] = response
#         elif param.startswith('meal'):
#             pk = int(param.split('-')[-1])
#             response = responses.get(pk, {})
#             response['meal'] = value
#             responses[pk] = response
#
#     for pk, response in responses.items():
#         yield InviteResponse(pk, response['attending'], response.get('meal', None))
#
#
# def rsvp_confirm(request, invite_id=None):
#     party = guess_party_by_invite_id_or_404(invite_id)
#     return render(request, template_name='guests/rsvp_confirmation.html', context={
#         'party': party,
#         'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
#     })
#
#
# @login_required
# def invitation_email_preview(request, invite_id):
#     party = guess_party_by_invite_id_or_404(invite_id)
#     context = get_invitation_context(party)
#     return render(request, INVITATION_TEMPLATE, context=context)
#
#
# @login_required
# def invitation_email_test(request, invite_id):
#     party = guess_party_by_invite_id_or_404(invite_id)
#     send_invitation_email(party, recipients=[settings.DEFAULT_WEDDING_TEST_EMAIL])
#     return HttpResponse('sent!')
#
#
# def save_the_date_random(request):
#     template_id = random.choice(SAVE_THE_DATE_CONTEXT_MAP.keys())
#     return save_the_date_preview(request, template_id)
#
#
# def save_the_date_preview(request, template_id):
#     context = get_save_the_date_context(template_id)
#     context['email_mode'] = False
#     return render(request, SAVE_THE_DATE_TEMPLATE, context=context)
#
#
# @login_required
# def test_email(request, template_id):
#     context = get_save_the_date_context(template_id)
#     send_save_the_date_email(context, [settings.DEFAULT_WEDDING_TEST_EMAIL])
#     return HttpResponse('sent!')
#
#
# def _base64_encode(filepath):
#     with open(filepath, "rb") as image_file:
#         return base64.b64encode(image_file.read())