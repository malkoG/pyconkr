from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Sponsor, SponsorLevel,
)


class SponsorTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)


translator.register(Sponsor, SponsorTranslationOptions)


class SponsorLevelTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)


translator.register(SponsorLevel, SponsorLevelTranslationOptions)
