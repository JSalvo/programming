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
# <summary>Stampa i numeri primi da 2 a n. (versione 2)</summary>      #
#                                                                      #
#                                                                      #
# ######################################################################
 
n = 100
 
# Determina se candidate e' primo o no, ma ha bisogno di tutti
# i numeri primi che lo precedono (primeNumbers)
def prime(candidate, primeNumbers):
    for prime in primeNumbers:
        if candidate % prime == 0:
            return False
    # Se nessun numero primo contenuto in primeNumbers e' divisore
    # di candidate allora anche candidate e' un numero primo    
    return True
 
 
# Inizializzo la lista di numeri primi con il primo numero primo
primeNumbers = [2]
 
# Eseguo il test per determinare se un numero e' primo o no, su i 
# numeri compresi tra 3 e n con step 2 (in questo modo salto il test 
# per numeri pari)
for candidate in range(3, n, 2):
    if prime(candidate, primeNumbers):
        # Se un numero e' primo, lo inserisco nella lista primeNumbers      
        primeNumbers.append(candidate)
         
 
print primeNumbers
 
 
# Fine
