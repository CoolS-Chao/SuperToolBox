#ifndef DBVIEWER_H
#define DBVIEWER_H

#include <QMainWindow>
#include <QSqlDatabase>
#include <QSqlQueryModel>
#include <QSqlQuery>
#include <QTableView>
#include <QVBoxLayout>
#include <QPushButton>
#include <QLabel>
#include <QLineEdit>


class SQLiteViewer : public QMainWindow {
    Q_OBJECT

public:
    SQLiteViewer(QWidget *parent = nullptr);

public slots:
    void refreshData();
    void executeQuery();

private:
    QSqlDatabase db;
    QSqlQueryModel *model;
    QTableView *table_view;
    QLineEdit *query_input;
};

#endif // DBVIEWER_H
