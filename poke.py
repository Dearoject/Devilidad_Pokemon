#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
print sys.argv[1:]

# typos:
types = ["normal",
	"fire", "water", "grass", "electric",
	"ice", "fighting", "poison", "ground", "flying",
	"psychic", "bug", "rock", "ghost", "dragon",
	"dark", "steel", "fairy"
	]

# La primera pose és zero
# La segona és 1/2
# La tercera és 2
dic = {
	"normal":(("ghost"),(),("fighting")),
	"fire":((),("fire", "grass", "ice", "bug", "steel", "fairy"),("water", "ground", "rock")),
	"water":((),("fire", "water", "ice", "steel"),("grass", "electric")),
	"grass":((),("water", "grass", "electric", "ground"),("fire", "ice", "poison", "flying", "bug")),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	"model":((),(),()),
	}
