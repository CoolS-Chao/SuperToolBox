#include "DBViewer.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    SQLiteViewer w;
    w.show();
    return a.exec();
}
