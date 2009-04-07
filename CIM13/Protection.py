#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM13.Core import Equipment
from CIM13.Core import IdentifiedObject



from enthought.traits.api import Instance, List, Float, Bool, Int
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "ProtectionEquipment" class:
#------------------------------------------------------------------------------

class ProtectionEquipment(Equipment):
    """ An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Circuit breakers may be operated by protection relays.
    Operates_Breakers = List(Instance("CIM13.Wires.ProtectedSwitch"))

    # Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
    ConductingEquipments = List(Instance("CIM13.Core.ConductingEquipment"))

    # The Protection Equipments having the Unit.
    Unit = Instance("CIM13.Core.Unit")

    # Direction same as positive active power flow value.
    powerDirectionFlag = Bool

    # The minimum allowable value.
    lowLimit = Float

    # The maximum allowable value.
    highLimit = Float

    # The time delay from detection of abnormal conditions to relay operation.
    relayDelayTime = Float

    #--------------------------------------------------------------------------
    #  Begin protectionEquipment user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End protectionEquipment user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RecloseSequence" class:
#------------------------------------------------------------------------------

class RecloseSequence(IdentifiedObject):
    """ A reclose sequence (open and close) is defined for each possible reclosure of a breaker.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A breaker may have zero or more automatic reclosures after a trip occurs.
    Breaker = Instance("CIM13.Wires.ProtectedSwitch")

    # Indicates the time lapse before the reclose step will execute a reclose.
    recloseDelay = Float

    # Indicates the ordinal position of the reclose step relative to other steps in the sequence.
    recloseStep = Int

    #--------------------------------------------------------------------------
    #  Begin recloseSequence user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End recloseSequence user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SynchrocheckRelay" class:
#------------------------------------------------------------------------------

class SynchrocheckRelay(ProtectionEquipment):
    """ A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The maximum allowable difference voltage across the open device
    maxVoltDiff = Float

    # The maximum allowable frequency difference across the open device
    maxFreqDiff = Float

    # The maximum allowable voltage vector phase angle difference across the open device
    maxAngleDiff = Float

    #--------------------------------------------------------------------------
    #  Begin synchrocheckRelay user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End synchrocheckRelay user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurrentRelay" class:
#------------------------------------------------------------------------------

class CurrentRelay(ProtectionEquipment):
    """ A device that checks current flow values in any direction or designated direction
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Current limit #3 for inverse time pickup
    currentLimit3 = Float

    # Current limit #1 for inverse time pickup
    currentLimit1 = Float

    # Inverse time delay #3 for current limit #3
    timeDelay3 = Float

    # Set true if the current relay has inverse time characteristic.
    inverseTimeFlag = Bool

    # Inverse time delay #1 for current limit #1
    timeDelay1 = Float

    # Current limit #2 for inverse time pickup
    currentLimit2 = Float

    # Inverse time delay #2 for current limit #2
    timeDelay2 = Float

    #--------------------------------------------------------------------------
    #  Begin currentRelay user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End currentRelay user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------