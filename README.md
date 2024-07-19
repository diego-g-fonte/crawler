# crawler
Descarga los trabajos de titulación (pdf)de TESIUNAM junto con los metadatos (JSON)

Está pensado para que correr los programas 2.py, luego 3, 4, y así consecutivamente. 1.py no funciona,
pero lo mantengo para propósitos históricos.

Instrucciones rascuachas:
1. hacer la búsqueda en tesiunam con "licenciatura en lengua y literaturas modernas inglesas"
2. copiar la dirección de la primera página de resultados a metadata/url_manual.txt
3. correr metadata/1.py ajustando el contador del loop del final
4. copiar el contenido de metadata/urls_results_pages.txt a urls.txt
5. correr 2.py, 3.py, 4.py y 5.py

Con esto, obtienes los links a los pdfs de los trabajos de titulación de letras inglesas en pdf_links.txt.

Falta:
1. descargar los pdfs.
2. linkear los pdfs con sus metadatos
    2.1. usar los datos de los links para fechar los trabajos. (o decidir juzgarlas por año y no ser tan específico con las fechas)
bonus. hacer que el código sea limpio y no así de rascuacho

5.py es un copy paste de chat gpt.