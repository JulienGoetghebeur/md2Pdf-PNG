"""
Convert md file to html files
BUT info S1 2021 SAE1.04
Goetghebeur Julien
"""


numPage = -1
codeEnCours = False
listeEnCours = False



def newPage():
	global numPage, fichierHTML
	if numPage >= 0:
		fichierHTML.write("</body>\n")
		fichierHTML.write("</html>\n")
		fichierHTML.close()
	numPage += 1
	nomPage = "html/page" + str(numPage) + ".html"
	print("Création du fichier ",nomPage)
	fichierHTML = open(nomPage,"w")

	# ajout de la base de la page
	fichierHTML.write("<!DOCTYPE html>\n")
	fichierHTML.write("<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='fr' lang='fr'>\n")
	fichierHTML.write("<head>\n")
	fichierHTML.write("<meta charset=utf-8 />\n")
	fichierHTML.write("<link rel=stylesheet type='text/css' href='style.css' />\n")
	fichierHTML.write("</head>\n")
	fichierHTML.write("<body>\n")


print("Lecture du fichier")
fichierMD = open("md/config.md","r")
lignes = fichierMD.readlines()

for numLigne,ligne in enumerate(lignes):
	ligne = ligne[:-1]

	if numLigne == 0 :
		newPage()

	if ligne == "---":
		newPage()

	elif ligne == "":
		if listeEnCours :
			txt = "</ul>\n"
			listeEnCours = False
		else:
			txt = "\n"
		fichierHTML.write(txt)

	elif len(ligne) > 2 and ligne[2] == "#" :
		txt = "<header>\n<h3>" + ligne[4:] + "</h3>\n</header>\n"
		fichierHTML.write(txt)

	elif len(ligne) > 1 and ligne[1] == "#":
		txt = "<header>\n<h2>" + ligne[3:] + "</h2>\n</header>\n"
		fichierHTML.write(txt)

	elif ligne[0] == "#":
		txt = "<header>\n<h1>" + ligne[2:] + "</h1>\n</header>\n"
		fichierHTML.write(txt)

	elif ligne == "```":
		if codeEnCours:
			txt = "</div>\n"
			codeEnCours = False
		else :
			txt = "<div class=code>\n"
			codeEnCours = True
		fichierHTML.write(txt)

	elif ligne[0] == "-":
		if not listeEnCours:
			fichierHTML.write("<ul>\n");
			listeEnCours = True
		txt = "<li>" + ligne[1:] + "</li>\n"
		fichierHTML.write(txt)

	else:
		txt = "<p>" + ligne + "</p>\n"
		fichierHTML.write(txt)

fichierMD.close()





