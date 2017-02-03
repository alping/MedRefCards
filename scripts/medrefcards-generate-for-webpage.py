#!/usr/bin/python

# Script for generating medical reference cards for distribution on medrefcards.alping.se
# Copyright (C) 2016 Peter Alping
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Peter Alping
# medrefcards@alping.se

import MedRefCards

med_ref_cards = MedRefCards.MedRefCards('swe', 'all', '../contents')
med_ref_cards.generate_pdf('default-colour-scheme', 'screen', '../pdf')
# med_ref_cards.generate_pdf('default-colour-scheme', 'screen-wide', '../pdf')
# med_ref_cards.generate_pdf('default-colour-scheme', 'print', '../pdf')
med_ref_cards.generate_pdf('default-colour-scheme', 'print-spread', '../pdf')
med_ref_cards.generate_pdf('default-colour-scheme', 'print-double-sided', '../pdf')
