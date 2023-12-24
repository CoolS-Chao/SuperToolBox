#include "ToolBox.h"
#include "ui_ToolBox.h"
#include <QResource>
#include <QSettings>
#include <QMessageBox>
#include <QHostAddress>
#include <QDebug>

ToolBox::ToolBox(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::ToolBox)
{
    ui->setupUi(this);

    loadConfig();
    connect(&m_tcpSocket, SIGNAL(connected()), this, SLOT(connectSuccess()));   //第一个参数传递对象指针
    m_tcpSocket.connectToHost(QHostAddress(m_serverIp), m_serverPort);
}

ToolBox::~ToolBox()
{
    delete ui;
}

void ToolBox::loadConfig()
{
    // 加载嵌入的资源文件
    QResource::registerResource("config.qrc");
    QSettings configFile(":/db.ini", QSettings::IniFormat);   // QFile configFile(":/db.ini");
    m_serverIp = configFile.value("serviceData/ip").toString();
    m_serverPort = configFile.value("serviceData/port").toUInt();
    qDebug() << m_serverIp;
    qDebug() << m_serverPort;
}

void ToolBox::connectSuccess()
{
    QMessageBox::information(this, "Connect Status", "Successful");
    // QMessageBox messageBox(QMessageBox::Information, "Connect Status", "Successful", QMessageBox::Ok, this);
}

//void ToolBox::connectFailed()
//{
//    QMessageBox::information("222");
//}

