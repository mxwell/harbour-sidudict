/***************************************************************************

    DictDownload.qml - Sidudict, a StarDict clone based on QStarDict
    Copyright 2014 Reto Zingg <g.d0b3rm4n@gmail.com>

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the Free Software           *
 *   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,            *
 *   MA 02110-1301, USA.                                                   *
 *                                                                         *
 ***************************************************************************/

import QtQuick 2.0
import Sailfish.Silica 1.0
import QtQuick.XmlListModel 2.0

Page {
    XmlListModel {
        id: xmlModel
        source: "https://raw.github.com/d0b3rm4n/harbour-sidudict/master/data/dictionaries/dictionaries.xml"
        query: "/dictionaries/dictionary"

        XmlRole { name: "id"; query: "id/string()" }
        XmlRole { name: "name"; query: "name/string()" }
        XmlRole { name: "url"; query: "url/string()" }
        XmlRole { name: "entries"; query: "entries/string()" }
        XmlRole { name: "size"; query: "size/string()" }
        XmlRole { name: "date"; query: "date/string()" }
        XmlRole { name: "description"; query: "description/string()" }
    }
    SilicaListView {
        id: listView
        model: xmlModel
        anchors.fill: parent
        header: PageHeader {
            title: "Download"
        }
        delegate: DictDelegate{}
        VerticalScrollDecorator {}
    }
}