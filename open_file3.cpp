class DirectorySelectionDialog(QDialog):
    def __init__(self, initial_path: Path, parent: QWidget) -> None:
        super().__init__(parent=parent)

        self.initial_path = initial_path
        self.setMinimumSize(200, 300)
        self.resize(400, 430)
        
        self.model = QFileSystemModel(parent=self)
        self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        root_index = self.model.setRootPath(str(self.initial_path))
        
        self.tree_view = QTreeView(parent=self)
        self.tree_view.setModel(self.model)
        self.tree_view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tree_view.setHeaderHidden(True)
        self.tree_view.setSortingEnabled(True)
        self.tree_view.sortByColumn(0, Qt.AscendingOrder)
        for i in range(1, self.model.columnCount()):
            self.tree_view.setColumnHidden(i, True)
        self.tree_view.scrollTo(root_index)
        self.tree_view.selectionModel().setCurrentIndex(root_index, QItemSelectionModel.Current | QItemSelectionModel.Select)
        self.tree_view.selectionModel().selectionChanged.connect(self.onCurrentChanged)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.ok_button = button_box.button(QDialogButtonBox.Ok)

        label = QLabel("Folder:")
        self.folder_name = QLineEdit(parent=self)
        self.folder_name.setReadOnly(True)
        self.folder_name.setText(self.initial_path.name)
        path_layout = QHBoxLayout()
        path_layout.addWidget(label)
        path_layout.addSpacing(10)
        path_layout.addWidget(self.folder_name)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tree_view)
        main_layout.addSpacing(10)
        main_layout.addLayout(path_layout)
        main_layout.addSpacing(10)
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)

    def onCurrentChanged(self):
        file_info = self.model.fileInfo(self.tree_view.selectionModel().currentIndex())
        self.folder_name.setText(file_info.fileName())
        self.ok_button.setEnabled(file_info.isDir())
        self.ok_button.setDefault(file_info.isDir())

    def directory(self) -> Path:
        file_info = self.model.fileInfo(self.tree_view.selectionModel().currentIndex())
        return Path(file_info.absoluteFilePath())