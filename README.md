ulInterference.mos uses avg.py -for LTE UlInterference calculation.
avg.py must be placed in the same directory as this script.
The path for the files must be set under "Initial variables" in both scripts.
Since python works from scripting-vm only, you need to enter to that first.

To enter to scripting-vm on ENM do as follows:

Option-a)
Launch "Shell Terminal on Scripting" from ENM GUI.
Enter the node:
amos <nodename>
run this script:
runx ulinterference.mos

Option-b)
You can enter to scripting-vm via your own ssh-terminal (e.g. Mobaterm):
To find out the IP-address of the scripting-vm, launch "Shell Terminal on Scripting" from ENM GUI.
Check the IP-address of the scripting-vm by: "hostname -i" from "Shell Terminal on Scripting" on ENM GUI.
From your own ssh-terminal on your PC ssh to scripting-vm:
ssh <IP of scripting-vm>
use your ENM-pw!
Enter the node:
amos <nodename>
run this script:
runx ulinterference.mos

Note: you enter to your amos-vm by default -normally. ssh from the amos-vm to the scripting-vm works usually.
Note: You may want to add a new line to your .moshellrc -to run this script by a simple command e.g:
if your files (ulinterference.mos and avg.py) are located in ~/scripts
and you add the following to your .moshellrc:
alias intf runx ~/scripts/ulinterference.mos
then you can call the script using "intf" from your amos/moshell.
