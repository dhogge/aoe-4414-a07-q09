# max_bitrate.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Dylan Hogge
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
c = 299792458
L_l =10**(-1/10)
L_a = 10**(0/10)


# initialize script arguments
tx_w = float('nan') 
tx_gain_db = float('nan') 
freq_hz = float('nan') 
dist_km = float('nan')
rx_gain_db = float('nan') 
n0_j = float('nan') 
bw_hz = float('nan') 

# parse script arguments
if len(sys.argv)==8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
    print(\
        'Usage: '\
        'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
            )
    exit()

# write script below this line
lam = c/freq_hz
S = dist_km*1000

C = tx_w*L_l*tx_gain_db*((lam/(4*math.pi*S))**2)*L_a*rx_gain_db
N = n0_j*bw_hz
r_max = bw_hz*math.log((1+C/N),2)

print(math.floor(r_max))
