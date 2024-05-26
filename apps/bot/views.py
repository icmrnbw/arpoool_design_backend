from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from telegram.constants import ChatType

from apps.bot.utils import parse_update, get_user, send_hello


@method_decorator(csrf_exempt, name='dispatch')
class TelegramView(View):
    def post(self, request, *args, **kwargs):
        token = kwargs.get('token')
        update = parse_update(request_token=token, request=request)
        user, created = get_user(update)

        if created:
            send_hello(user)

        if user is None:  # Discard the update, we have nothing to do without user
            return HttpResponse('gg', status=200)

        # Updates that came from private messages
        if update.effective_chat.type == ChatType.PRIVATE:

            # Our bot was blocked/unblocked
            if update.my_chat_member:
                user.has_blocked_the_bot = update.my_chat_member.new_chat_member.status == ChatMember.KICKED
                user.save()

        return HttpResponse('gg', status=200)
