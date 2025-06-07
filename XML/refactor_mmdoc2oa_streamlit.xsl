<?xml version="1.0" encoding="UTF-8"?>
<!-- edited with XMLSpy v2009 (http://www.altova.com) by s0315 (s0315) -->
<!--
========
**20221016**
========
Consider exdpanding refactor to include the whole Streamlit Specs from:

* [Streamlit Cheatsheet](StreamlitCheatsheet.mm)
* [Steamlit Doc]()

-->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" exclude-result-prefixes="fo fn xs xsl">
	<xsl:output method="xml" encoding="utf-8" omit-xml-declaration="no" indent="yes" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions"/>
	<!--
	<xsl:strip-space elements="*"/>
-->
	<xsl:key name="param_keys" match="//xsl:template/xsl:param" use="@name"/>
	<xsl:param name="creation_date">
		<xsl:value-of select="format-dateTime(current-dateTime(), 
		'[Y0001]/[M01]/[D01] [h01]:[m01]:[s01] [P] [z] ')"/>
	</xsl:param>
	<xsl:param name="pad">
		<xsl:text>    </xsl:text>
	</xsl:param>
	<xsl:param name="ret">
		<xsl:text>&#010;</xsl:text>
	</xsl:param>
	<xsl:param name="tab">
		<xsl:text>&#009;</xsl:text>
	</xsl:param>
	<xsl:param name="template_name"/>
	<xsl:param name="template_params">
		<xsl:for-each select="$refactor_list/refactor_item[@class = 'template_param']">
			<xsl:sort select="concat(@type,@name)"/>
			<xsl:attribute name="{@name}"/>
		</xsl:for-each>
	</xsl:param>
	<xsl:param name="refactor_list">
		<refactor_item type="template_param" name="collect_answer" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="form_key" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="form_return" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="group_pos" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="indent" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="n_checkboxs" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="n_cols" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="n_tabs" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="name" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="node_key" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="node_level" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="pos" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="st_layout" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="st_prefix" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="submit_return" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="submit_text" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="type" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template_param" name="variable_name" class=" ">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template" name="/" class="base">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_camera_input" class="widget">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_checkbox" class="widget">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_col" class="widget">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_collect_answer" class="widget">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_color_picker" class="widget">
			<description><![CDATA[
			]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_columns" class="layout">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_date_input" class="widget">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_expander" class="basic">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_file_uploader" class="basic">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_html" class="component">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_multiselect" class="widget">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_node_tree" class="main">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_radio" class="widget">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_selectbox" class="widget">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_selectslider" class="widget">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_sidebar" class="layout">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_slider" class="widget">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_st_form" class="form">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_st_submit" class="form">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_tab" class="layout">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_tabs" class="layout">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_text_area" class="widget">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_text_input" class="widget">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template" name="mk_time_input" class="widget">
			<description><![CDATA[]]></description>
		</refactor_item>
		<refactor_item type="template_class" name="base">
			<description><![CDATA[Basic template for building app]]></description>
		</refactor_item>
		<refactor_item type="template_class" name="simple">
			<description><![CDATA[Simple streamlit command (To be validated with docs)]]></description>
		</refactor_item>
		<refactor_item type="template_class" name="component">
			<description><![CDATA[Custom designed component (Complex cases to be researched)]]></description>
		</refactor_item>
		<refactor_item type="template_class" name="form">
			<description><![CDATA[Form & Form Submit Button. (Form Widgets are an indepente classes)]]></description>
		</refactor_item>
		<refactor_item type="template_class" name="layout">
			<description><![CDATA[Page layouts alternatives (Tabs, Columns, Sidebar...)]]></description>
		</refactor_item>
		<refactor_item type="template_class" name="main">
			<description><![CDATA[Main dispatcher for building app]]></description>
		</refactor_item>
		<refactor_item type="template_class" name="widget">
			<description><![CDATA[Each one of different form widgets]]></description>
		</refactor_item>
		<refactor_item type="with_param" name="widget">
			<description><![CDATA[Each one of different form widgets]]></description>
		</refactor_item>
	</xsl:param>
	<xsl:param name="oa_result_fields">
		<refactor_item type="oa_result_field" name="n" weight="0"/>
		<refactor_item type="oa_result_field" name="title" weight="10"/>
		<refactor_item type="oa_result_field" name="webresource" weight="11"/>
		<refactor_item type="oa_result_field" name="doi" weight="13"/>
		<refactor_item type="oa_result_field" name="openaireid" weight="14"/>
		<refactor_item type="oa_result_field" name="authors" weight="15"/>
		<refactor_item type="oa_result_field" name="sourcejournal" weight="16"/>
		<refactor_item type="oa_result_field" name="publicationtype" weight="20"/>
		<refactor_item type="oa_result_field" name="bestlicense" weight="30"/>
		<refactor_item type="oa_result_field" name="dateofacceptance" weight="40"/>
		<refactor_item type="oa_result_field" name="description" weight="90"/>
	</xsl:param>
	<xsl:param name="Streamlit_doc_nav">
	</xsl:param>
	<!-- EJEMPLO RECURSIÓN -->
	<xsl:variable name="recursion_example">
		<xsl:element name="xsl:recursion_example" inherit-namespaces="yes" xpath-default-namespace="xsl">
			<xsl:text disable-output-escaping="yes"><![CDATA[
			<xsl:if test="count(node[@type != 'no']) > 0">
				<xsl:for-each select="node">
					<xsl:call-template name="mk_node_tree">
						<xsl:with-param name="pos">
							<xsl:value-of select="concat($pos, '.', position())"/>
						</xsl:with-param>
						<xsl:with-param name="indent">
							<xsl:value-of select="concat($indent, $pad)"/>
						</xsl:with-param>
						<xsl:with-param name="type">
							<xsl:value-of select="@type"/>
						</xsl:with-param>
						<xsl:with-param name="node_level">
							<xsl:value-of select="number($node_level) + 1"/>
						</xsl:with-param>
						<xsl:with-param name="group_pos">
							<xsl:value-of select="position()"/>
						</xsl:with-param>
						<xsl:with-param name="name">
							<xsl:value-of select="upper-case(@TEXT)"/>
						</xsl:with-param>
						<xsl:with-param name="st_prefix">
							<xsl:value-of select="$st_prefix"/>
						</xsl:with-param>
						<xsl:with-param name="n_tabs">
							<xsl:value-of select="$n_tabs"/>
						</xsl:with-param>
						<xsl:with-param name="n_cols">
							<xsl:value-of select="$n_cols"/>
						</xsl:with-param>
						<xsl:with-param name="node_key">
							<xsl:value-of select="concat(generate-id(), '_', @ID)"/>
						</xsl:with-param>
						<xsl:with-param name="st_layout">
							<xsl:value-of select="$st_layout"/>
						</xsl:with-param>
						<xsl:with-param name="form_return">
							<xsl:value-of select="$form_return"/>
						</xsl:with-param>
						<xsl:with-param name="submit_return">
							<xsl:value-of select="$submit_return"/>
						</xsl:with-param>
						<xsl:with-param name="form_key">
							<xsl:value-of select="$form_key"/>
						</xsl:with-param>
						<xsl:with-param name="collect_answer">
							<xsl:value-of select="$collect_answer"/>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:for-each>
			</xsl:if>
			]]></xsl:text>
		</xsl:element>
	</xsl:variable>
	<!-- TEMPLATE LIST -->
	<xsl:variable name="template_list" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
		<xsl:for-each select="$refactor_list//*[@type = 'template']">
			<xsl:sort select="concat(@class,' ',@name)"/>
			<xsl:element name="xsl:template" inherit-namespaces="yes" xpath-default-namespace="xsl">
				<xsl:attribute name="class"><xsl:value-of select="@class"/></xsl:attribute>
				<xsl:attribute name="name"><xsl:value-of select="@name"/></xsl:attribute>
			</xsl:element>
		</xsl:for-each>
	</xsl:variable>
	<!-- PARAM_LIST -->
	<xsl:variable name="param_list" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
		<!-- PARAM LIST -->
		<xsl:for-each select="$refactor_list//*[@type = 'template_param']">
			<xsl:sort select="concat(@class,' ',@name)"/>
			<xsl:element name="xsl:param" inherit-namespaces="yes" xpath-default-namespace="xsl">
				<xsl:attribute name="name"><xsl:value-of select="@name"/></xsl:attribute>
			</xsl:element>
		</xsl:for-each>
	</xsl:variable>
	<!-- XSL PAGE PARAMS -->
	<xsl:param name="xsl_page_params">
		<xsl:for-each select="/doc/xsl:stylesheet/xsl:param">
			<xsl:sort select="@name"/>
			<xsl:element name="{local-name()}">
				<xsl:attribute name="name"><xsl:value-of select="@name"/></xsl:attribute>
				<xsl:attribute name="position"><xsl:value-of select="position()"/></xsl:attribute>
				<xsl:attribute name="type"> </xsl:attribute>
				<xsl:attribute name="description"> </xsl:attribute>
				<xsl:if test=". != ''">
					<xsl:attribute name="value"><xsl:value-of select="."/></xsl:attribute>
				</xsl:if>
			</xsl:element>
		</xsl:for-each>
	</xsl:param>
	<!-- WITH_PARAM -->
	<xsl:param name="with_param">
		<!--
				<xsl:element name="xsl:with-param" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" inherit-namespaces="yes" xpath-default-namespace="xsl">
-->
		<xsl:for-each select="//xsl:call-template">
			<xsl:sort select="@name"/>
			<xsl:element name="xsl:call-template" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" inherit-namespaces="yes" xpath-default-namespace="xsl">
				<xsl:attribute name="name"><xsl:value-of select="@name"/></xsl:attribute>
				<xsl:for-each select="xsl:with-param">
					<xsl:sort select="@name"/>
					<xsl:copy-of select="."/>
				</xsl:for-each>
			</xsl:element>
		</xsl:for-each>
		<!--
			</xsl:element>
-->
	</xsl:param>
	<!-- WITH_PARAM_LIST -->
	<xsl:variable name="with_param_list" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
		<xsl:for-each select="$with_param//*[local-name() = 'with-param']">
			<xsl:sort select="@name"/>
			<xsl:element name="xsl:with_param" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" inherit-namespaces="yes" xpath-default-namespace="xsl">
				<xsl:attribute name="name"><xsl:value-of select="@name"/></xsl:attribute>
				<xsl:attribute name="template"><xsl:value-of select="../@name"/></xsl:attribute>
				<xsl:attribute name="select"><xsl:value-of select="xsl:value-of/@select"/></xsl:attribute>
				<xsl:copy-of select="./*[local-name() != 'value-of']"/>
			</xsl:element>
		</xsl:for-each>
	</xsl:variable>
	<!-- MAIN -->
	<xsl:template match="/" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
		<!-- TEMPLATE_BODIES -->
		<xsl:variable name="template_bodies">
			<!-- TEMPLATE_BODY -->
			<xsl:for-each select="//*[local-name() = 'template']">
				<xsl:element name="element_body">
					<xsl:attribute name="name"><xsl:value-of select="@name"/></xsl:attribute>
					<xsl:copy-of select="./*[local-name() != 'param']"/>
				</xsl:element>
			</xsl:for-each>
		</xsl:variable>
		<xsl:element name="xsl:refactor" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" inherit-namespaces="yes" xpath-default-namespace="xsl">
			<xsl:element name="xsl:lists" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" inherit-namespaces="yes" xpath-default-namespace="xsl">
				<xsl:copy-of select="$refactor_list"/>
				<xsl:copy-of select="$template_list"/>
				<xsl:copy-of select="$param_list"/>
				<xsl:copy-of select="$with_param_list"/>
				<xsl:copy-of select="$template_bodies"/>
				<xsl:copy-of select="$recursion_example"/>
			</xsl:element>
			<!--
			<lists>
				<xsl:copy-of select="$key_params_content"/>
				<xsl:copy-of select="$all_params0"/>
				<xsl:copy-of select="$all_params_ok"/>
				<xsl:copy-of select="$xsl_param"/>
				<xsl:copy-of select="$template_params"/>
			</lists>
-->
			<!-- TEMPLATE CONTENT -->
			<xsl:element name="stylesheet">
				<xsl:attribute name="version">2.0</xsl:attribute>
				<xsl:attribute name="creation_date"><xsl:value-of select="$creation_date"/></xsl:attribute>
				<xsl:for-each select="//xsl:*[local-name() = 'template']">
					<xsl:call-template name="mk_node">
						<xsl:with-param name="type">
							<xsl:value-of select="local-name()"/>
						</xsl:with-param>
						<xsl:with-param name="name">
							<xsl:choose>
								<xsl:when test="@match != ''">main</xsl:when>
								<xsl:otherwise>
									<xsl:value-of select="@name"/>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:with-param>
						<xsl:with-param name="template_name">
							<xsl:value-of select="@name"/>
						</xsl:with-param>
						<xsl:with-param name="template_list">
							<xsl:value-of select="$template_list"/>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:for-each>
				<!-- TEMPLATE_BODY -->
				<xsl:for-each select="xsl:*">
					<xsl:choose>
						<xsl:when test="xsl:*[local-name() = 'with-param']"/>
						<xsl:otherwise>
							<xsl:call-template name="mk_node">
								<xsl:with-param name="type">
									<xsl:value-of select="local-name()"/>
								</xsl:with-param>
								<xsl:with-param name="name">
									<xsl:value-of select="@name"/>
								</xsl:with-param>
								<xsl:with-param name="template_name">
									<xsl:value-of select="@name"/>
								</xsl:with-param>
								<xsl:with-param name="template_list">
									<xsl:value-of select="$template_list"/>
								</xsl:with-param>
							</xsl:call-template>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:for-each>
			</xsl:element>
		</xsl:element>
	</xsl:template>
	<!-- MK_ NODE -->
	<xsl:template name="mk_node">
		<xsl:param name="type"/>
		<xsl:param name="name"/>
		<xsl:param name="template_name"/>
		<xsl:param name="template_list"/>
		<xsl:choose>
			<xsl:when test="local-name() = 'param'"/>
			<xsl:otherwise>
				<xsl:element name="{local-name()}">
					<xsl:element name="template_body">
						<xsl:attribute name="name"><xsl:value-of select="local-name()"/></xsl:attribute>
						<xsl:if test="count(@*) > 0">
							<xsl:for-each select="@*">
								<xsl:sort select="."/>
								<xsl:sort select="local-name()"/>
								<xsl:attribute name="{local-name()}"><xsl:value-of select="."/></xsl:attribute>
							</xsl:for-each>
						</xsl:if>
						<xsl:value-of select="text()"/>
						<xsl:if test="count(*) > 0">
							<xsl:for-each select="*">
								<xsl:choose>
									<xsl:when test="xsl:*[local-name() = 'with-param']"/>
									<xsl:otherwise>
										<xsl:call-template name="mk_node">
											<xsl:with-param name="type">
												<xsl:value-of select="local-name()"/>
											</xsl:with-param>
											<xsl:with-param name="name">
												<xsl:value-of select="local-name()"/>
											</xsl:with-param>
											<xsl:with-param name="template_name">
												<xsl:value-of select="@name"/>
											</xsl:with-param>
											<xsl:with-param name="template_list">
												<xsl:value-of select="$template_list"/>
											</xsl:with-param>
										</xsl:call-template>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:for-each>
						</xsl:if>
					</xsl:element>
				</xsl:element>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
	<!-- TEXT() -->
	<xsl:template match="text()"/>
	<!-- MK_TEMPLATE_LIST -->
	<xsl:template name="mk_lists">
		<xsl:comment>
			<xsl:for-each select="//*[local-name() = 'template'][@name]">
				<xsl:value-of select="concat($ret,'template:',$tab,@name,$tab,$tab,'params:',$tab)"/>
				<xsl:for-each select="*[local-name() = 'param']">
					<xsl:sort select="@name"/>
					<xsl:value-of select="@name"/>
					<xsl:if test="position() != last()">, </xsl:if>
				</xsl:for-each>
			</xsl:for-each>
		</xsl:comment>
	</xsl:template>
	<!-- MK_TEMPLATE_PARAMETERS -->
	<xsl:template name="mk_template_parameters"/>
	<!-- MK_GENERIC RECURSION -->
	<xsl:template name="mk_generic_recursion"/>
	<!-- MK_ELEMENT_CODE -->
	<xsl:template name="mk_element_code"/>
	<!-- MK_CODE_PREAMBLE -->
	<xsl:template name="mk_code_preamble"/>
	<!-- MK_FORM_OPTION_DICTIONARY_ANSWER -->
	<xsl:template name="mk_form_optiona_dictionary"/>
	<!-- MK_FORM_COLLECT_ANSWER -->
	<xsl:template name="mk_form_collect_answer"/>
	<!--
  * Template Parameters
  * Code preamble for layout containers
    o Include option dictionary generator (tabs, columns)
  * Element code
  * Collect-Answer for form widgets
  * Generic recursion
-->
</xsl:stylesheet>
