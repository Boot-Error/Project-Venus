#!/usr/bin/env python

import os
import re
import math

def tokenize(sentence):
	
	s = sentence.lower()
	result = []	

	for i in s.split(" "):
		
		for j in ["?", ".", "!"]:
				
			i = i.rstrip(j)

		result.append(i)
	
	return result

				
				
