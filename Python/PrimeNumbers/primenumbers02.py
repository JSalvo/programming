########################################################################
# This program is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or    #
# (at your option) any later version.                                  #
#                                                                      #
# This program is distributed in the hope that it will be useful,      #     
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU General Public License for more details.                         #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.#
#                                                                      #
# <author>Gianmario Salvetti</author>                                  #
# <date>2013-11-12</date>                                              #
# <summary>Stampa i numeri primi da 2 a n</summary>                    #
#                                                                      #
#                                                                      #
# ######################################################################
 
 
 
n = 100
 
 
 
# Produce True se un numero e' primo
def prime(candidate):
    # Verifica se candidate e' divisibile per i numeri che vanno
    # da 2 alla sua meta' (anche se sarebbe sufficiente fino alla sua radice)
    for i in range(2, candidate / 2):
        # Se il resto della seguente divisione e' nullo ...     
        if candidate % i == 0:
            return False # ... candidate non e' primo
     
    # Se sono arrivato a questo punto del programma, candidate e' primo 
    return True
 
 
# Testo tramite la funzione prime i numeri compresi tra 2 e n
for i in range(2, n):
    if prime(i): # Se i e' primo ...
        print i # ... lo stampo a video
 
# Fine
