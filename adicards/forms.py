from django.forms import Form, CharField, URLField, ModelMultipleChoiceField, Textarea
from adicards.models import Deck, Flashcard


class DeckCreateForm(Form):
    name = CharField(label='Deck Name', max_length=124)


class FlashcardCreateForm(Form):
    url_prompt = URLField(label='URL Prompt Link (ex. Image, Website, etc.)')
    text_prompt = CharField(label='Text Prompt Link', widget=Textarea)
    answer = CharField(label='Answer', widget=Textarea)
    decks = ModelMultipleChoiceField(queryset=Deck.objects.all())