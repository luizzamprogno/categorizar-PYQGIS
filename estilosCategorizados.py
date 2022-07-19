import numpy as np

layer = iface.activeLayer()

#aplicar estilo de simbolo simples

'''
# print(layer.renderer().symbol().symbolLayers()[0].properties())
estilo = {'color':'blue', 'width_border':'0.3'}
simbolo = QgsFillSymbol.createSimple(estilo)

layer.renderer().setSymbol(simbolo)
iface.layerTreeView().refreshLayerSymbology(layer.id())
layer.triggerRepaint()
'''

nome_campo = 'Classes'
campo = layer.fields().lookupField(nome_campo)
valores_unicos = layer.dataProvider().uniqueValues(campo)

categorias = []

for valor in valores_unicos:

	cor = np.random.choice(range(256), size=3)
	paleta_cores = ','.join([str(elem) for elem in cor])

	# imprimir todas as propriedades do layer
	estilo = {'color':paleta_cores, 'width_border':'0.3'}
	

	simbolo = QgsSymbol.defaultSymbol(layer.geometryType())
	layer_simbolo = QgsSimpleFillSymbolLayer().create(estilo)

	simbolo.changeSymbolLayer(0, layer_simbolo)

	categoria = QgsRendererCategory(valor, simbolo, str(valor))
	categorias.append(categoria)

	categorizado = QgsCategorizedSymbolRenderer(nome_campo, categorias)

layer.setRenderer(categorizado)
layer.triggerRepaint()