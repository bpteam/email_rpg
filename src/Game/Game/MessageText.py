__author__ = 'Evgeny Pyanykh'
__email__ = 'bpteam22@gmail.com'
__credits__ = ["Evgeny Pyanykh", "Roman Evdokimov"]
__license__ = "GPL"


class MessageText(object):
    message_text = ''

    @staticmethod
    def add_text(message_text):
        MessageText.message_text += message_text

    @staticmethod
    def show_text():
        print(MessageText.text)
        MessageText.text = ''