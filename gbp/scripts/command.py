#!/usr/bin/python
# vim: set fileencoding=utf-8 :
#
# (C) 2013 Guido Günther <agx@sigxcpu.org>
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""Wrapper for all gbp commands"""

import sys

def sanitize(cmd):
    return cmd.replace('-', '_')

def usage():
    print """
Usage:
    gbp <command> [<args>]

The most commonly used commands are:

    buildpackage - build a Debian package
    import-orig  - import a new upstream tarball
    import-dsc   - import a single Debian source package
    import-dscs  - import multiple Debian source packages
"""

def import_command(cmd):
    if '.' in cmd:
        raise ImportError('Illegal module name')

    m = __import__('gbp.scripts.%s' % cmd, fromlist='main', level=0)
    return m


def gbp_command(argv=None):
    argv = argv or sys.argv

    if len(argv) < 2:
        usage()
        return 1

    cmd = argv[1]
    args = argv[1:]

    if cmd in ['--help', '-h']:
        usage()
        return 0

    modulename = sanitize(cmd)
    try:
        module = import_command(modulename)
    except ImportError as e:
        print >>sys.stderr, "'%s' is not a valid command." % cmd
        usage()
        if '--verbose' in args:
            print >>sys.stderr, e
        return 2

    return module.main(args)

# vim:et:ts=4:sw=4:et:sts=4:ai:set list listchars=tab\:»·,trail\:·:
