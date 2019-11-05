#!/bin/bash
apt install cowsay && \
	mkdir -p /etc/mannaggia.d && \
	cp src/mannaggia /usr/sbin/mannaggia && \
	cp src/cowdamn /usr/sbin/cowdamn && \
	cp src/mannaggia.dat  /etc/mannaggia.d/mannaggia.dat && \
	cp src/mannaggia.cow  /etc/mannaggia.d/mannaggia.cow && \
	chmod +x /usr/sbin/mannaggia && \
	chmod +x /usr/sbin/cowdamn && \
	echo "Mannaggia e cowdamn installati con successo. Adesso anche tu puoi mannaggiare come un vero system administrator"
