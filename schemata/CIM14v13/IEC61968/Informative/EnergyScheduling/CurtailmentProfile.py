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

from CIM14v13.IEC61968.Informative.EnergyScheduling.Profile import Profile

class CurtailmentProfile(Profile):
    """Curtailing entity must be providing at least one service to the EnergyTransaction. The CurtailmentProfile must be completely contained within the EnergyProfile timeframe for this EnergyTransaction.
    """

    def __init__(self, EnergyTransaction=None, *args, **kw_args):
        """Initializes a new 'CurtailmentProfile' instance.

        @param EnergyTransaction: An EnergyTransaction may be curtailed by any of the participating entities.
        """
        self._EnergyTransaction = None
        self.EnergyTransaction = EnergyTransaction

        super(CurtailmentProfile, self).__init__(*args, **kw_args)

    def getEnergyTransaction(self):
        """An EnergyTransaction may be curtailed by any of the participating entities.
        """
        return self._EnergyTransaction

    def setEnergyTransaction(self, value):
        if self._EnergyTransaction is not None:
            filtered = [x for x in self.EnergyTransaction.CurtailmentProfiles if x != self]
            self._EnergyTransaction._CurtailmentProfiles = filtered

        self._EnergyTransaction = value
        if self._EnergyTransaction is not None:
            self._EnergyTransaction._CurtailmentProfiles.append(self)

    EnergyTransaction = property(getEnergyTransaction, setEnergyTransaction)
