# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61968.Informative.InfAssets.StructureSupport import StructureSupport

class Anchor(StructureSupport):
    """A type of support for structures, used to hold poles secure.
    """

    def __init__(self, kind='other', *args, **kw_args):
        """Initializes a new 'Anchor' instance.

        @param kind: Kind of this anchor. Values are: "other", "concrete", "rod", "screw", "multiHelix", "helix", "unknown"
        """
        #: Kind of this anchor.Values are: "other", "concrete", "rod", "screw", "multiHelix", "helix", "unknown"
        self.kind = kind

        super(Anchor, self).__init__(*args, **kw_args)
