/********************************************************************************
** Form generated from reading UI file 'ToolBox.ui'
**
** Created by: Qt User Interface Compiler version 5.12.12
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TOOLBOX_H
#define UI_TOOLBOX_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_ToolBox
{
public:

    void setupUi(QWidget *ToolBox)
    {
        if (ToolBox->objectName().isEmpty())
            ToolBox->setObjectName(QString::fromUtf8("ToolBox"));
        ToolBox->resize(800, 600);

        retranslateUi(ToolBox);

        QMetaObject::connectSlotsByName(ToolBox);
    } // setupUi

    void retranslateUi(QWidget *ToolBox)
    {
        ToolBox->setWindowTitle(QApplication::translate("ToolBox", "ToolBox", nullptr));
    } // retranslateUi

};

namespace Ui {
    class ToolBox: public Ui_ToolBox {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TOOLBOX_H
