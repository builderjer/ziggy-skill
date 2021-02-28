import QtQuick.Layouts 1.4
import QtQuick 2.4
import QtQuick.Controls 2.0
import org.kde.kirigami 2.4 as Kirigami

import Mycroft 1.0 as Mycroft

Mycroft.Delegate {

    FontLoader { id: ziggyfont; source: "fonts/Ziggy.ttf" }

    background: Image {
        source: Qt.resolvedUrl("img/idle.png")
        anchors.fill: parent
        fillMode: Image.PreserveAspectCrop
    }
    Label {
        id: title
        Layout.alignment: Qt.AlignCenter
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        font.family: ziggyfont.name
        font.pixelSize: 200
        color: "#00e6e6"
        text: sessionData.title
    }
    // ColumnLayout {
    //
    //     id: grid
    //     Layout.fillWidth: true
    //     anchors.centerIn: parent
    //     spacing: 0
    //
    //
    //     Item {
    //         height: Kirigami.Units.largeSpacing * 6
    //     }
    //     Label {
    //         id: time
    //         Layout.alignment: Qt.AlignCenter
    //         font.capitalization: Font.AllUppercase
    //         font.family: ziggyfont.name
    //         font.pixelSize: 140
    //         color: "#00e6e6"
    //         lineHeight: 0.6
    //         text: sessionData.time_string.replace(":", "꞉")
    //     }
    //     Item {
    //         height: Kirigami.Units.largeSpacing * 5
    //     }
    //     Label {
    //         id: weekday
    //         Layout.alignment: Qt.AlignCenter
    //         font.pixelSize: 50
    //         wrapMode: Text.WordWrap
    //         font.family: ziggyfont.name
    //         lineHeight: 0.6
    //         text: sessionData.weekday_string
    //         color: "#00e6e6"
    //     }
    //     Item {
    //         height: Kirigami.Units.largeSpacing * 3
    //     }
    //     Label {
    //         id: date
    //         Layout.alignment: Qt.AlignCenter
    //         font.pixelSize: 50
    //         wrapMode: Text.WordWrap
    //         font.family: ziggyfont.name
    //         lineHeight: 0.6
    //         text: sessionData.month_string
    //         color: "#00e6e6"
    //     }
    //     Item {
    //         height: Kirigami.Units.largeSpacing * 1
    //     }
    // }
}
