#!/bin/bash
#script that request a POST with some determinated things
curl -sLX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
