# Network-Visualization-Project
A network of US airports and the flights between them. FlightGraph.pdf is the network mapped over a map of the United States. The edges curve clockwise to show direction of the flight. The network visualization was processed in Gephi.

<b>Supporting files:</b><br>
edgesFlights.tsv - edges of network<br>
nodesFlights.csv - nodes of network (after script was run)<br>
Airport_Codes.csv - set of airport codes mapped to their coordinates<br>

<b>Script:</b><br>
airportCodes.py - edits the nodesFlights.csv contents (originally only containing id and name columns) to add latitude and longitude.<br>

<b>Data source:</b><br>
http://konect.uni-koblenz.de/networks/opsahl-usairport

