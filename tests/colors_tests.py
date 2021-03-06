# Copyright (C) 2010-2014 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from nose.tools import assert_equals

from lib.cuckoo.common.colors import color


def test_return_text():
    """Test colorized text contains the input string."""
    assert "foo" in color("foo", 11)