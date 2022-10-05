The tikzpeople package provides people shaped nodes to be used in tikz.
The available node shapes are:

alice, bob, bride, builder, businessman, charlie, chef, conductor, cowboy, 
criminal, dave, devil, duck, graduate, groom, guard, jester, judge, maninblack, 
mexican, nun, nurse, physician, pilot, police, priest, sailor, santa, surgeon

The package has four options:
- The "draft" option causes all tikzpeople to be rendered as a basic outline 
		of a person.
- The "demo" option adds two commands. 
	The command \alltikzpeople{<width>}{<options>} produces a series of figures 
	of all available shapes with the given width and the provided options 
	applied. The command \tikzpeoplecolors{<shapename>} produces a figure 
	showing the available color keys for the shape.
- The "nonbeards" option removes all beards.
- The "saturated" option causes the tikzpeople to be drawn with saturated colors.
	
The nodes have the following hopefully self explanatory options:

evil, good, female, mirrored, monitor, saturated, shield, sword

All options can be combined freely.

The tikzpeople package is licensed under the LaTeX Project Public License

 -- Nils Fleischhacker <mail@nilsfleischhacker.de>  22 Apr 2017
