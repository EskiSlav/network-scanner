from django.test import TestCase, Client
from cabinet.models import Messages, Users
class TestModels(TestCase):
    
    def setUp(self):
        
        self.user = Users.objects.create(
            tg_id=123456,
            username="eskislav",
            first_name="Viacheslav",
            last_name="Kozachok",
            is_bot=False
        )
        msg1 = Messages.objects.create(
            message_id=1,
            text="Text1",
            user=self.user,
            direction="from"
        )
        msg2 = Messages.objects.create(
            message_id=2,
            text="Text2",
            user=self.user,
            direction="from"
        )
        msg3 = Messages.objects.create(
            message_id=3,
            text="Text3",
            user=self.user,
            direction="to"
        )
        self.user.save()
        msg1.save()
        msg2.save()
        msg3.save()


    def test_number_of_messages_sent(self):
        self.assertEquals(self.user.messages_sent_to_user_number, 1)

    def test_number_of_messages_sent(self):
        self.assertEquals(self.user.messages_received_from_user_number, 2)

    def test_total_messages(self):
        self.assertEquals(self.user.total_messages, 3)