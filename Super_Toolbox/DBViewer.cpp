#include "DBViewer.h"
#include <QDebug>
#include <QFileInfo>
#include <QApplication>

SQLiteViewer::SQLiteViewer(QWidget *parent) : QMainWindow(parent) {
    setWindowTitle("SQLite Viewer");
    setGeometry(100, 100, 800, 600);

    // 创建数据库连接
//    db = QSqlDatabase::addDatabase("QSQLITE");
//    db.setDatabaseName("../ManagePlatform/db.sqlpite3");  // 替换为你的SQLite数据库文件名

//    if (!db.open()) {
//            qDebug() << "Failed to open the database: " << db.lastError().text(); // 输出错误信息
//            QApplication::exit(1);
//        }

    // 获取当前执行文件的路径
        QString executablePath = QCoreApplication::applicationDirPath();
        qDebug() << executablePath << "\n";

        // 构建数据库文件的绝对路径
        QString dbFilePath = QFileInfo(executablePath + "/../ManagePlatform/db.sqlite3").canonicalFilePath();
        qDebug() << dbFilePath;

        // 创建一个数据库连接
        QSqlDatabase db = QSqlDatabase::addDatabase("QSQLITE");

        // 设置数据库的文件名
        db.setDatabaseName(dbFilePath);

    // 创建模型
    model = new QSqlQueryModel(this);

    // 创建视图
    table_view = new QTableView(this);
    table_view->setModel(model);

    // 创建布局
    QVBoxLayout *layout = new QVBoxLayout();

    // 添加表格视图到布局
    layout->addWidget(table_view);

    // 添加布局到主窗口
    QWidget *central_widget = new QWidget(this);
    central_widget->setLayout(layout);
    setCentralWidget(central_widget);

    // 添加刷新按钮
    QPushButton *refresh_button = new QPushButton("Refresh Data", this);
    connect(refresh_button, &QPushButton::clicked, this, &SQLiteViewer::refreshData);
    layout->addWidget(refresh_button);

    // 添加查询输入框和按钮
    QLabel *query_label = new QLabel("SQL Query:", this);
    query_input = new QLineEdit(this);
    QPushButton *query_button = new QPushButton("Execute Query", this);
    connect(query_button, &QPushButton::clicked, this, &SQLiteViewer::executeQuery);

    layout->addWidget(query_label);
    layout->addWidget(query_input);
    layout->addWidget(query_button);
}

void SQLiteViewer::refreshData() {
    // 刷新数据
    model->setQuery("SELECT * FROM your_table");  // 替换为你的表名
}

void SQLiteViewer::executeQuery() {
//     执行自定义查询
        QString queryStr = query_input->text();
        QSqlQuery query(queryStr, db); // 使用当前数据库连接创建查询对象

//        if (!query.isValid()) { // 检查查询是否有效
//            qDebug() << "Invalid query: " << query.lastError().text(); // 输出错误信息
//            return; // 如果查询无效，直接返回，不执行后续操作
//        }

//        // 设置模型的查询
//        model->setQuery(query);


//    // 执行自定义查询
//    QString query = query_input->text();
//    model->setQuery(query);
//    if (!model->query().isValid()) { // 检查查询是否有效
//        qDebug() << "Invalid query: " << model->query().lastError().text(); // 输出错误信息
//    }


    // 执行自定义查询
//        QString queryStr = query_input->text();
//        QSqlQuery query(db); // 使用当前数据库连接创建查询对象
//        query.prepare(queryStr);

//        if (!query.exec()) { // 检查查询是否执行成功
//            qDebug() << "Query execution failed: " << query.lastError().text(); // 输出错误信息
//            return; // 如果查询失败，直接返回，不执行后续操作
//        }

//        // 设置模型的查询
//        if (!model->setQuery(query)) {
//            qDebug() << "Failed to set query to model: " << model->lastError().text(); // 输出错误信息
//            return; // 如果设置查询失败，直接返回，不执行后续操作
//        }


    // 执行自定义查询
//        QString queryStr = query_input->text();
//        QSqlQuery query(db); // 使用当前数据库连接创建查询对象
//        query.prepare(queryStr);

//        if (!query.exec()) { // 检查查询是否执行成功
//            qDebug() << "Query execution failed: " << query.lastError().text(); // 输出错误信息
//            return; // 如果查询失败，直接返回，不执行后续操作
//        }

//        // 手动将查询结果添加到模型中
//        QSqlRecord rec = query.record();
//        QStringList headers;
//        for (int i = 0; i < rec.count(); ++i) {
//            headers << rec.fieldName(i);
//        }
//        model->clear(); // 清空模型数据
//        model->setColumnCount(rec.count()); // 设置列数
//        model->setHorizontalHeaderLabels(headers); // 设置表头
//        int row = 0;
//        while (query.next()) {
//            model->insertRow(row); // 插入新行
//            for (int i = 0; i < rec.count(); ++i) {
//                QModelIndex index = model->index(row, i); // 获取索引
//                model->setData(index, query.value(i)); // 设置数据
//            }
//            ++row;
//        }

}
