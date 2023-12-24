#ifndef TOOLBOX_H
#define TOOLBOX_H

#include <QWidget>
#include <QTcpSocket>

QT_BEGIN_NAMESPACE
namespace Ui { class ToolBox; }
QT_END_NAMESPACE

class ToolBox : public QWidget
{
    Q_OBJECT

public:
    ToolBox(QWidget *parent = nullptr);
    ~ToolBox();

    void loadConfig();

public slots:
    void connectSuccess();
//    void connectFailed();

private:
    Ui::ToolBox *ui;

    QString m_serverIp;
    quint16 m_serverPort;
    QTcpSocket m_tcpSocket;

};
#endif // TOOLBOX_H
