# django-recaptcha3==0.4.0 (its latest release, still) imports the removed
# django.utils.translation.ugettext_lazy (hard-removed in Django 4.0) - same
# unmaintained-dependency situation as django-bootstrap-form's broken render()
# (patched in magi/urls.py). Restore the old name as an alias for gettext_lazy
# before any submodule here gets a chance to trigger that import.
from django.utils import translation as _translation
if not hasattr(_translation, 'ugettext_lazy'):
    _translation.ugettext_lazy = _translation.gettext_lazy
