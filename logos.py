#/usr/bin/python
"""
Copyright (C) 2021  Piotr Lange

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 3.

Logos is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import sys, os
from PyQt5.QtGui import *
from PyQt5.Qt import PYQT_VERSION_STR
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QFile, QTextStream
from PyQt5.Qsci import *
from datetime import datetime

version = "0.3.4"

global filenamen
filenamen = ""

h_sit = True

def About_p(win):
	global version
	dial = QDialog(win)
	dial.setObjectName("aboutwidget")
	dial.setContentsMargins(0, 0, 0, 0)
	dial.setWindowFlags(Qt.Window | Qt.Dialog | Qt.WindowCloseButtonHint)
	dial.setWindowModality(Qt.ApplicationModal)
	logolabel = QLabel(dial)
	logolabel.setPixmap(QPixmap("icons/about-bar.png"))
	versionlabel = QLabel("""
			<style>
				b.label {{
					font-family: "Noto Sans", sans-serif;
					font-size: 14px;
					font-weight: 500;
					color: {0};
				}}
				b.version {{
					font-family: "Futura LT", sans-serif;
					font-size: 16px;
					font-weight: 600;
				}}
			</style>
			<b class="label">version:</b>&nbsp; <b class="version">"""+version+"""</b>""".format("#EA95FF", qApp.applicationVersion(), dial))
	versionspacing = 95
	versionlabel.setAlignment(Qt.AlignBottom)
	versionlayout = QHBoxLayout()
	versionlayout.setSpacing(0)
	versionlayout.setContentsMargins(0, 0, 0, 0)
	versionlayout.addStretch(1)
	versionlayout.addWidget(versionlabel)
	versionlayout.addSpacing(versionspacing)
	headerlayout = QVBoxLayout()
	headerlayout.setSpacing(0)
	headerlayout.setContentsMargins(0, 0, 0, 0)
	headerlayout.addWidget(logolabel, 1)
	headerlayout.addLayout(versionlayout)
##################################################
	tab_about = QLabel(dial)
	tab_about.setTextFormat(Qt.RichText)
	tab_about.setWordWrap(True)
	tab_about.setAlignment(Qt.AlignLeft | Qt.AlignTop)
	tab_about.setOpenExternalLinks(True)
	bgcolor = "rgba(12, 15, 16, 210)"
	pencolor = "#FFF"
	tab_about.setStyleSheet("""
			QLabel {{
				background-color: {bgcolor};
				color: {pencolor};
				padding: 8px;
			}}""".format(**locals()))
	pencolor = "#FAFAFA"
	linkcolor = "#FDA502"
	python_version = sys.version.split(" ")[0]
	pyqt_version = PYQT_VERSION_STR
	year = datetime.now().year
	tab_about.setText("""
<style>
	table {{ width:100%; font-family:"Noto Sans", sans-serif; background-color:transparent; }}
	td.label {{ font-size:13px; font-weight:bold; text-align:right; }}
	td.value {{
		color: {pencolor};
		font-weight: 600;
		font-family: "Futura LT", sans-serif;
		font-size: 12.5px;
		vertical-align: bottom;
	}}
	a {{ color: {linkcolor}; text-decoration:none; font-weight:bold; }}
</style>
<table border="0" cellpadding="0" cellspacing="4">
	<tr>
		<td>
			<table border="0" cellpadding="0" cellspacing="0">
				<tr valign="top">
					<td>
						<table border="0" cellpadding="0" cellspacing="0">
							<td nowrap style="font-weight:500;font-size:13px;">
								<p>
									<a href="https://qt.io" title="Qt5"><img src="icons/Qt.png" /></a>
									<br/><br/>
									<a href="https://python.org" title="Python"><img src="icons/python.png" /></a>
								</p>
							</td>
							<td align="left" nowrap style="font-weight:500;font-size:13px;">
								<p class="label">PyQt:<br/>{pyqt_version}</p>
								<p class="label">Python:<br/>{python_version}</p>
							</td>
						</td>
						<p style="font-size:13px;">
							Copyright © 2020 - {year} <a href="https://github.com/PiotrZPL">Piotr Lange</a>
							<br/>
							Source code: <a href="https://github.com/PiotrZPL/Logos">https://github.com/PiotrZPL/Logos</a>
						</p>
						<p style="font-size:13px;">
							If you encounter any bugs, report them <a href="https://github.com/PiotrZPL/Logos/issues">here</a>.
						</p>
					<td nowrap style="font-weight:500;font-size:13px;">
						<img src="icons/lambda.png"
						width="154"/>
					</td>
				</tr>
			</table>
			<p style="font-size:12px; margin-top:15px;">
				This program is free software: you can redistribute it and/or modify
				it under the terms of the GNU General Public License as published by
				the Free Software Foundation; version 3.<br/><br/>
				Logos is distributed in the hope that it will be useful,
				but WITHOUT ANY WARRANTY; without even the implied warranty of
				MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
				GNU General Public License for more details.<br/><br/>
				You should have received a copy of the GNU General Public License
				along with this program.  If not, see http://www.gnu.org/licenses.
			</p>
		</td>
	</tr>
</table>""".format(**locals()))
##################################################
	tab_credits = QLabel(dial)
	tab_credits.setTextFormat(Qt.RichText)
	tab_credits.setWordWrap(True)
	tab_credits.setAlignment(Qt.AlignLeft | Qt.AlignTop)
	tab_credits.setOpenExternalLinks(True)
	bgcolor = "rgba(12, 15, 16, 210)"
	pencolor = "#FFF"
	linkcolor = "#FDA502"
	tab_credits.setStyleSheet("""
			QLabel {{
				background-color: {bgcolor};
				color: {pencolor};
				padding: 8px;
			}}""".format(**locals()))
	tab_credits.setObjectName("credits")
	tab_credits.setText("""
		<style>
			table { background-color: transparent; }
			a { color:%s; text-decoration:none; font-weight:bold; }
		</style>
		<h2 style="text-align:center;">CREDITS</h2>
		<p style="font-size:15px;">Logos would not look like this without help and/or assistance of those people:</p>
		<p style="font-size:15px;"><a href="https://buz.info.pl">Konrad Buzak</a><br/>
		<b>Igor Sobociński</b><br/>
		<p style="font-size:15px;">Logos uses modified and/or unmodified parts of code and other resources from the following sources:</p>
		<p style="font-size:15px;"><a href="https://github.com/PapirusDevelopmentTeam/papirus-icon-theme">Papirus Icon Theme</a> under <a href="https://www.gnu.org/licenses/gpl-3.0.html">the GNU GPL v3.0</a><br/>
		<a href="https://riverbankcomputing.com/software/qscintilla/intro">QScintilla</a> under <a href="https://www.gnu.org/licenses/gpl-3.0.html">the GNU GPL v3.0</a><br/>
		<a href="https://github.com/ozmartian/vidcutter">VidCutter</a> under <a href="https://www.gnu.org/licenses/gpl-3.0.html">the GNU GPL v3.0</a><br/>
		<a href="https://www.riverbankcomputing.com/software/pyqt">PyQt5</a> under <a href="https://www.gnu.org/licenses/gpl-3.0.html">the GNU GPL v3.0</a></p>""" % ("#FFF"))
##################################################
	tab_license = QLabel(dial)
	tab_license.setTextFormat(Qt.RichText)
	tab_license.setWordWrap(True)
	tab_license.setAlignment(Qt.AlignLeft | Qt.AlignTop)
	tab_license.setOpenExternalLinks(True)
	bgcolor = "rgba(12, 15, 16, 210)"
	pencolor = "#FFF"
	tab_license.setStyleSheet("""
			QLabel {{
				background-color: {bgcolor};
				color: {pencolor};
				padding: 8px;
			}}""".format(**locals()))
	tab_license.setObjectName("license")
	licensefile = QFile("license.html")
	licensefile.open(QFile.ReadOnly | QFile.Text)
	content = QTextStream(licensefile).readAll()
	tab_license.setText(content)
##################################################
	scrollarea = QScrollArea(dial)
	scrollarea.setStyleSheet("QScrollArea { background:transparent; }")
	scrollarea.setWidgetResizable(True)
	scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
	scrollarea.setFrameShape(QScrollArea.NoFrame)
	scrollarea.setWidget(tab_license)
	tabs = QTabWidget()
	tabs.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
	tabs.addTab(tab_about, "About")
	tabs.addTab(tab_credits, "Credits")
	tabs.addTab(scrollarea, "License")
	buttons = QDialogButtonBox(QDialogButtonBox.Ok)
	buttons.accepted.connect(dial.close)
	layout = QVBoxLayout()
	layout.addLayout(headerlayout)
	layout.addWidget(tabs, 1)
	layout.addWidget(buttons)
	dial.setLayout(layout)
	dial.setWindowTitle("About Logos")
	dial.show()

def Open_f(tb, win, lexer):
	global filenamen
	global h_sit
	options = QFileDialog.Options()
	options |= QFileDialog.DontUseNativeDialog
	path = QFileDialog.getOpenFileName(win, "Open a file", "", "Text files (*.txt);;Python Files (*.py);;HTML Files (*.html);;C++ Files (*.cpp);;All Files (*)", options=options)
	if not path == ("", ""):
		filename = str(path[0])
		filenamen = filename
		f = open(filename, "r")
		filedata = f.read()
		tb.setText(filedata)
		if filename.endswith(".py"):
			h_sit = False
			Code_hl(lexer)
		f.close()

def SaveAs_f(tb, win):
	global filenamen
	options = QFileDialog.Options()
	options |= QFileDialog.DontUseNativeDialog
	path = QFileDialog.getSaveFileName(win, "Save a file", "", "Text files (*.txt);;Python Files (*.py);;HTML Files (*.html);;C++ Files (*.cpp);;All Files (*)", options=options)
	if not path == ("", ""):
		filename = str(path[0])
		filenamen = filename
		f = open(filename, "w")
		filedata = tb.text()
		f.write(filedata)
		f.close()

def Save_f(tb, win):
	global filenamen
	if filenamen:
		f = open(filenamen, "w")
		filedata = tb.text()
		f.write(filedata)
		f.close()
	else:
		SaveAs_f(tb, win)
	 
def cpc(tb, sb):
	global aaas
	line, col = tb.getCursorPosition()
	linecol = ("Line: "+str(line+1)+", "+"Column: "+str(col))
	try:
		sb.removeWidget(aaas)
	except:
		pass		
	aaas = QLabel(linecol)
	sb.addPermanentWidget(aaas)
	#print("a")

def Code_hl(lexer):
	global h_sit
	h_sit = not h_sit
	if h_sit:
		lexer.setColor(QColor("cyan"), QsciLexerPython.ClassName)
		lexer.setFont(QFont("Source Code Pro", 15, QFont.Bold), QsciLexerPython.ClassName)
		lexer.setColor(QColor("darkGreen"), QsciLexerPython.Comment)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Comment)
		lexer.setColor(QColor("darkGreen"), QsciLexerPython.CommentBlock)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.CommentBlock)
		lexer.setColor(QColor("white"), QsciLexerPython.Decorator)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Decorator)
		lexer.setColor(QColor("white"), QsciLexerPython.Default)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Default)
		lexer.setColor(QColor("magenta"), QsciLexerPython.DoubleQuotedString)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.DoubleQuotedString)
		lexer.setColor(QColor("cyan"), QsciLexerPython.FunctionMethodName)
		lexer.setFont(QFont("Source Code Pro", 15, QFont.Bold), QsciLexerPython.FunctionMethodName)
		lexer.setColor(QColor("white"), QsciLexerPython.HighlightedIdentifier)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.HighlightedIdentifier)
		lexer.setColor(QColor("white"), QsciLexerPython.Identifier)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Identifier)
		lexer.setColor(QColor("darkGreen"), QsciLexerPython.Inconsistent) #Comments
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Inconsistent)
		lexer.setColor(QColor("blue"), QsciLexerPython.Keyword)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Keyword)
		lexer.setColor(QColor("white"), QsciLexerPython.NoWarning)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.NoWarning)
		lexer.setColor(QColor("red"), QsciLexerPython.Number)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Number)
		lexer.setColor(QColor("red"), QsciLexerPython.Operator)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Operator)
		lexer.setColor(QColor("magenta"), QsciLexerPython.SingleQuotedString)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.SingleQuotedString)
		lexer.setColor(QColor("yellow"), QsciLexerPython.Spaces) #Strings
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Spaces)
		lexer.setColor(QColor("white"), QsciLexerPython.Tabs)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Tabs)
		lexer.setColor(QColor("blue"), QsciLexerPython.TabsAfterSpaces) #Numbers
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.TabsAfterSpaces)
		lexer.setColor(QColor("yellow"), QsciLexerPython.TripleDoubleQuotedString) #A
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.TripleDoubleQuotedString)
		lexer.setColor(QColor("yellow"), QsciLexerPython.TripleSingleQuotedString) #A
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.TripleSingleQuotedString)
		lexer.setColor(QColor("megenta"), QsciLexerPython.UnclosedString)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.UnclosedString)
	else:
		lexer.setColor(QColor("white"), QsciLexerPython.ClassName)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.ClassName)
		lexer.setColor(QColor("white"), QsciLexerPython.Comment)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Comment)
		lexer.setColor(QColor("white"), QsciLexerPython.CommentBlock)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.CommentBlock)
		lexer.setColor(QColor("white"), QsciLexerPython.Decorator)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Decorator)
		lexer.setColor(QColor("white"), QsciLexerPython.Default)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Default)
		lexer.setColor(QColor("white"), QsciLexerPython.DoubleQuotedString)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.DoubleQuotedString)
		lexer.setColor(QColor("white"), QsciLexerPython.FunctionMethodName)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.FunctionMethodName)
		lexer.setColor(QColor("white"), QsciLexerPython.HighlightedIdentifier)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.HighlightedIdentifier)
		lexer.setColor(QColor("white"), QsciLexerPython.Identifier)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Identifier)
		lexer.setColor(QColor("white"), QsciLexerPython.Inconsistent) #Comments
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Inconsistent)
		lexer.setColor(QColor("white"), QsciLexerPython.Keyword)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Keyword)
		lexer.setColor(QColor("white"), QsciLexerPython.NoWarning)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.NoWarning)
		lexer.setColor(QColor("white"), QsciLexerPython.Number)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Number)
		lexer.setColor(QColor("white"), QsciLexerPython.Operator)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Operator)
		lexer.setColor(QColor("white"), QsciLexerPython.SingleQuotedString)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.SingleQuotedString)
		lexer.setColor(QColor("white"), QsciLexerPython.Spaces) #Strings
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Spaces)
		lexer.setColor(QColor("white"), QsciLexerPython.Tabs)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.Tabs)
		lexer.setColor(QColor("white"), QsciLexerPython.TabsAfterSpaces) #Numbers
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.TabsAfterSpaces)
		lexer.setColor(QColor("white"), QsciLexerPython.TripleDoubleQuotedString) #A
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.TripleDoubleQuotedString)
		lexer.setColor(QColor("white"), QsciLexerPython.TripleSingleQuotedString) #A
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.TripleSingleQuotedString)
		lexer.setColor(QColor("white"), QsciLexerPython.UnclosedString)
		lexer.setFont(QFont("Source Code Pro", 15), QsciLexerPython.UnclosedString)
	
def main():
	app = QApplication(sys.argv)
	app.setStyle("Fusion")
	palette = QPalette()
	palette.setColor(QPalette.Window, QColor(53, 53, 53))
	palette.setColor(QPalette.WindowText, Qt.white)
	palette.setColor(QPalette.Base, QColor(25, 25, 25))
	palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
	palette.setColor(QPalette.ToolTipBase, Qt.black)
	palette.setColor(QPalette.ToolTipText, Qt.white)
	palette.setColor(QPalette.Text, Qt.white)
	palette.setColor(QPalette.Button, QColor(53, 53, 53))
	palette.setColor(QPalette.ButtonText, Qt.white)
	palette.setColor(QPalette.BrightText, Qt.red)
	palette.setColor(QPalette.Link, QColor(42, 130, 218))
	palette.setColor(QPalette.Highlight, QColor("orange"))
	palette.setColor(QPalette.HighlightedText, Qt.black)
	app.setPalette(palette)
	window = QMainWindow()
	#text_box = QTextEdit(window)

	text_box = QsciScintilla()
	#text_box.setTabStopWidth(24)
	text_box.setTabWidth(4)
	text_box.setLexer(None)
	text_box.setMarginsForegroundColor(QColor("orange"))
	text_box.setMargins(0)
	#text_box.ensureCursorVisible()
	text_box.setCaretForegroundColor(QColor("white"))
	text_box.setUtf8(True)  # Set encoding to UTF-8
	text_box.setFont(QFont("Source Code Pro", 15, QFont.Bold))  # Will be overridden by lexer!
	lexer = QsciLexerPython(text_box)
	Code_hl(lexer)
	text_box.setLexer(lexer)

	window.setCentralWidget(text_box)
	
	A_new = QAction(QIcon("icons/document-new.svg"), "New file", window)
	A_new.setShortcut("Ctrl+N")
	A_new.setStatusTip("New file")
	A_new.triggered.connect(lambda:text_box.clear())

	A_open = QAction(QIcon("icons/document-open.svg"), "Open a file", window)
	A_open.setStatusTip("Open a file")
	A_open.setShortcut("Ctrl+O")
	A_open.triggered.connect(lambda:Open_f(text_box, window, lexer))

	A_save = QAction(QIcon("icons/document-save.svg"), "Save", window)
	A_save.setStatusTip("Save")
	A_save.setShortcut("Ctrl+S")
	A_save.triggered.connect(lambda:Save_f(text_box, window))

	A_saveas = QAction(QIcon("icons/document-save-as.svg"), "Save as", window)
	A_saveas.setStatusTip("Save as")
	A_saveas.setShortcut("Shift+Ctrl+S")
	A_saveas.triggered.connect(lambda:SaveAs_f(text_box, window))

	A_cut = QAction(QIcon("icons/edit-cut.svg"), "Cut selected text", window)
	A_cut.setStatusTip("Cut selected text")
	A_cut.setShortcut("Ctrl+X")
	A_cut.triggered.connect(lambda:text_box.cut())

	A_copy = QAction(QIcon("icons/edit-copy.svg"), "Copy selected text", window)
	A_copy.setStatusTip("Copy selected text")
	A_copy.setShortcut("Ctrl+C")
	A_copy.triggered.connect(lambda:text_box.copy())

	A_paste = QAction(QIcon("icons/edit-paste.svg"), "Paste from clipboard", window)
	A_paste.setStatusTip("Paste from clipboard")
	A_paste.setShortcut("Ctrl+V")
	A_paste.triggered.connect(lambda:text_box.paste())

	A_undo = QAction(QIcon("icons/edit-undo.svg"), "Undo", window)
	A_undo.setStatusTip("Undo")
	A_undo.setShortcut("Ctrl+Z")
	A_undo.triggered.connect(lambda:text_box.undo())

	A_redo = QAction(QIcon("icons/edit-redo.svg"), "Redo", window)
	A_redo.setStatusTip("Redo")
	A_redo.setShortcut("Ctrl+Y")
	A_redo.triggered.connect(lambda:text_box.redo())

	A_about = QAction(QIcon("icons/help-about.svg"), "About Logos", window)
	A_about.setStatusTip("About Logos")
	A_about.triggered.connect(lambda:About_p(window))

	A_highlight = QAction(QIcon("icons/tool-highlight.svg"), "Switch on/off code highlighting", window)
	A_highlight.setStatusTip("Switch on/off code highlighting")
	A_highlight.setShortcut("Ctrl+R")
	A_highlight.triggered.connect(lambda:Code_hl(lexer))
	
	toolbar_m = window.addToolBar("Options")
	toolbar_m.setMovable(False)
	toolbar_m.addAction(A_new)
	toolbar_m.addAction(A_open)
	toolbar_m.addAction(A_save)
	toolbar_m.addAction(A_saveas)
	toolbar_m.addAction(A_cut)
	toolbar_m.addAction(A_copy)
	toolbar_m.addAction(A_paste)
	toolbar_m.addAction(A_undo)
	toolbar_m.addAction(A_redo)
	toolbar_m.addAction(A_highlight)
	
	statusbrr = window.statusBar()

	text_box.cursorPositionChanged.connect(lambda:cpc(text_box, statusbrr))

	window.setWindowTitle("Logos")
	window.setWindowIcon(QIcon("icons/lambda.png"))
	 
	menubar = window.menuBar()
	file_menu = menubar.addMenu("File")
	edit_menu = menubar.addMenu("Edit")
	code_menu = menubar.addMenu("Code")
	help_menu = menubar.addMenu("Help")

	file_menu.addAction(A_new)
	file_menu.addAction(A_open)
	file_menu.addAction(A_save)
	file_menu.addAction(A_saveas)

	edit_menu.addAction(A_undo)
	edit_menu.addAction(A_redo)
	edit_menu.addAction(A_cut)
	edit_menu.addAction(A_copy)

	code_menu.addAction(A_highlight)

	help_menu.addAction(A_about)
	
	window.showMaximized()
 
	sys.exit(app.exec_())

main()
