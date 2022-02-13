#!/bin/bash
#SAE103 BUT info 2022
#GOETGHEBEUR Julien

echo "Création du dossier png_pdf"
mkdir -p png_pdf
echo "En attente des fichiers pdf et png"
while true
do
	if [[ -f png/style.css ]]; then
		if [[ -f pdf/style.css ]]; then
			echo "Fichiers trouvés"
			rm html/style.css
			rm png/style.css
			rm pdf/style.css
			echo "récupération des fichiers vers png_pdf"
			cd png
			for ficPng in *.png
			do
				cp $ficPng ../png_pdf/$ficPng
			done
			cd ../pdf
			for ficPdf in *.pdf 
			do
				cp $ficPdf ../png_pdf/$ficPdf
			done
			cd ..
			echo "contenu png_pdf :"
			ls png_pdf
			echo "Création archive"
			tar czf archive.tgz png_pdf
			rm -r png_pdf
			echo "Fin traitement"
		fi
	fi
	sleep 5
done