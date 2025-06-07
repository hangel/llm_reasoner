<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1665961554439" ID="ID_1275179991" LINK="https://daniellewisdl-streamlit-cheat-sheet-app-ytm9sg.streamlitapp.com/" MODIFIED="1665962319515" TEXT="StreamlitCheatsheet">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570700" ID="ID_1642988736" MODIFIED="1665961570700" POSITION="right" TEXT="Summary of the docs, as of Streamlit v1.8.0.">
<node CREATED="1665961570702" FOLDED="true" ID="ID_864047500" MODIFIED="1665962337489" TEXT="How to install and import">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570704" ID="ID_1230758803" MODIFIED="1665961570704" TEXT="$ pip install streamlit"/>
<node CREATED="1665961570705" FOLDED="true" ID="ID_1973567021" MODIFIED="1665962336539" TEXT="Import convention">
<node CREATED="1665961570706" ID="ID_507509271" MODIFIED="1665961570706" TEXT="&gt;&gt;&gt; import streamlit as st"/>
</node>
</node>
<node CREATED="1665961570707" FOLDED="true" ID="ID_546431617" MODIFIED="1665962337490" TEXT="Add widgets to sidebar">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570708" ID="ID_1300909835" MODIFIED="1665961570708" TEXT="st.sidebar.&lt;widget&gt;"/>
<node CREATED="1665961570709" ID="ID_1939230798" MODIFIED="1665961570709" TEXT="&gt;&gt;&gt; a = st.sidebar.radio(&apos;R:&apos;,[1,2])"/>
</node>
<node CREATED="1665961570711" FOLDED="true" ID="ID_64828542" MODIFIED="1665962337490" TEXT="Command line">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570712" ID="ID_1584555054" MODIFIED="1665961570712" TEXT="$ streamlit --help"/>
<node CREATED="1665961570712" ID="ID_23346415" MODIFIED="1665961570712" TEXT="$ streamlit run your_script.py"/>
<node CREATED="1665961570713" ID="ID_1913460806" MODIFIED="1665961570713" TEXT="$ streamlit hello"/>
<node CREATED="1665961570713" ID="ID_1250274051" MODIFIED="1665961570713" TEXT="$ streamlit config show"/>
<node CREATED="1665961570714" ID="ID_947052227" MODIFIED="1665961570714" TEXT="$ streamlit cache clear"/>
<node CREATED="1665961570715" ID="ID_214497151" MODIFIED="1665961570715" TEXT="$ streamlit docs"/>
<node CREATED="1665961570716" ID="ID_877425535" MODIFIED="1665961570716" TEXT="$ streamlit --version"/>
</node>
<node CREATED="1665961570717" FOLDED="true" ID="ID_935630685" MODIFIED="1665962337490" TEXT="Pre-release features">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570718" ID="ID_891315595" LINK="https://docs.streamlit.io/library/advanced-features/prerelease#beta-and-experimental-features" MODIFIED="1665961704166" TEXT="Beta and experimental features"/>
<node CREATED="1665961570719" ID="ID_845175823" MODIFIED="1665961570719" TEXT="pip uninstall streamlit"/>
<node CREATED="1665961570720" ID="ID_1597943498" MODIFIED="1665961570720" TEXT="pip install streamlit-nightly --upgrade"/>
<node CREATED="1665961570721" ID="ID_418111649" LINK="https://github.com/daniellewisDL/streamlit-cheat-sheet" MODIFIED="1665961818900" TEXT="st.cheat_sheet v1.8.0 | April 2022"/>
</node>
<node CREATED="1665961570722" ID="ID_1002141458" MODIFIED="1665962450199" TEXT="Magic commands">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570722" ID="ID_609168694" MODIFIED="1665961570722" TEXT="# Magic commands implicitly `st.write()`"/>
<node CREATED="1665961570723" ID="ID_1307379303" MODIFIED="1665961570723" TEXT="&apos;&apos;&apos; _This_ is some __Markdown__ &apos;&apos;&apos;"/>
<node CREATED="1665961570726" ID="ID_1319021197" MODIFIED="1665961570726" TEXT="a=3"/>
<node CREATED="1665961570727" ID="ID_753954262" MODIFIED="1665961570727" TEXT="&apos;dataframe:&apos;, data"/>
</node>
<node CREATED="1665961570728" FOLDED="true" ID="ID_62602756" MODIFIED="1666356874922" TEXT="Display text">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570729" ID="ID_1954629714" MODIFIED="1665961570729" TEXT="st.text(&apos;Fixed width text&apos;)"/>
<node CREATED="1665961570730" ID="ID_1966333354" MODIFIED="1665961570730" TEXT="st.markdown(&apos;_Markdown_&apos;) # see *"/>
<node CREATED="1665961570731" ID="ID_147221907" MODIFIED="1665961570731" TEXT="st.caption(&apos;Balloons. Hundreds of them...&apos;)"/>
<node CREATED="1665961570731" ID="ID_316803096" MODIFIED="1665961570731" TEXT="st.latex(r&apos;&apos;&apos; e^{i\pi} + 1 = 0 &apos;&apos;&apos;)"/>
<node CREATED="1665961570733" ID="ID_1182411431" MODIFIED="1665961570733" TEXT="st.write(&apos;Most objects&apos;) # df, err, func, keras!"/>
<node CREATED="1665961570734" ID="ID_1958958302" MODIFIED="1665961570734" TEXT="st.write([&apos;st&apos;, &apos;is &lt;&apos;, 3]) # see *"/>
<node CREATED="1665961570734" ID="ID_969209450" MODIFIED="1665961570734" TEXT="st.title(&apos;My title&apos;)"/>
<node CREATED="1665961570735" ID="ID_218632322" MODIFIED="1665961570735" TEXT="st.header(&apos;My header&apos;)"/>
<node CREATED="1665961570735" ID="ID_949242840" MODIFIED="1665961570735" TEXT="st.subheader(&apos;My sub&apos;)"/>
<node CREATED="1665961570736" ID="ID_688329246" MODIFIED="1665961570736" TEXT="st.code(&apos;for i in range(8): foo()&apos;)"/>
<node CREATED="1665961570737" ID="ID_1430732974" MODIFIED="1665961570737" TEXT="* optional kwarg unsafe_allow_html = True"/>
</node>
<node CREATED="1665961570738" FOLDED="true" ID="ID_950433994" MODIFIED="1665962337491" TEXT="Display data">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570739" ID="ID_1481686155" MODIFIED="1665961570739" TEXT="st.dataframe(my_dataframe)"/>
<node CREATED="1665961570739" ID="ID_1718996032" MODIFIED="1665961570739" TEXT="st.table(data.iloc[0:10])"/>
<node CREATED="1665961570740" ID="ID_1603886602" MODIFIED="1665961570740" TEXT="st.json({&apos;foo&apos;:&apos;bar&apos;,&apos;fu&apos;:&apos;ba&apos;})"/>
<node CREATED="1665961570741" ID="ID_1350831374" MODIFIED="1665961570741" TEXT="st.metric(label=&quot;Temp&quot;, value=&quot;273 K&quot;, delta=&quot;1.2 K&quot;)"/>
</node>
<node CREATED="1665961570742" FOLDED="true" ID="ID_700401646" MODIFIED="1665962337491" TEXT="Display charts">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570743" ID="ID_660195382" MODIFIED="1665961570743" TEXT="st.line_chart(data)"/>
<node CREATED="1665961570743" ID="ID_1406040184" MODIFIED="1665961570743" TEXT="st.area_chart(data)"/>
<node CREATED="1665961570744" ID="ID_732433846" MODIFIED="1665961570744" TEXT="st.bar_chart(data)"/>
<node CREATED="1665961570744" ID="ID_972557180" MODIFIED="1665961570744" TEXT="st.pyplot(fig)"/>
<node CREATED="1665961570745" ID="ID_1158506333" MODIFIED="1665961570745" TEXT="st.altair_chart(data)"/>
<node CREATED="1665961570746" ID="ID_1682517823" MODIFIED="1665961570746" TEXT="st.vega_lite_chart(data)"/>
<node CREATED="1665961570747" ID="ID_31737280" MODIFIED="1665961570747" TEXT="st.plotly_chart(data)"/>
<node CREATED="1665961570748" ID="ID_867671494" MODIFIED="1665961570748" TEXT="st.bokeh_chart(data)"/>
<node CREATED="1665961570749" ID="ID_1952457773" MODIFIED="1665961570749" TEXT="st.pydeck_chart(data)"/>
<node CREATED="1665961570749" ID="ID_252833175" MODIFIED="1665961570749" TEXT="st.deck_gl_chart(data)"/>
<node CREATED="1665961570750" ID="ID_1995611799" MODIFIED="1665961570750" TEXT="st.graphviz_chart(data)"/>
<node CREATED="1665961570751" ID="ID_686761684" MODIFIED="1665961570751" TEXT="st.map(data)"/>
</node>
<node CREATED="1665961570751" FOLDED="true" ID="ID_1593541213" MODIFIED="1665962337491" TEXT="Display media">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570752" ID="ID_1088240425" MODIFIED="1665961570752" TEXT="st.image(&apos;./header.png&apos;)"/>
<node CREATED="1665961570753" ID="ID_1068774055" MODIFIED="1665961570753" TEXT="st.audio(data)"/>
<node CREATED="1665961570754" ID="ID_1336971701" MODIFIED="1665961570754" TEXT="st.video(data)"/>
</node>
<node CREATED="1665961570755" FOLDED="true" ID="ID_952274343" MODIFIED="1665962337491" TEXT="Display interactive widgets">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961971217" FOLDED="true" ID="ID_1263677322" MODIFIED="1665962336539" TEXT="widgets">
<node CREATED="1665961570757" ID="ID_1496555523" MODIFIED="1665961570757" TEXT="st.button(&apos;Hit me&apos;)"/>
<node CREATED="1665961570758" ID="ID_1686237128" MODIFIED="1665961570758" TEXT="st.download_button(&apos;On the dl&apos;, data)"/>
<node CREATED="1665961570758" ID="ID_761586449" MODIFIED="1665961570758" TEXT="st.checkbox(&apos;Check me out&apos;)"/>
<node CREATED="1665961570759" ID="ID_1607095058" MODIFIED="1665961570759" TEXT="st.radio(&apos;Radio&apos;, [1,2,3])"/>
<node CREATED="1665961570760" ID="ID_869307246" MODIFIED="1665961570760" TEXT="st.selectbox(&apos;Select&apos;, [1,2,3])"/>
<node CREATED="1665961570760" ID="ID_754275524" MODIFIED="1665961570760" TEXT="st.multiselect(&apos;Multiselect&apos;, [1,2,3])"/>
<node CREATED="1665961570761" ID="ID_599273223" MODIFIED="1665961570761" TEXT="st.slider(&apos;Slide me&apos;, min_value=0, max_value=10)"/>
<node CREATED="1665961570762" ID="ID_1797447727" MODIFIED="1665961570762" TEXT="st.select_slider(&apos;Slide to select&apos;, options=[1,&apos;2&apos;])"/>
<node CREATED="1665961570764" ID="ID_1356392450" MODIFIED="1665961570764" TEXT="st.text_input(&apos;Enter some text&apos;)"/>
<node CREATED="1665961570767" ID="ID_852430749" MODIFIED="1665961570767" TEXT="st.number_input(&apos;Enter a number&apos;)"/>
<node CREATED="1665961570769" ID="ID_307642144" MODIFIED="1665961570769" TEXT="st.text_area(&apos;Area for textual entry&apos;)"/>
<node CREATED="1665961570771" ID="ID_1022275887" MODIFIED="1665961570771" TEXT="st.date_input(&apos;Date input&apos;)"/>
<node CREATED="1665961570773" ID="ID_1012714958" MODIFIED="1665961570773" TEXT="st.time_input(&apos;Time entry&apos;)"/>
<node CREATED="1665961570774" ID="ID_483417605" MODIFIED="1665961570774" TEXT="st.file_uploader(&apos;File uploader&apos;)"/>
<node CREATED="1665961570776" ID="ID_261732952" MODIFIED="1665961570776" TEXT="st.camera_input(&quot;&#x4e00;&#x4e8c;&#x4e09;,&#x8304;&#x5b50;!&quot;)"/>
<node CREATED="1665961570777" ID="ID_923586045" MODIFIED="1665961570777" TEXT="st.color_picker(&apos;Pick a color&apos;)"/>
</node>
<node CREATED="1665961570777" FOLDED="true" ID="ID_1128358418" MODIFIED="1665962336539" TEXT="Use widgets&apos; returned values in variables:">
<node CREATED="1665961570779" ID="ID_1912891703" MODIFIED="1665961570779" TEXT="&gt;&gt;&gt; for i in range(int(st.number_input(&apos;Num:&apos;))): foo()"/>
<node CREATED="1665961570780" ID="ID_52353909" MODIFIED="1665961570780" TEXT="&gt;&gt;&gt; if st.sidebar.selectbox(&apos;I:&apos;,[&apos;f&apos;]) == &apos;f&apos;: b()"/>
<node CREATED="1665961570781" ID="ID_1696941138" MODIFIED="1665961570781" TEXT="&gt;&gt;&gt; my_slider_val = st.slider(&apos;Quinn Mallory&apos;, 1, 88)"/>
<node CREATED="1665961570782" ID="ID_543376691" MODIFIED="1665961570782" TEXT="&gt;&gt;&gt; st.write(slider_val)"/>
</node>
</node>
<node CREATED="1665961570783" FOLDED="true" ID="ID_1635768538" MODIFIED="1665962337492" TEXT="Control flow">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570785" ID="ID_359731476" MODIFIED="1665961570785" TEXT="st.stop()"/>
</node>
<node CREATED="1665961570790" FOLDED="true" ID="ID_1347670547" MODIFIED="1665962337492" TEXT="Lay out your app">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665962063328" FOLDED="true" ID="ID_864138136" MODIFIED="1665962336540" TEXT="layout widgets">
<node CREATED="1665961570792" ID="ID_87887078" MODIFIED="1665961570792" TEXT="st.form(&apos;my_form_identifier&apos;)"/>
<node CREATED="1665961570793" ID="ID_1626700441" MODIFIED="1665961570793" TEXT="st.form_submit_button(&apos;Submit to me&apos;)"/>
<node CREATED="1665961570794" ID="ID_521209160" MODIFIED="1665961570794" TEXT="st.container()"/>
<node CREATED="1665961570795" ID="ID_1181862961" MODIFIED="1665961570795" TEXT="st.columns(spec)"/>
<node CREATED="1665961570796" ID="ID_497222739" MODIFIED="1665961570796" TEXT="&gt;&gt;&gt; col1, col2 = st.columns(2)"/>
<node CREATED="1665961570796" ID="ID_1573109942" MODIFIED="1665961570796" TEXT="&gt;&gt;&gt; col1.subheader(&apos;Columnisation&apos;)"/>
<node CREATED="1665961570797" ID="ID_620268725" MODIFIED="1665961570797" TEXT="st.expander(&apos;Expander&apos;)"/>
<node CREATED="1665961570798" ID="ID_56209148" MODIFIED="1665961570798" TEXT="&gt;&gt;&gt; with st.expander(&apos;Expand&apos;):"/>
<node CREATED="1665961570798" ID="ID_426933272" MODIFIED="1665961570798" TEXT="&gt;&gt;&gt;     st.write(&apos;Juicy deets&apos;)"/>
</node>
<node CREATED="1665961570799" FOLDED="true" ID="ID_372244023" MODIFIED="1665962336540" TEXT="Batch widgets together in a form:">
<node CREATED="1665961570799" ID="ID_1888240064" MODIFIED="1665961570799" TEXT="&gt;&gt;&gt; with st.form(key=&apos;my_form&apos;):"/>
<node CREATED="1665961570800" ID="ID_1981831786" MODIFIED="1665961570800" TEXT="&gt;&gt;&gt;         text_input = st.text_input(label=&apos;Enter some text&apos;)"/>
<node CREATED="1665961570801" ID="ID_1569586430" MODIFIED="1665961570801" TEXT="&gt;&gt;&gt;         submit_button = st.form_submit_button(label=&apos;Submit&apos;)"/>
</node>
</node>
<node CREATED="1665961570801" FOLDED="true" ID="ID_1341687673" MODIFIED="1665962337492" TEXT="Display code">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570802" ID="ID_603272492" MODIFIED="1665961570802" TEXT="st.echo()"/>
<node CREATED="1665961570802" ID="ID_70298945" MODIFIED="1665961570802" TEXT="&gt;&gt;&gt; with st.echo():"/>
<node CREATED="1665961570803" ID="ID_1751746792" MODIFIED="1665961570803" TEXT="&gt;&gt;&gt;     st.write(&apos;Code will be executed and printed&apos;)"/>
</node>
<node CREATED="1665961570804" FOLDED="true" ID="ID_1947931977" MODIFIED="1665962337492" TEXT="Display progress and status">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570804" ID="ID_776855795" MODIFIED="1665961570804" TEXT="&gt;&gt;&gt; with st.spinner(text=&apos;In progress&apos;):"/>
<node CREATED="1665961570805" ID="ID_183818220" MODIFIED="1665961570805" TEXT="&gt;&gt;&gt;   time.sleep(5)"/>
<node CREATED="1665961570806" ID="ID_150361628" MODIFIED="1665961570806" TEXT="&gt;&gt;&gt;   st.success(&apos;Done&apos;)"/>
<node CREATED="1665961570807" ID="ID_1612345086" MODIFIED="1665961570807" TEXT="st.progress(progress_variable_1_to_100)"/>
<node CREATED="1665961570807" ID="ID_987837250" MODIFIED="1665961570807" TEXT="st.balloons()"/>
<node CREATED="1665961570808" ID="ID_275803093" MODIFIED="1665961570808" TEXT="st.snow()"/>
<node CREATED="1665961570809" ID="ID_80505573" MODIFIED="1665961570809" TEXT="st.error(&apos;Error message&apos;)"/>
<node CREATED="1665961570809" ID="ID_1466249478" MODIFIED="1665961570809" TEXT="st.warning(&apos;Warning message&apos;)"/>
<node CREATED="1665961570810" ID="ID_64337785" MODIFIED="1665961570810" TEXT="st.info(&apos;Info message&apos;)"/>
<node CREATED="1665961570811" ID="ID_284971358" MODIFIED="1665961570811" TEXT="st.success(&apos;Success message&apos;)"/>
<node CREATED="1665961570811" ID="ID_1494249505" MODIFIED="1665961570811" TEXT="st.exception(e)"/>
</node>
<node CREATED="1665961570812" FOLDED="true" ID="ID_1829054083" MODIFIED="1665962337493" TEXT="Placeholders, help, and options">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570813" ID="ID_98882298" MODIFIED="1665961570813" TEXT="# Replace any single element."/>
<node CREATED="1665961570814" ID="ID_722214144" MODIFIED="1665961570814" TEXT="&gt;&gt;&gt; element = st.empty()"/>
<node CREATED="1665961570814" ID="ID_1551545810" MODIFIED="1665961570814" TEXT="&gt;&gt;&gt; element.line_chart(...)"/>
<node CREATED="1665961570815" ID="ID_852734545" MODIFIED="1665961570815" TEXT="&gt;&gt;&gt; element.text_input(...)  # Replaces previous."/>
<node CREATED="1665961570816" ID="ID_768528232" MODIFIED="1665961570816" TEXT="# Insert out of order."/>
<node CREATED="1665961570816" ID="ID_227405118" MODIFIED="1665961570816" TEXT="&gt;&gt;&gt; elements = st.container()"/>
<node CREATED="1665961570818" ID="ID_243407932" MODIFIED="1665961570818" TEXT="&gt;&gt;&gt; elements.line_chart(...)"/>
<node CREATED="1665961570819" ID="ID_58984471" MODIFIED="1665961570819" TEXT="&gt;&gt;&gt; st.write(&quot;Hello&quot;)"/>
<node CREATED="1665961570820" ID="ID_1565484119" MODIFIED="1665961570820" TEXT="&gt;&gt;&gt; elements.text_input(...)  # Appears above &quot;Hello&quot;."/>
<node CREATED="1665961570820" ID="ID_1733216908" MODIFIED="1665961570820" TEXT="st.help(pandas.DataFrame)"/>
<node CREATED="1665961570821" ID="ID_1083034793" MODIFIED="1665961570821" TEXT="st.get_option(key)"/>
<node CREATED="1665961570822" ID="ID_569920240" MODIFIED="1665961570822" TEXT="st.set_option(key, value)"/>
<node CREATED="1665961570823" ID="ID_1765366739" MODIFIED="1665961570823" TEXT="st.set_page_config(layout=&apos;wide&apos;)"/>
<node CREATED="1665961570823" ID="ID_996285977" MODIFIED="1665961570823" TEXT="st.experimental_show(objects)"/>
<node CREATED="1665961570824" ID="ID_1048590207" MODIFIED="1665961570824" TEXT="st.experimental_get_query_params()"/>
<node CREATED="1665961570825" ID="ID_771347563" MODIFIED="1665961570825" TEXT="st.experimental_set_query_params(**params)"/>
</node>
<node CREATED="1665961570825" FOLDED="true" ID="ID_643000213" MODIFIED="1665962337493" TEXT="Mutate data">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570826" ID="ID_1826915434" MODIFIED="1665961570826" TEXT="# Add rows to a dataframe after"/>
<node CREATED="1665961570827" ID="ID_328594682" MODIFIED="1665961570827" TEXT="# showing it."/>
<node CREATED="1665961570827" ID="ID_1130326238" MODIFIED="1665961570827" TEXT="&gt;&gt;&gt; element = st.dataframe(df1)"/>
<node CREATED="1665961570828" ID="ID_1184713084" MODIFIED="1665961570828" TEXT="&gt;&gt;&gt; element.add_rows(df2)"/>
<node CREATED="1665961570829" ID="ID_1099163542" MODIFIED="1665961570829" TEXT="# Add rows to a chart after"/>
<node CREATED="1665961570829" ID="ID_1049905844" MODIFIED="1665961570829" TEXT="# showing it."/>
<node CREATED="1665961570830" ID="ID_800439343" MODIFIED="1665961570830" TEXT="&gt;&gt;&gt; element = st.line_chart(df1)"/>
<node CREATED="1665961570831" ID="ID_1958675493" MODIFIED="1665961570831" TEXT="&gt;&gt;&gt; element.add_rows(df2)"/>
</node>
<node CREATED="1665961570832" FOLDED="true" ID="ID_198433340" MODIFIED="1665962337493" TEXT="Optimize performance">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570832" FOLDED="true" ID="ID_1002432834" MODIFIED="1665962336540" TEXT="Legacy caching">
<node CREATED="1665961570833" ID="ID_190559604" MODIFIED="1665961570833" TEXT="&gt;&gt;&gt; @st.cache"/>
<node CREATED="1665961570834" ID="ID_1850476291" MODIFIED="1665961570834" TEXT="... def foo(bar):"/>
<node CREATED="1665961570834" ID="ID_18961231" MODIFIED="1665961570834" TEXT="...   # Do something expensive in here..."/>
<node CREATED="1665961570835" ID="ID_1176672429" MODIFIED="1665961570835" TEXT="...   return data"/>
<node CREATED="1665961570836" ID="ID_60612026" MODIFIED="1665961570836" TEXT="&gt;&gt;&gt; # Executes foo"/>
<node CREATED="1665961570837" ID="ID_626681350" MODIFIED="1665961570837" TEXT="&gt;&gt;&gt; d1 = foo(ref1)"/>
<node CREATED="1665961570837" ID="ID_1740950162" MODIFIED="1665961570837" TEXT="&gt;&gt;&gt; # Does not execute foo"/>
<node CREATED="1665961570838" ID="ID_410436204" MODIFIED="1665961570838" TEXT="&gt;&gt;&gt; # Returns cached item by reference, d1 == d2"/>
<node CREATED="1665961570839" ID="ID_1527821484" MODIFIED="1665961570839" TEXT="&gt;&gt;&gt; d2 = foo(ref1)"/>
<node CREATED="1665961570839" ID="ID_394453185" MODIFIED="1665961570839" TEXT="&gt;&gt;&gt; # Different arg, so function foo executes"/>
<node CREATED="1665961570840" ID="ID_793575802" MODIFIED="1665961570840" TEXT="&gt;&gt;&gt; d3 = foo(ref2)"/>
</node>
<node CREATED="1665961570841" FOLDED="true" ID="ID_1064535769" MODIFIED="1665962336541" TEXT="Cache data objects">
<node CREATED="1665961570842" ID="ID_1489105469" MODIFIED="1665961570842" TEXT="&gt;&gt;&gt; @st.experimental_memo"/>
<node CREATED="1665961570842" ID="ID_12204081" MODIFIED="1665961570842" TEXT="... def foo(bar):"/>
<node CREATED="1665961570843" ID="ID_416897644" MODIFIED="1665961570843" TEXT="...   # Do something expensive and return data"/>
<node CREATED="1665961570844" ID="ID_1845351257" MODIFIED="1665961570844" TEXT="...   return data"/>
<node CREATED="1665961570844" ID="ID_1433432247" MODIFIED="1665961570844" TEXT="# Executes foo"/>
<node CREATED="1665961570845" ID="ID_1580079754" MODIFIED="1665961570845" TEXT="&gt;&gt;&gt; d1 = foo(ref1)"/>
<node CREATED="1665961570846" ID="ID_7080407" MODIFIED="1665961570846" TEXT="# Does not execute foo"/>
<node CREATED="1665961570846" ID="ID_990509532" MODIFIED="1665961570846" TEXT="# Returns cached item by value, d1 == d2"/>
<node CREATED="1665961570847" ID="ID_1007649315" MODIFIED="1665961570847" TEXT="&gt;&gt;&gt; d2 = foo(ref1)"/>
<node CREATED="1665961570847" ID="ID_316837019" MODIFIED="1665961570847" TEXT="# Different arg, so function foo executes"/>
<node CREATED="1665961570849" ID="ID_797796950" MODIFIED="1665961570849" TEXT="&gt;&gt;&gt; d3 = foo(ref2)"/>
<node CREATED="1665961570850" ID="ID_415186457" MODIFIED="1665961570850" TEXT="# Clear all cached entries for this function"/>
<node CREATED="1665961570851" ID="ID_390716936" MODIFIED="1665961570851" TEXT="&gt;&gt;&gt; foo.clear()"/>
<node CREATED="1665961570851" ID="ID_762475720" MODIFIED="1665961570851" TEXT="# Clear values from *all* memoized functions"/>
<node CREATED="1665961570852" ID="ID_1658868926" MODIFIED="1665961570852" TEXT="&gt;&gt;&gt; st.experimental_memo.clear()"/>
</node>
<node CREATED="1665961570853" FOLDED="true" ID="ID_1103655230" MODIFIED="1665962336541" TEXT="Cache non-data objects">
<node CREATED="1665961570853" ID="ID_171105377" MODIFIED="1665961570853" TEXT="# E.g. TensorFlow session, database connection, etc."/>
<node CREATED="1665961570854" ID="ID_850775609" MODIFIED="1665961570854" TEXT="&gt;&gt;&gt; @st.experimental_singleton"/>
<node CREATED="1665961570854" ID="ID_32304912" MODIFIED="1665961570854" TEXT="... def foo(bar):"/>
<node CREATED="1665961570855" ID="ID_1058525082" MODIFIED="1665961570855" TEXT="...   # Create and return a non-data object"/>
<node CREATED="1665961570856" ID="ID_591011245" MODIFIED="1665961570856" TEXT="...   return session"/>
<node CREATED="1665961570856" ID="ID_1885753158" MODIFIED="1665961570856" TEXT="# Executes foo"/>
<node CREATED="1665961570857" ID="ID_236667371" MODIFIED="1665961570857" TEXT="&gt;&gt;&gt; s1 = foo(ref1)"/>
<node CREATED="1665961570857" ID="ID_582566808" MODIFIED="1665961570857" TEXT="# Does not execute foo"/>
<node CREATED="1665961570858" ID="ID_1626169533" MODIFIED="1665961570858" TEXT="# Returns cached item by reference, d1 == d2"/>
<node CREATED="1665961570858" ID="ID_628920857" MODIFIED="1665961570858" TEXT="&gt;&gt;&gt; s2 = foo(ref1)"/>
<node CREATED="1665961570859" ID="ID_490005308" MODIFIED="1665961570859" TEXT="# Different arg, so function foo executes"/>
<node CREATED="1665961570859" ID="ID_1769968395" MODIFIED="1665961570859" TEXT="&gt;&gt;&gt; s3 = foo(ref2)"/>
<node CREATED="1665961570860" ID="ID_889558181" MODIFIED="1665961570860" TEXT="# Clear all cached entries for this function"/>
<node CREATED="1665961570860" ID="ID_943932253" MODIFIED="1665961570860" TEXT="&gt;&gt;&gt; foo.clear()"/>
<node CREATED="1665961570861" ID="ID_1544427572" MODIFIED="1665961570861" TEXT="# Clear all singleton caches"/>
<node CREATED="1665961570861" ID="ID_418192982" MODIFIED="1665961570861" TEXT="&gt;&gt;&gt; st.experimental_singleton.clear()"/>
</node>
</node>
<node CREATED="1665961570862" FOLDED="true" ID="ID_816933444" MODIFIED="1665962337493" TEXT="Other key parts of the API">
<font BOLD="true" NAME="DejaVu Sans Mono" SIZE="12"/>
<node CREATED="1665961570862" ID="ID_810693768" MODIFIED="1665961570862" TEXT="State API"/>
<node CREATED="1665961570863" ID="ID_241947517" MODIFIED="1665961570863" TEXT="Theme option reference"/>
<node CREATED="1665961570863" ID="ID_98022248" MODIFIED="1665961570863" TEXT="Components API reference"/>
<node CREATED="1665961570864" ID="ID_206152244" MODIFIED="1665961570864" TEXT="API cheat sheet"/>
</node>
</node>
</node>
</map>
