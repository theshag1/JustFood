from modeltranslation.translator import translator, TranslationOptions
from .models import Food


class FoodTranslation(TranslationOptions):
    fields = ('name', 'composition')


translator.register(Food, FoodTranslation)
