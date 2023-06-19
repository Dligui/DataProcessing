#pragma once

#include <QtWidgets/QDialog>

class QTreeView;
class QFileSystemModel;
class QLineEdit;
class QPushButton;

class CDirSelectionDlg : public QDialog {
    Q_OBJECT

public:
    CDirSelectionDlg(const QString initialPath, QWidget *parent = nullptr);
    QDir directory() const;

private:
    void onCurrentChanged();

    QTreeView *m_treeView;
    QFileSystemModel *m_model;
    QLineEdit *m_folderName;
    QPushButton *m_OKbutton;
    QString m_initialPath;
};