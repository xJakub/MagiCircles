# django-recaptcha3==0.4.0 (its latest release, still) imports the removed
# django.utils.translation.ugettext_lazy (hard-removed in Django 4.0) - same
# unmaintained-dependency situation as django-bootstrap-form's broken render()
# (patched in magi/urls.py). Restore the old name as an alias for gettext_lazy
# before any submodule here gets a chance to trigger that import.
from django.utils import translation as _translation
if not hasattr(_translation, 'ugettext_lazy'):
    _translation.ugettext_lazy = _translation.gettext_lazy

# django-bootstrap-form==3.2 (its latest release, still) does
# `from distutils.version import StrictVersion` just to stringify a version
# number (bootstrapform/meta.py). distutils was removed entirely in Python
# 3.12. Provide a minimal stand-in before that import can run.
import sys as _sys
if 'distutils' not in _sys.modules:
    import types as _types
    _distutils = _types.ModuleType('distutils')
    _distutils_version = _types.ModuleType('distutils.version')
    class _StrictVersion(object):
        def __init__(self, vstring=None):
            self.vstring = vstring
        def __str__(self):
            return self.vstring
    _distutils_version.StrictVersion = _StrictVersion
    _distutils.version = _distutils_version
    _sys.modules['distutils'] = _distutils
    _sys.modules['distutils.version'] = _distutils_version
