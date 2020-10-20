#!/bin/bash

# Add some error handling

open_files=""

for i in $@
do
	open_files="${open_files}-fits ${i} -frame new "
done

open_files="${open_files} -frame delete" # Do something about it!

animate=""

for i in $@
do
	animate="${animate} -sleep 1 -frame next "
done

ds9 $open_files $animate