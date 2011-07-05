from base import Setting, SettingSet
from forms import StringListWidget

from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import Textarea

MODERATION_SET = SettingSet('moderation', _('Moderation settings'), _("Define the moderation workflow of your site"), 100)

USE_CANNED_COMMENTS = Setting('USE_CANNED_COMMENTS', True, MODERATION_SET, dict(
label = _("Use canned comments"),
help_text = _("If you check, the canned comments feature will be activated, allowing moderators to use canned patterns for their comments."),
required=False))

CANNED_COMMENTS = Setting('CANNED_COMMENTS',
[
"We require all postings to have a clear, specific QUESTION in the title field. Please edit this right away to rephrase the title as a proper question.",
],
MODERATION_SET, dict(
label = _("Canned comments"),
help_text = _("Create some canned comments to be used for easier moderation."),
widget=StringListWidget))

FLAG_TYPES = Setting('FLAG_TYPES',
["Spam", "Advertising", "Offensive, Abusive, or Inappropriate", "Content violates terms of use", "Copyright Violation",
 "Misleading", "Someone is not being nice", "Not relevant/off-topic", "Other"],
MODERATION_SET, dict(
label = _("Flag Reasons"),
help_text = _("Create some flag reasons to use in the flag post popup."),
widget=StringListWidget))


CLOSE_TYPES = Setting('CLOSE_TYPES',
["Duplicate Question", "Question is off-topic or not relevant", "Too subjective and argumentative",
 "The question is answered, right answer was accepted", "Problem is not reproducible or outdated", "Other"],
MODERATION_SET, dict(
label = _("Close Reasons"),
help_text = _("Create some close reasons to use in the close question popup."),
widget=StringListWidget))
