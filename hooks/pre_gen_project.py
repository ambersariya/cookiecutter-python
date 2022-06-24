import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

package_slug = '{{ cookiecutter.package_slug }}'

if not re.match(MODULE_REGEX, package_slug):
    print('ERROR: %s is not a valid Python module name!' % package_slug)
    # exits with status 1 to indicate failure
    sys.exit(1)
else:
    print('Post Creation Validation: Everything looks good')
