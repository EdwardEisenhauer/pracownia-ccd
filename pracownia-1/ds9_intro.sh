#!/bin/bash

animate="-blink yes -blink interval 0.5"
scale="-zscale"
zoom="-zoom to fit -match scale"

ds9 $@ $scale $zoom $animate # There is no need to create a loop
