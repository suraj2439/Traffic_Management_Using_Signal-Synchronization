
Project Name:- Traffic Management Using Signal Syncronization.

Team Members:-	
	1) Siddhesh Rajendra Mehta 	MIS: 111903105
	2) Tushar Ram Godbole		MIS: 111903115
	3) Suraj Machhindra Yerkal	MIS: 111903109
Programming Language Used:- PYTHON
GUI:- PYGAME
Supporting Libraries:-
	pygame
	matplotlib
	time
	random
	numpy


Project Discription:-

Cause Of Traffic:
	By normal observation we can see that traffic problem occurs only at some
specific location like big highways other location donot have much traffic at
same time. This is because highways have many subrouts connected. Generally
these subrouts which are connected to highway donot have traffic problem but
when vehicles on these subrouts add up in highway leads to traffic problem in
highway.

Solution:
	In current situation if there is traffic problem at some point that particular
traffic signal system fails to solve traffic problem. this is because currently
traffic signal does not vary with density of vehicles present at that traffic
signal.
In the syncronization of traffic signal we will bring contact of every traffic
signal in nearby that location lets say we will syncronize all traffic signals
in Pune city.


Basic idea :
Here we are increasing and decreasing the signal duration on the road in order
to avoid traffic jams. This doc is in sink with the image shared. Suppose there
is a main road as mentioned and is linked by 5 small roads.
There is a high possibility that there is a traffic jam on the main road. The
main road contains a signal. When the signal shows red, traffic strarts
accumulating. To solve this issue of this unexpected traffic we have an idea.
Suppose the main road signal is of 60 secs. We have sensors to keep atrack of
traffic. When the traffic level reaches a threshhold value, the time of the main
road signal reduces, say that it becomes 50 secs. The time reduction is of 10
secs. This time decrease is compensated by the increase in time of the signals
of the roads connected to the main road. Say the time of each of the signals of
the 5 roads connected to the main roads increase by 2 secs each. This increase
in time of the signals depends on the traffic on these roads. Each signal is in
sink with the signals before and after it on the road.

Aim :
	Before implementing the idea we are checking the time for a vehicle to reach a
perticular destination.
	After implementing the idea we are checking the time for a vehicle to reach a
perticular destination.
	We are the comparing the two time periods and manage the optimizations.
	
	
Technology :
	Basically we have implemented this model by using GUI and some inbuilt
libraries.
	Choosen language is Python as it supports to OOP and having inbuilt
libraries related to GUI.


More information is present in the "Traffic_Management.pdf" file.

