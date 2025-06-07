<?xml version="1.0" encoding="UTF-8"?>
<!--
20220607
Agregar generación de widgets
- Se debe partir de una definición de un sistema de multipáginas
- Redefinir 
  - la plantilla de atributos
  - elementos de soporte para las funcionalidades
  - hacer análisis preliminar en una hoja de cálculo para general el XML definitivo
  - hacer ingenieria inversa del resultado esperado a partir de un ejemplo
  - Diferenciar bien Siidebar y multipage
  - generar Markdown para casos especiales
  - preprarar rachivoo requirementes.txt para garantizar instalación sin tropiezos
-->

<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<xsl:output encoding="utf-8" method="text" indent="yes"/>
	<xsl:param name="fill">
		<xsl:text>&#09;</xsl:text>
	</xsl:param>
	<xsl:param name="ret">
		<xsl:text>&#xA;</xsl:text>
	</xsl:param>
	<xsl:template match="/">
		<xsl:for-each select="/doc/node[@text='DESARROLLO']/node[@text='APIS']">import streamlit as st

#
<xsl:for-each select="node">
				<xsl:call-template name="mk_widget">
					<xsl:with-param name="nudge">#</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
		</xsl:for-each>
	</xsl:template>
	<!-- MK_WIDGET -->
	<xsl:template name="mk_widget">
		<xsl:param name="nudge"/>
		<xsl:param name="pos"/>
		<xsl:variable name="indent"/>
		<xsl:value-of select="concat($nudge,position(),': ',@text,$ret)"/>
		<xsl:choose>
			<xsl:when test="@widget='checkbox'"><xsl:call-template name="mk_widget_checkbox"/></xsl:when>
		</xsl:choose>
		<xsl:if test="count(node)>0">
			<xsl:for-each select="node">
				<xsl:call-template name="mk_widget">
					<xsl:with-param name="nudge">
						<xsl:value-of select="concat($nudge,$fill)"/>
					</xsl:with-param>
					<xsl:with-param name="pos">
						<xsl:value-of select="position()"/>
					</xsl:with-param>
				</xsl:call-template>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>
	<xsl:template name="mk_widget_checkbox">
	</xsl:template>
</xsl:stylesheet>

<!--
import streamlit as st

file = "file.txt"

# Button: Display a button widget.
clicked = st.button("Click me")

#Download button: Display a download button widget.
st.download_button("Download file", file)

#Checkbox: Display a checkbox widget.
selected = st.checkbox("I agree")

#Radio: Display a radio button widget.
choice = st.radio("Pick one", ["cats", "dogs"])

#Selectbox: Display a select widget.
choice = st.selectbox("Pick one", ["cats", "dogs"])

#Multiselect: Display a multiselect widget. The multiselect widget starts as empty.
choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])

#Slider: Display a slider widget.
number = st.slider("Pick a number", 0, 100)

#Select-slider: Display a slider widget to select items from a list.
size = st.select_slider("Pick a size", ["S", "M", "L", "XL", "XXL", "XXXL"])

#Text input: Display a single-line text input widget.
name = st.text_input("First name")

#Number input: Display a numeric input widget.

choice = st.number_input("Pick a number", 0, 10)

#Text-area: Display a multi-line text input widget.
text = st.text_area("Text to translate")

#Date input: Display a date input widget.
date = st.date_input("Your birthday")

#Time input: Display a time input widget.
time = st.time_input("Meeting time")

#File Uploader: Display a file uploader widget.
data = st.file_uploader("Upload a CSV")

#Camera input: Display a widget that allows users to upload images directly from a camera.
image = st.camera_input("Take a picture")

#Color picker: Display a color picker widget.
color = st.color_picker("Pick a color")
-->
